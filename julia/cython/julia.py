import time
import numpy as np
import juliac
import matplotlib.pyplot as plt

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calc_cython(width, max_iterations):
    x_step  = (x2 - x1) / width
    y_step  = (y1 - y2) / width

    x = []
    y = []

    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    zs = np.array(zs)
    cs = np.array(cs)

    start_time = time.time()
    result = juliac.calculate_z(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(f'Took {secs:0.2f} seconds')

    result = np.array(result).reshape((width, width))
    plt.imshow(result)
    plt.show()


if __name__ == '__main__':
    calc_cython(1000, 300)
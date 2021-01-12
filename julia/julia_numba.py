import time
import numpy as np
from numba import jit, prange
import matplotlib.pyplot as plt

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

@jit(nopython=False, parallel=True)
def calculate_z(maxiter, zs, cs, output):
    """Calculate output list using Julia update rule"""
    for i in prange(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < maxiter and (z.real*z.real + z.imag*z.imag) < 4:
            z = z*z + c
            n += 1

        output[i] = n

def calc_pure_python(width, max_iterations):
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
    output = np.empty(len(zs), dtype=np.int32)

    start_time = time.time()
    calculate_z(max_iterations, zs, cs, output)
    end_time = time.time()
    secs = end_time - start_time
    print(f'Took {secs:0.2f} seconds')

    result = output.reshape((width, width))
    plt.imshow(result)
    plt.show()


if __name__ == '__main__':
    calc_pure_python(1000, 300)
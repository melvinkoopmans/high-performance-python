import time
import numpy as np
import matplotlib.pyplot as plt

# Area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        return func


@profile
def calculate_z_serial_purepython(maxiter, x, y):
    """Calculate output list using Julia update rule"""
    output = []

    for ycoord in y:
        for xcoord in x:
            z = complex(xcoord, ycoord)
            c = complex(c_real, c_imag)
            n = 0

            while abs(z) < 2 and n < maxiter:
                z = z*z + c
                n += 1

            output.append(n)

    return output


def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs), build Julia set"""
    x_step  = (x2 - x1) / desired_width
    y_step  = (y1 - y2) / desired_width

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

    start_time = time.time()
    result = calculate_z_serial_purepython(max_iterations, x, y)
    end_time = time.time()
    secs = end_time - start_time
    print(f'Took {secs:0.2f} seconds')

    result = np.array(result).reshape((desired_width, desired_width))
    plt.imshow(result)
    plt.show()


if __name__ == '__main__':
    calc_pure_python(1000, 300)

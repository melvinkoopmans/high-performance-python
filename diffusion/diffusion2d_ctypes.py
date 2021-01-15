import os
import ctypes
import numpy as np
import matplotlib.pyplot as plt

from diffusion2d import initialize_grid
from utils.profiling import timefn

grid_shape = (512, 512)

# Import shared library
_diffusion = ctypes.CDLL(os.path.join(os.getcwd(), "diffusion.so"))

# Create references to the C types.
TYPE_INT = ctypes.c_int
TYPE_DOUBLE = ctypes.c_double
TYPE_DOUBLE_SS = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

# Set types of arguments and return value.
_diffusion.evolve.argtypes = [TYPE_DOUBLE_SS, TYPE_DOUBLE_SS, TYPE_DOUBLE, TYPE_DOUBLE]
_diffusion.evolve.restype = None


def evolve(grid, out, dt, D=1.0):
    assert grid.shape == (512, 512)
    # Type casting.
    cdt = TYPE_DOUBLE(dt)
    cD = TYPE_DOUBLE(D)

    # Obtain a pointer to the grid and out.
    pointer_grid = grid.ctypes.data_as(TYPE_DOUBLE_SS)
    pointer_out = out.ctypes.data_as(TYPE_DOUBLE_SS)

    _diffusion.evolve(pointer_grid, pointer_out, cD, cdt)


@timefn
def run_experiment():
    grid = np.array(initialize_grid(grid_shape))
    out = np.zeros(grid_shape)

    for i in range(10):
        evolve(grid, out, 0.1)
        grid, out = out, grid

    return out


if __name__ == '__main__':
    result = run_experiment()

    plt.imshow(result)
    plt.show()

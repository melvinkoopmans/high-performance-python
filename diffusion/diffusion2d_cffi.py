import matplotlib.pyplot as plt
import numpy as np
from cffi import FFI
from diffusion2d import initialize_grid

from utils.profiling import timefn

grid_shape = (512, 512)

ffi = FFI()
ffi.cdef("void evolve(double **in, double **out, double D, double dt);")
lib = ffi.dlopen("./diffusion.so")


def evolve(grid, out, dt, D=1.0):
    assert grid.shape == (512, 512)

    # Obtain a pointer to the grid and out.
    pointer_grid = ffi.cast("double**", grid.ctypes.data)
    pointer_out = ffi.cast("double**", out.ctypes.data)

    lib.evolve(pointer_grid, pointer_out, D, dt)


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

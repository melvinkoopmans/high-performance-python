import numpy as np
from cffi import FFI

from utils.profiling import timefn

grid_shape = (512, 512)

ffi = FFI()
ffi.cdef("void evolve(double **in, double **out, double D, double dt);")
lib = ffi.dlopen("./diffusion.so")


@timefn
def evolve(grid, out, dt, D=1.0):
    assert grid.shape == (512, 512)

    # Obtain a pointer to the grid and out.
    pointer_grid = ffi.cast("double**", grid.ctypes.data)
    pointer_out = ffi.cast("double**", out.ctypes.data)

    lib.evolve(pointer_grid, pointer_out, D, dt)


if __name__ == '__main__':
    grid = np.random.rand(*grid_shape)
    out = np.zeros(grid_shape)

    evolve(grid, out, 0.01)
    print(out)

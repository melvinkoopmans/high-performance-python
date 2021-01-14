from cdiffusion import evolve
import numpy as np
from utils.profiling import timefn

grid_shape = (512, 512)


@timefn
def evolve_timed(grid, out, dt, D=1.0):
    for i in range(10_000):
        evolve(grid, out, dt, D)


if __name__ == '__main__':
    grid = np.random.rand(*grid_shape).astype(np.double)
    out = np.zeros(grid_shape, dtype=np.double)

    evolve_timed(grid, out, 1.0, 0.01)
    print(out)

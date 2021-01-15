from cdiffusion import evolve
import numpy as np

from diffusion2d import initialize_grid
from utils.profiling import timefn
import matplotlib.pyplot as plt

grid_shape = (512, 512)


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

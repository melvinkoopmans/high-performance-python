import matplotlib.pyplot as plt
import numpy as np
from numpy import roll

from utils.profiling import timefn

grid_shape = (640, 640)


def laplacian(grid):
    return (
        roll(grid, +1, 0) +
        roll(grid, -1, 0) +
        roll(grid, +1, 1) +
        roll(grid, -1, 1) -
        4 * grid
    )


def evolve(grid, dt, D=1.0):
    return grid + dt * D * laplacian(grid)


@timefn
def run_experiment(grid):
    for i in range(10_000):
        grid = evolve(grid, 0.1)

    return grid


def initialize_grid(grid_shape):
    # Initial conditions
    x_max, y_max = grid_shape
    grid = [[0.0] * y_max for x in range(x_max)]

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    for i in range(block_low, block_high):
        for j in range(block_low, block_high):
            grid[i][j] = 0.005

    return grid


if __name__ == '__main__':
    grid = np.array(initialize_grid(grid_shape))

    # Evolve
    result = run_experiment(grid)

    plt.imshow(result)
    plt.show()



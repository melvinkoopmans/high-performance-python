import torch
from torch import (roll, zeros)
import matplotlib.pyplot as plt

grid_shape = (640, 640)


def laplacian(grid: torch.Tensor):
    return (
        roll(grid, +1, 0)
        + roll(grid, -1, 0)
        + roll(grid, +1, 1)
        + roll(grid, -1, 1)
        - 4 * grid
    )


def evolve(grid, dt, d=1):
    return grid + dt * d * laplacian(grid)


def run_experiment(num_iterations):
    grid = zeros(grid_shape)

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005

    grid = grid.cuda()
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)

    return grid


if __name__ == '__main__':
    # TODO: Compare to NumPy implementation, plot results.
    result = run_experiment(10)

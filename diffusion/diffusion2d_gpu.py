import torch
from torch import (roll, zeros)
import matplotlib.pyplot as plt

from diffusion2d import initialize_grid
from utils.profiling import timefn

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


@timefn
def run_experiment(grid, num_iterations):
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)

    return grid


if __name__ == '__main__':
    grid = torch.tensor(initialize_grid(grid_shape))
    grid = grid.cuda()

    result = run_experiment(grid, 10_000)

    plt.imshow(result.cpu().numpy())
    plt.show()

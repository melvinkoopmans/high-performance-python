import matplotlib.pyplot as plt

from utils.profiling import timefn

grid_shape = (640, 640)


def evolve(grid, out, dt, D=1.0):
    x_max, y_max = grid_shape
    for i in range(x_max):
        for j in range(y_max):
            grid_xx = (
                grid[(i + 1) % x_max][j] + grid[(i - 1) % x_max][j] - 2.0 * grid[i][j]
            )
            grid_yy = (
                grid[i][(j + 1 ) % y_max] + grid[i][(j - 1) % y_max] - 2.0 * grid[i][j]
            )
            out[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt

    return out


@timefn
def run_experiment(grid):
    x_max, y_max = grid_shape
    out = [[0.0] * y_max for x in range(x_max)]

    for i in range(10):
        evolve(grid, out, 0.1)
        grid, out = out, grid

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
    grid = initialize_grid(grid_shape)

    # Evolve
    result = run_experiment(grid)

    plt.imshow(result)
    plt.show()



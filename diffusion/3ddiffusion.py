from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm, animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from scipy.stats import multivariate_normal

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)

dist = multivariate_normal(
    mean=[0, 0],
    cov=[
        [1, 0],
        [0, 0.25],
    ]
)

pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y
Z = dist.pdf(pos)

# Plot the surface.
plot = [ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)]

ax.set_zlim(0, max(Z.reshape(-1)))
ax.view_init(elev=10, azim=0)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

D = 1
dt = 0.2


def update(frame):
    N = Z.shape[0]
    M = Z.shape[1]

    for i in range(1, N - 2):
        for j in range(1, M - 2):
            Z[i][j] = Z[i][j] + D * dt * (
                    (Z[(i + 1) % N][j] + Z[(i - 1) % N][j] - 2 * Z[i][j]) +  # d^2 u / dx^2
                    (Z[i][(j + 1) % M] + Z[i][(j - 1) % M] - 2 * Z[i][j])
            )

    # Update surface plot.
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)

    # Rotation
    ax.view_init(elev=10 + min(frame/30, 15), azim=1/4 * frame)

    return plot,


fps = 30
duration = 12 # seconds
frames = fps*duration

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1)
ani.save('3ddiffusion.mp4', fps=fps)

plt.show()

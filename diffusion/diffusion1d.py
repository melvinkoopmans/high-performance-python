import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
N = 200
x_data = list(range(1, N))
# y_data = [0 if i < 75 or i > 125 else 1 for i in x_data]
y_data = np.sin([0.1 * x for x in x_data])
y_data = y_data + np.sin([0.2 * x for x in x_data])
y_data = y_data + np.sin([0.3 * x for x in x_data])

ln, = plt.plot([], [])


def init():
    ax.set_xlim(0, N)
    ax.set_ylim(1.1 * min(y_data), 1.1 * max(y_data))
    return ln,


D = 1
dt = 0.4


# dt = 0.0000001

def update(frame):
    for i in range(N):
        if i <= 1:
            y_data[i] = 0
            continue
        if i >= N - 2:
            y_data[i] = 0
            break

        y_data[i] = y_data[i] + D * dt * (y_data[(i + 1) % N] + y_data[(i - 1) % N] - 2 * y_data[i])

    ln.set_data(x_data, y_data)

    return ln,


fps = 30
duration = 20  # seconds
frames = fps * duration

ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, interval=1)
ani.save('diffusion1d.mp4', fps=fps)

plt.show()

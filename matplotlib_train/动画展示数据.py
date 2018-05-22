import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 ** np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def my_animation(i):
    line.set_ydata(np.sin(x + i / 60))
    return line,


def init():
    line.set_ydata(np.sin(x))
    return line,


ani = animation.FuncAnimation(fig=fig, func=my_animation, init_func=init, interval=20, blit=False)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.figure(num=1)
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.plot(x, y1, color="red", linestyle="--")
plt.plot(x, y2, color="blue",)

# plt.xlim((-1, 1))
# plt.ylim((0, 1))

plt.xlabel("x")
plt.ylabel("y")

new_ticks = np.linspace(-2, 3, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks(np.linspace(-1, 3, 4), ["bad", "normal", "good", "$very\ good$"])

ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

# l1 = plt.plot(x, y1)
# l2 = plt.plot(x, y2)

import matplotlib.lines as mlines
red_lines = mlines.Line2D([x], [y1], color="red", marker="", markersize=15, label="y = 2 * x + 1")
blue_lines = mlines.Line2D([x], [y2], color="blue", marker="", markersize=15, label="y = x ** 2")
plt.legend(handles=[blue_lines, red_lines])

# plt.scatter(x, y1)

x0 = 0.2
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color="b")

plt.plot([x0, x0], [y0, 0], "k--", lw=2)

plt.annotate(r"$2*{}+1={}$".format(x0, y0), xy=(x0, y0),
             xycoords="data", xytext=(+30, -30), textcoords="offset points",
             fontsize=15, arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))

plt.text(-1, 1.5, "$This\ is \ some\ text!$")

plt.show()

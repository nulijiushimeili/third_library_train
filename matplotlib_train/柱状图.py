import matplotlib.pyplot as plt
import numpy as np

# 制造数据
n = 12
x = np.arange(n)
y = (1 - x / float(n) * np.random.uniform(0.5, 1.0, n))

# 画柱状图
plt.bar(x, +y, facecolor="#9999ff", edgecolor="#ffffff")

# 设置坐标轴的限定范围
plt.xlim(-1, n)
plt.ylim(0, 1)

# 设置坐标轴的位置
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", -1))

# 在柱状图上标注数值
for x, y in zip(x, y):
    plt.text(x, y, "%.2f" % y, ha="center", va="bottom")

# 显示图像
plt.show()

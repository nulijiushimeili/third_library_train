import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

# 设置窗口的大小()
plt.figure(num=3, figsize=(5, 5))

# 生成x,y轴的坐标
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

# x,y是象限参数,linestyle是线段的样式
# plt.plot(x, y1, linestyle="--", color="b", linewidth=1.0)

# 限定x,y轴的取值范围
plt.xlim((-1, 3))
plt.ylim((0, 3))

# 替换x,y轴的小标
new_ticks = np.linspace(-1.5, 3, 5)
plt.xticks(new_ticks)

# 自定义小标的名称(如果需要输入两个单词,可以使用正则表达式)
plt.yticks(np.linspace(-1, 3, 4), ["$really\ bad$", "normal", "good", "better"])

# 设置坐标轴的位置
# gca -> "get current axis"
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

# x,y轴的介绍
plt.xlabel("x")
plt.ylabel("y")

# 给每条线起个名字
l1 = plt.plot(x, y1)
l2 = plt.plot(x, y2)

# 图例介绍
blue_line = lines.Line2D([x], [y1], color="blue", marker="", markersize=15, label="y=2*x+1")
red_line = lines.Line2D([x], [y2], color="red", marker="", markersize=15, label="y=x**2")
plt.legend(handles=[blue_line, red_line])

# 在图中指定的位置画一个点,并描述这个点的含义
x0 = 0.5
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color="blue")
plt.plot([x0, x0], [y0, 0], "k--", lw=2)

plt.annotate(r"$2x+1=%d$" % y0, xy=(x0, y0), xycoords="data", xytext=(+30, -30), textcoords="offset points",
             fontsize=15, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 在指定的位置输出一段文字
plt.text(1, 0.4, "$This\ is\ some\ text!$", fontsize=15)

# 画图,没有这个不会显示
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 定义一个figure
fig = plt.figure()
x = np.arange(2, 10)
y = np.arange(-5, 3)

# 定义figure的大小和位置
left, bottom, width, height = 0.1, 0.1, 1, 1
ax1 = fig.add_axes([left, bottom, width, height])
# 画出x,y
ax1.plot(x, y, c="r")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

# 第一个内部小图
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, "b")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("inside1")

# 第二个内部小图
left, bottom, width, height = 0.55, 0.15, 0.25, 0.25
ax3 = fig.add_axes([left,bottom,width,height])
ax3.plot(x,y,"g")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_title("inside2")

plt.show()

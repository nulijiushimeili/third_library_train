import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# 制造数据
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


# 生成256个数据
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
x, y = np.meshgrid(x, y)


# 为每个区域填充颜色
plt.contourf(x, y, f(x, y), 8, alpha=0.75, cmap=cm.hot)

# 画等高线图
c = plt.contour(x, y, f(x, y), 8, color="b", )

# 添加label
plt.clabel(c, inline=True, fontsize=10, color="b")

plt.xticks(())
plt.yticks(())
plt.show()

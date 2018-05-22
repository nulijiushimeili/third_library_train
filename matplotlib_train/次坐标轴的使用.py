import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y1 = 0.5 * x ** 2
y2 = -1 * y1

fig, ax1 = plt.subplots()

# 使用镜面将y轴上的数据反射过来
ax2 = ax1.twinx()

ax1.plot(x, y1, "g-")
ax2.plot(x, y2, "r-")

plt.show()

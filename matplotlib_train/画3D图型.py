# import numpy as np
# import matplotlib.pyplot as plt
# # 注意需要导入3D图形的包
# from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = Axes3D(fig)
#
# x = np.arange(-4, 4, 0.25)
# y = np.arange(-4, 4, 0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x ** 2, y ** 2)
# z = np.sin(r)
#
# ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))
#
# ax.contourf(x, y, z, zdir="z", offset=-2, cmap="rainbow")
# ax.set_zlim(-2, 2)
#
# plt.show()

# ----------------------------华丽的分割线----------------------------------

import numpy as np
import matplotlib.pyplot as plt
# 注意要导入3D图形包
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

# x,y轴的值
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
# 高度值
Z = np.sin(R)

# rstride=1, cstride=1, 代表的是密度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))

ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap="rainbow")
ax.set_zlim(-2, 2)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 数据
a = np.arange(1, 10).reshape(3, 3)
print(a)

# interpolation 可以在官网上看,有很多取值
# plt.imshow(a, interpolation="nearest", cmap="bone", origin="upper")
plt.imshow(a, interpolation="none", cmap=plt.cm.bone, origin="lower")
# 条形的指示图,shrink代表压缩比
plt.colorbar(shrink=0.9)

# 不显示坐标
plt.xticks(())
plt.yticks(())
plt.show()
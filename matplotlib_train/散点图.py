import matplotlib.pyplot as plt
import numpy as np

# 样本数据1024
n = 1024
# 生成随机数
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
# 生成颜色的值
c = np.arctan2(x, y)
# 开始画散点图
plt.scatter(x, y, s=75, c=c, alpha=0.75)
# 设置x,y轴的限制
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
# 将x,y轴的坐标去掉(()),里面的()代表替换掉原来的值
plt.xticks(())
plt.yticks(())
plt.show()

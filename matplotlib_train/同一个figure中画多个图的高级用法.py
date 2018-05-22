import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 1.subplot2grid
plt.figure()
# 第一个参数代表分成3行3列
# 第二个参数代表从在第几个格子里画
# rowspan & colspan 表示在行和列的维度上跨几个格子
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=2)
ax1.plot([1, 2], [1, 2])
ax1.set_title("ax1_title")
ax2 = plt.subplot2grid((3, 3), (2, 0), colspan=3, rowspan=1)
ax2.plot([-1, 9], [9, 3])
ax2.set_title("ax2_title")
plt.tight_layout()
plt.show()

# 2.gridspec
plt.figure()
gs = gridspec.GridSpec(3, 3)
# 从第一行占满所有的列
ax1 = plt.subplot(gs[0, :])
# 从第二行占满第二列之前的列
ax2 = plt.subplot(gs[1, :2])
# 从第二行开始占满第二行之后的行
ax3 = plt.subplot(gs[1:, 2])
plt.tight_layout()
plt.show()


# 3.定义结构
plt.figure()
# 使用subplots,,,sharex,共享x轴  sharey,共享y轴
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])

# 注意还有这句代码
plt.tight_layout()
plt.show()

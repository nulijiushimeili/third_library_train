import numpy as np

# 创建一个矩阵
matrix1 = np.array([[1, 2],
                    [3, 4]])
# print(matrix1)

# 查看矩阵是几维数组
print(matrix1.ndim)
# 查看矩阵是几行几列
print(matrix1.shape)
# 查看矩阵中元素的个数
print(matrix1.size)

# 设置数组的数据类型
# dtype = int64,int32,int16,float64,float32
# 默认是64位
a = np.array([1, 2, 3, 4], dtype=np.int32)
print(a.dtype)

# 生成一个数组,指定数组的区间和个数,该数组的每个元素之间是等距的
b = np.linspace(0, 100, 5)
print(b)

# 生成矩阵
A = np.arange(0, 12).reshape(3, 4)
print(A)
# 矩阵的累加
print(A.cumsum())
# [ 0  1  3  6 10 15 21 28 36 45 55 66]
# 对矩阵的元素进行排序
print(np.sort(A))

B = np.arange(1, 5).reshape(2, 2)
C = np.arange(3, 7).reshape(2, 2)
print(B)
print(C)
# 矩阵的点乘
D = B.dot(C)
# 注意顺序,如果顺序调换了,结果也会不一样(等同于上面的写法)
E = np.dot(B, C)
print(D)
print(E)

# 查看矩阵中对应的元素
# 查看第3行第3列的值,注意下标是从0开始
print(A[2, 2])
print(A[2][2])
# 查看第二行以后所有的行,注意下标是从1开始
print(A[2:])
# 查看第2行以前的所有行,下标是从1开始
print(A[:1])
# 如果想要查看某一列的值可以使用转置
print(A.T[1:3])
# [[ 1  5  9]
#  [ 2  6 10]]
# 返回的是第一行和第二行的值
print()

# 遍历矩阵和矩阵的转置
# 查看矩阵每一行的数据
for row in A:
    print(row)
# 查看矩阵每一列的数据
for col in A.T:
    pass
# 矩阵转置的另一种写法,等同与上面的A.T
for col in np.transpose(A):
    print(col)

# 拼接矩阵
F = np.array([2, 2, 2])[:, np.newaxis]
G = np.array([5, 5, 5])[:, np.newaxis]
print(F)
print(G)
# 纵向合并矩阵(3行变成6行)
H = np.vstack((F, G))
print(H)
# 横向合并矩阵(一列变成两列)
J = np.hstack((F, G))
print(J)
# 纵向合并矩阵
K = np.concatenate((F, G), axis=0)
print(K)
# 横向合并矩阵
L = np.concatenate((F, G), axis=1)
print(L)

# 生成1-16的方阵
M = np.arange(1, 17).reshape(4, 4)
print(M)
# 小于设定的最小值,则赋值最小值
# 大于设定的最大值,则赋值最大值
N = np.clip(M, 5, 10)
print(N)
# [[ 5  5  5  5]
#  [ 5  6  7  8]
#  [ 9 10 10 10]
#  [10 10 10 10]]

# 切分矩阵
# 横向切分
Q = np.split(M, 2, axis=0)
# 纵向切分
P = np.split(M, 2, axis=1)
print(Q)
print(P)
# 横向切分数组
U = np.vsplit(M, 2)
# 纵向切分数组
V = np.hsplit(M, 2)
print(U)
print(V)

# 复制矩阵
# 建立真正的副本,指向不同的内存空间
W = M.copy()
# 这个仅仅是引用传递
X = M
print(W)
print(W is M)
print(X is M)

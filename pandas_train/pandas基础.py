import numpy as np
import pandas as pd

# 创建一个序列
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
# 0     1.0
# 1     3.0
# 2     6.0
# 3     NaN
# 4    44.0
# 5     1.0
# dtype: float64

# 生成一个时间序列
dates = pd.date_range("20160101", periods=6)
print(dates)
# DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
#                '2016-01-05', '2016-01-06'],
#               dtype='datetime64[ns]', freq='D')

# 创建一个数据框,指定行和列的索引
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=["A", "B", "C", "D"])
print(df)
#                    A         B         C         D
# 2016-01-01  0.969381  0.483409  0.469310  0.759778
# 2016-01-02  0.291548  0.426283  0.740162  0.443385
# 2016-01-03  0.625571  0.262858  0.511033  0.127727
# 2016-01-04  0.877843  0.794533  0.243019  0.399019
# 2016-01-05  0.235939  0.800824  0.714343  0.143092
# 2016-01-06  0.721514  0.057687  0.012479  0.298619

# pandas默认的序列0,1,2,...
df1 = pd.DataFrame(np.arange(1, 13).reshape(3, 4))
print(df1)
#    0   1   2   3
# 0  1   2   3   4
# 1  5   6   7   8
# 2  9  10  11  12

# 使用字典生成数据框
dic = {
    "小明": "xiaoming",
    "小红": "xiaohong",
    "小华": "xiaohua",
    "小刚": "xiaogang",
    "老李": "laoli",
    "大名": pd.Series([3, 4, "none", True])
}
df2 = pd.DataFrame(dic)
print(df2)
#      大名        小刚       小华        小明        小红     老李
# 0     3  xiaogang  xiaohua  xiaoming  xiaohong  laoli
# 1     4  xiaogang  xiaohua  xiaoming  xiaohong  laoli
# 2  none  xiaogang  xiaohua  xiaoming  xiaohong  laoli
# 3  True  xiaogang  xiaohua  xiaoming  xiaohong  laoli

# 查看每一列的数据类型
print(df.dtypes)
# A    float64
# B    float64
# C    float64
# C    float64
# dtype: object

# 返回df的列名
print(df.columns)
# Index(['A', 'B', 'C', 'D'], dtype='object')

# 返回df的所有的值
print(df.values)
# [[0.41551966 0.00948096 0.90188901 0.67548289]
#  [0.08186594 0.14332108 0.19490506 0.97090662]
#  [0.30699519 0.65867843 0.71535053 0.46159662]
#  [0.42044557 0.47991125 0.0229145  0.20688395]
#  [0.29459892 0.39391302 0.37503309 0.44629916]
#  [0.11946022 0.3684851  0.66015322 0.44008341]]

# 查看数据的统计相关的信息
print(df1.describe())
#          0     1     2     3
# count  3.0   3.0   3.0   3.0
# mean   5.0   6.0   7.0   8.0
# std    4.0   4.0   4.0   4.0
# min    1.0   2.0   3.0   4.0
# 25%    3.0   4.0   5.0   6.0
# 50%    5.0   6.0   7.0   8.0
# 75%    7.0   8.0   9.0  10.0
# max    9.0  10.0  11.0  12.0

# 转置
print(df2.T)
#            0         1         2         3
# 大名         3         4      none      True
# 小刚  xiaogang  xiaogang  xiaogang  xiaogang
# 小华   xiaohua   xiaohua   xiaohua   xiaohua
# 小明  xiaoming  xiaoming  xiaoming  xiaoming
# 小红  xiaohong  xiaohong  xiaohong  xiaohong
# 老李     laoli     laoli     laoli     laoli

# axis=1 对列进行排序
# ascending=False  倒序排序
print(df.sort_index(axis=1, ascending=False))
#                    D         C         B         A
# 2016-01-01  0.898244  0.326733  0.366118  0.763515
# 2016-01-02  0.979316  0.280069  0.097486  0.094180
# 2016-01-03  0.926560  0.087694  0.725952  0.361708
# 2016-01-04  0.251664  0.435591  0.360976  0.122582
# 2016-01-05  0.494071  0.581114  0.301435  0.382009
# 2016-01-06  0.756356  0.864808  0.196476  0.031030

# 对D这一列进行排序
print(df.sort_values(by="D"))

# 创建DataFrame
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=["A", "B", "C", "D"])
print(df)
#                    A         B         C         D
# 2016-01-04  0.767543  0.202745  0.536597  0.014253
# 2016-01-03  0.671961  0.563432  0.279912  0.117155
# 2016-01-06  0.152405  0.977533  0.522810  0.439084
# 2016-01-01  0.470468  0.297487  0.924779  0.529722
# 2016-01-05  0.948680  0.054530  0.375037  0.704765
# 2016-01-02  0.749658  0.666558  0.170298  0.865731

# 查看数据某一列的值
print(df["A"], df.A)
# 2013-01-01     0
# 2013-01-02     4
# 2013-01-03     8
# 2013-01-04    12
# 2013-01-05    16
# 2013-01-06    20
# Freq: D, Name: A, dtype: int32
# 2013-01-01     0
# 2013-01-02     4
# 2013-01-03     8
# 2013-01-04    12
# 2013-01-05    16
# 2013-01-06    20
# Freq: D, Name: A, dtype: int32

# 查看指定行的数据
print(df[0:3], df["20130102":"20130105"])
#             A  B   C   D
# 2013-01-01  0  1   2   3
# 2013-01-02  4  5   6   7
# 2013-01-03  8  9  10  11
#             A   B   C   D
# 2013-01-02   4   5   6   7
# 2013-01-03   8   9  10  11
# 2013-01-04  12  13  14  15
# 2013-01-05  16  17  18  19

# 查看第二行的值
print(df.loc["20130102"])
# A    4
# B    5
# C    6
# D    7
# Name: 2013-01-02 00:00:00, dtype: int32

# 查看指定列的值
print(df.loc[:, ["A", "B"]])
#              A   B
# 2013-01-01   0   1
# 2013-01-02   4   5
# 2013-01-03   8   9
# 2013-01-04  12  13
# 2013-01-05  16  17
# 2013-01-06  20  21

# 返回指定区域的数据
print(df.loc["20130102", ["A", "B"]])
# A    4
# B    5
# Name: 2013-01-02 00:00:00, dtype: int32

# 通过默认的索引进行返回
print(df.iloc[[1, 3, 5], 1:3])
#              B   C
# 2013-01-02   5   6
# 2013-01-04  13  14
# 2013-01-06  21  22

# 返回指定区域的数据
print(df.ix[:3, ["B", "D"]])
#             B   D
# 2013-01-01  1   3
# 2013-01-02  5   7
# 2013-01-03  9  11

# 按照条件筛选数据
print(df[df.A > 8])
#              A   B   C   D
# 2013-01-04  12  13  14  15
# 2013-01-05  16  17  18  19
# 2013-01-06  20  21  22  23

#
df.iloc[2, 2] = 100
df.loc["20130102", "D"] = 200
print(df)
#              A   B    C    D
# 2013-01-01   0   1    2    3
# 2013-01-02   4   5    6  200
# 2013-01-03   8   9  100   11
# 2013-01-04  12  13   14   15
# 2013-01-05  16  17   18   19
# 2013-01-06  20  21   22   23

# 改变某一列的值
df.A[df.A > 8] = 0
print(df)
#             A   B    C    D
# 2013-01-01  0   1    2    3
# 2013-01-02  4   5    6  200
# 2013-01-03  8   9  100   11
# 2013-01-04  0  13   14   15
# 2013-01-05  0  17   18   19
# 2013-01-06  0  21   22   23

# 给数据夹上一列值
df["F"] = np.nan
print(df)
#           A   B    C    D   F
# 2013-01-01  0   1    2    3 NaN
# 2013-01-02  4   5    6  200 NaN
# 2013-01-03  8   9  100   11 NaN
# 2013-01-04  0  13   14   15 NaN
# 2013-01-05  0  17   18   19 NaN
# 2013-01-06  0  21   22   23 NaN

# 对照原来的行添加一列数据
df["E"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
print(df)
#             A   B    C    D   F  E
# 2013-01-01  0   1    2    3 NaN  1
# 2013-01-02  4   5    6  200 NaN  2
# 2013-01-03  8   9  100   11 NaN  3
# 2013-01-04  0  13   14   15 NaN  4
# 2013-01-05  0  17   18   19 NaN  5
# 2013-01-06  0  21   22   23 NaN  6

# 修改数据
df["F"] = 0
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
#             A     B      C    D  F  E
# 2013-01-01  0   NaN    2.0    3  0  1
# 2013-01-02  4   5.0    NaN  200  0  2
# 2013-01-03  8   9.0  100.0   11  0  3
# 2013-01-04  0  13.0   14.0   15  0  4
# 2013-01-05  0  17.0   18.0   19  0  5
# 2013-01-06  0  21.0   22.0   23  0  6

# 丢掉带有nan数据的行 how="any" | "all"
df = df.dropna(axis=0, how="any")
print(df)
#            A     B      C   D  F  E
# 2013-01-03  8   9.0  100.0  11  0  3
# 2013-01-04  0  13.0   14.0  15  0  4
# 2013-01-05  0  17.0   18.0  19  0  5
# 2013-01-06  0  21.0   22.0  23  0  6

# 如果某一列的值都为nan,就丢弃这一列
df["F"] = np.nan
df = df.dropna(axis=1, how="all")
print(df)
#             A     B      C   D  E
# 2013-01-03  8   9.0  100.0  11  3
# 2013-01-04  0  13.0   14.0  15  4
# 2013-01-05  0  17.0   18.0  19  5
# 2013-01-06  0  21.0   22.0  23  6

# 查看数据中是否含有丢失的数据
df.iloc[3, 3] = np.nan
# 如果有丢失的数据,返回True
print(df.isnull)
print(np.any(df.isnull()) == True)

# 加载文件中的数据
data = pd.read_csv("decision_tree_data.csv")
print(data)

# 将数据保存成pickel文件
# data.to_pickle("data.pickle")

# 读取pickel文件
data1 = pd.read_pickle("data.pickle")
print(data1)

# 创建3个dataframe
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["A", "B", "C", "D"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["A", "B", "C", "D"])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=["A", "B", "C", "D"])

# 纵向合并
res = pd.concat([df1, df2, df3], axis=0)
print(res)
#      A    B    C    D
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0

# 横向拼接
res = pd.concat([df1, df2, df3], axis=1)
print(res)

# 修改索引,使之保持一直
res = pd.concat([df1, df2], ignore_index=True, axis=0)
print(res)
#      A    B    C    D
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0

# 合并不重合索引的DataFrame
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["A", "B", "C", "D"], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["B", "C", "D", "E"], index=[2, 3, 4])

# 拼接DataFrame
res = pd.concat([df1, df2])
print(res)
#      A    B    C    D    E
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0

# join默认是outer,保留共同都有的属性
res = pd.concat([df1, df2], join="inner")
print(res)
#      B    C    D
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0

# 横向拼接,以df1的index为准
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(res)
#      A    B    C    D    B    C    D    E
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0

# append()追加数据到
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["A", "B", "C", "D"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["A", "B", "C", "D"])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=["A", "B", "C", "D"], index=[2, 3, 4])
res = df1.append(df2, ignore_index=True)
print(res)
#      A    B    C    D
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0


res = df1.append([df2, df3])
print(res)
#      A    B    C    D
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
# 2  2.0  2.0  2.0  2.0
# 3  2.0  2.0  2.0  2.0
# 4  2.0  2.0  2.0  2.0

# 追加一个序列到df后面
s1 = pd.Series([1, 2, 3, 4], index=["A", "B", "C", "D"])
res = df1.append(s1, ignore_index=True)
print(res)
#      A    B    C    D
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  2.0  3.0  4.0

# 创建DF
left = pd.DataFrame({"key": ["K0", "K1", "K2", "K3"],
                     "A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]
                     })
right = pd.DataFrame({"key": ["K0", "K1", "K2", "K3"],
                      "C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]
                      })
print(left)
print(right)

# merge()合并dataframe
res = pd.merge(left, right, on="key")
print(res)
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3

left = pd.DataFrame({"key1": ["K0", "K0", "K1", "K2"],
                     "key2": ["K0", "K1", "K0", "K1"],
                     "A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]
                     })
right = pd.DataFrame({"key1": ["K0", "K1", "K1", "K2"],
                      "key2": ["K0", "K0", "K0", "K0"],
                      "C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]
                      })
print(left)
print(right)
#   key1 key2   A   B
# 0   K0   K0  A0  B0
# 1   K0   K1  A1  B1
# 2   K1   K0  A2  B2
# 3   K2   K1  A3  B3
#   key1 key2   C   D
# 0   K0   K0  C0  D0
# 1   K1   K0  C1  D1
# 2   K1   K0  C2  D2
# 3   K2   K0  C3  D3

# 参考两个key进行合并,默认是how="inner"
res = pd.merge(left, right, on=["key1", "key2"])
print(res)

# how的取值outer, inner, left, right

#
df1 = pd.DataFrame({"col1": [0, 1], "col_left": ["a", "b"]})
df2 = pd.DataFrame({"col1": [1, 2, 2], "col_right": [2, 2, 2]})
print(df1)
print(df2)
#    col1 col_left
# 0     0        a
# 1     1        b
#    col1  col_right
# 0     1          2
# 1     2          2
# 2     2          2

#
res = pd.merge(df1, df2, on="col1", how="outer", indicator="改名字")
print(res)
#    col1 col_left  col_right      _merge
# 0     0        a        NaN   left_only
# 1     1        b        2.0        both
# 2     2      NaN        2.0  right_only
# 3     2      NaN        2.0  right_only

#
left = pd.DataFrame({"A": ["A0", "A1", "A2"],
                     "B": ["B0", "B1", "B2"]},
                    index=["K0", "K1", "K2"])
right = pd.DataFrame({"C": ["C0", "C1", "C2"],
                      "D": ["D0", "D1", "D2"]},
                     index=["K0", "K2", "K3"])
print(left)
print(right)

# 对比两个DF中的index,进行合并
res = pd.merge(left, right, left_index=True, right_index=True, how="outer")
print(res)
#       A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C1   D1
# K3  NaN  NaN   C2   D2

# how=[inner, outer, left, right]
res = pd.merge(left, right, left_index=True, right_index=True, how="inner")
print(res)
#      A   B   C   D
# K0  A0  B0  C0  D0
# K2  A2  B2  C1  D1

# 创建DF
boys = pd.DataFrame({"k": ["K0", "K1", "K2"], "age": [1, 2, 3]})
girls = pd.DataFrame({"k": ["K0", "K0", "K3"], "age": [4, 5, 6]})
print(boys)
print(girls)
#     k  age
# 0  K0    1
# 1  K1    2
# 2  K2    3
#     k  age
# 0  K0    4
# 1  K0    5
# 2  K3    6

# 合并
res = pd.merge(boys, girls, on="k", suffixes=["_boy", "_girl"], how="inner")
print(res)
#     k  age_boy  age_girl
# 0  K0        1         4
# 1  K0        1         5

# 画图
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()

# DF
df = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
df = df.cumsum()
print(df.head(5))

# plot(这里跟plt.plot()方法的参数一样)
df.plot()
# data.plot()
plt.show()

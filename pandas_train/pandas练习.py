import pandas as pd
import numpy as np

# 生成类似于一维数组的对象
s = pd.Series([4, 7, -5, 3])
print(s)
print(s.values)
print(s.index)

# 指定Series的index
s1 = pd.Series([4, 7, -5, 3, 6], index=["a", "b", "c", "d", "e"])
print(s1)
print(s1.index)
print(s1["c"])
# 选取指定索引对应的值
print(s1[["a", "c", "e"]])
# 根据布尔型条件选取值
print(s1[s1 > 3])
# 可以将Series看做是一个字典,索引作为每个元素的映射,
# 查看是否包含某个索引
print("e" in s1)

# 通过字典创建Series
sdata = {
    "Anqila": 15,
    "Yase": 30,
    "Jingke": 20,
    "Libai": 50
}
s2 = pd.Series(sdata)
print(s2)
# 匹配指定位置的元素,生成新的Series,
# 如果这元素不存在,默认使用NA填充
sindex = ["Daji", "Yase", "Libai", "Chengyaojin"]
s3 = pd.Series(sdata, index=sindex)
print(s3)
# 查看Series中是否包含NA,丢失值
print(pd.isnull(s3))
print(s3.notnull())

# Series对象本身及其索引都有name属性
s3.name = "info"
s3.index.name = "name"
print(s3)

# Series的索引可以通过赋值的方式进行修改
s3.index = ["Bob", "Jack", "Tom", "Tima"]
print(s3)

# 使用字典构建DataFrame
data = {
    "name": ["Yase", "Anqila", "Daji", "Xiaoqiao", "Chengyaojin"],
    "age": [30, 20, 15, 18, 40],
    "address": ["Eng", "Yidali", "Qianhudong", "Wu", "Tang"]
}
df = pd.DataFrame(data)
print(df)

# 按照指定的列进行排序
df = pd.DataFrame(data, columns=["name", "address", "age", "gender"],
                  index=["one", "two", "three", "four", "five"])
print(df)
print(df.columns)
print(df["address"])
# 列名可以当做属性来访问
print(df.name)
# 通过索引访问行的信息
print(df.ix["three"])
# 对列的值进行赋值
df.gender = "male"
print(df)
df.age = np.arange(900, 905)
print(df)

# 将列表或数组赋值给DataFrame某个列时,如果赋值的是一个Series,
# 就会精确匹配DataFrame的索引,其他的空位置都会被天上确实值
# 索引不存在的话不会创建新的行
new_age = pd.Series([500, 409, 666], index=["tow", "three", "five"])
df.age = new_age
print(df)

# 为不存在的列赋值会被创建一个新的列
df["eastern"] = df.name == "Yase"
print(df)

# 使用del() 删除列
del (df["eastern"])
print(df)

# 使用嵌套字典创建DataFrame
pop = {
    "Nevada": {2001: 2.4, 2002: 2.9},
    "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}
}
df = pd.DataFrame(pop)
print(df)
print(df.T)
# 内存字典的键最终会被合并排序以形成最终的索引
# 如果显式的指定了索引
# df = pd.DataFrame(pop, index=[2001, 2002, 2000])
# print(df) 运行出错

# 字典 键值对组成的集合
# 键必须不可变类型【元组，字符串】，值可以任意类型
# key唯一，存在重复时，后者覆盖前者

dictA = {"pro":"艺术","school":"北京电影学院"}
# 添加字典数据===============================
dictA["name"]="李易峰"
dictA["age"]=30
dictA["pos"]="歌手"
# print(type(dictA))
print(dictA)
dictA["name"] = "谢霆锋"
# print(dictA["name"])
# print(dictA["age"])
print(dictA)

# print(dictA.keys())
# print(dictA.values())
dictA.update({"age":'40'})

print(dictA.items())
# for key,value in dictA.items():
#     print("%s==%s"%(key,value))
print(sorted(dictA.items(),key=lambda d:d[0]))#根据key排序
print(sorted(dictA.items(),key=lambda d:d[1]))#根据value排序
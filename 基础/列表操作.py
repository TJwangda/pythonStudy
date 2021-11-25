# 列表数据可以改变，内存地址不变

# li = []
# li = [1,2,3,"你好"]
# strA = "我喜欢python"
# print(type(li))
# print(len(li))
# print(len(strA))

#查找===============================================
listA = ["abcd",785,12.23,"qiuzhi",True]
# print(listA)
# print(listA[0])
# print(listA[1:3])
# print(listA[2:])
# print(listA*2)#输出多次

# 增加===============================================
# listA.append(["fff","ddd"])
# listA.append("888")
# listA.insert(1,"刚插入的数据")
# rsData = list(range(10))
# print(type(rsData))
#
# # 扩展list，批量添加
# listA.extend(rsData)#
# print(listA)

# 修改==============================================
# print(listA)
# listA[0] = "333.6"
# print(listA)

#删除===========================================
print(listA)
# del listA[0]
# del listA[1:3]
# listA.remove("abcd")#移除指定元素值
listA.pop(1)# 移除指定索引数据
print(listA)
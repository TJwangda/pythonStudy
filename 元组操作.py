# 元组不可变，
# 元组只有一个元素时要加逗号，否则解释权会当做整形处理

tupleA = ()
tupleA = ('abcd',89,9.12,'peter',[11,22,33])
# print(type(tupleA))
# print(tupleA)

# 查询==================================
# for item in tupleA:
#     print(item,end=" ")
#     pass

print(tupleA[2])
print(tupleA[2:4])

print(tupleA[::-1])
print(tupleA[::-2])
print(tupleA.count(9.12))# 统计出现次数
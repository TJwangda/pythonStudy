import re

# .匹配除换行符之外的字符============
# data = "a1aaa"
# partern = ".."
# res = re.match(partern,data)
# print(res.group())
# names = "李达","李明","小王","小李"
# pattern2 = "李."
# for name in names:
#     res = re.match(pattern2, name)
#     # print(name)
#     if res:
#         print(res.group())

# [] 匹配中括号中的任意字符================
str1 = "hello"
res = re.match("[he]",str1)
print(res.group())


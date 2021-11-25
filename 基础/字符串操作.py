Test = 'python'
#print(type(Test))
# print(Test[0])
# print(Test[1])
# for item in Test:
#     print(item,end=" ")

name = "petertom"
#print("姓名首字母大写：%s"%name.capitalize())

# 去除空格
# a = "    hello   "
# b = a.strip()
# print(b)
# name.lstrip()#删除左边空格
# name.rstrip()#删除右边空格
#print(id(name))# 查看内存地址

# 查找是否包含
# print(name.find("w"))
# print(name.index("p"))#不存在会报错
# print(name.startswith("p"))#以某子母开头
# print(name.endswith("p"))#以某子母结尾
#
# print(name.lower())# 转小写
# print(name.upper())# 转大写

strMsg = "helloo world"
# print(strMsg)
# print(strMsg[0])
print(strMsg[2:5])#左闭右开，从2到5
print(strMsg[2:])#左闭右开，从2到最后
print(strMsg[::-1])#倒序输出


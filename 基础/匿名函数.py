# lambada表达式创建
# 自带return
# 有且只有一个表达式
# lanbada 参数1，参数2，参数3：执行代码语句
# 通过变量调用

# test = lambda x,y:x+y;
# print(test(2,3))
# age = 19
# print("可以参军" if age>18 else "继续上学")

# rs = lambda x,y:x if x>y else y
# print(rs(2,12))
rs = (lambda x,y:x if x>y else y)(16,2)# 直接调用
print(rs)

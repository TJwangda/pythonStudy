# 必选参数、默认参数（缺省参数）、可选参数、关键词参数

# 必选参数======================================
# def sum(a,b):# a,b 形参
#     sum=a+b
#     print(sum)
#     pass
#
# sum(1,2)#1,2 实参

# 缺省参数,默认参数放最后===========================
# def sum1(a=20,b=30):
# def sum1(a,b=30):
#     print("默认参数使用=%d"%(a+b))
#     pass
# # sum1()
# sum1(1)

# 可变参数（参数个数不确定）===========================
# def getComputer(*args):
#     print(args)
#     pass
#
# getComputer((1,2,3,4,5,6))
# getComputer(1,2,3,4,5,6)

# 关键字可变参数=======================================
# 函数体内 字典类型，参数key值必须是字符串
# def keyFunc(**kwargs):
#     print(kwargs)
#     pass
#
# dictA = {"name":"wd","age":35}
# keyFunc(**dictA)
# keyFunc(name="peter",age=36);
# keyFunc()

# 参数组合使用  可选参数必须要放在关键字可选参数之前
def complexFulx(*args,**kwargs):
    print(args)
    print(kwargs)
    pass

complexFulx()
complexFulx(1,2,3,4)
complexFulx(1,2,3,4,name="wd")
complexFulx(age=36)
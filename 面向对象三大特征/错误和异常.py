"""
try:
    可能出错的代码
except: 指定捕获异常的类型
    出错后执行
else:
    没出错执行
finally:
    最后一定执行
"""

# try:
#     print(b)
# except NameError as e:
#     print("exception")
#     print(e)
#     pass
# except IndexError as e:
#     print(e)
#     pass
# except Exception as e:
#     print(e)
# else:
#     print("els")
#     pass
# finally:
#     print("finally")


# 自定义异常类
class TooLongMyException(Exception):
    def __init__(self,length):
        self.len = length
        pass

    def __str__(self):
        return "输入长度是"+str(self.len)+"超长了"
    pass

def name_test():
    name = input("请输入姓名：")
    try:
        if len(name) > 5:
            raise TooLongMyException(len(name))
        else:
            print(name)
            pass
    except TooLongMyException as re:
        print(re)
    pass

name_test()
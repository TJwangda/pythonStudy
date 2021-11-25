# 内置好的特定方法 一般为__xx__,例如：__index__,__str__

class Anmoial:

    def eat(self):
        pass

    def __init__(self):
        print("===init===")
        pass


    def __str__(self):
        return "tostring"

    def __new__(cls, *args, **kwargs):
        """经常用来做单例模式
        必须返回，否则对象无法创建"""
        print("====new实例化====")
        return object.__new__(cls)#真正创建对象实例
        pass
    pass

a = Anmoial()

print(a)
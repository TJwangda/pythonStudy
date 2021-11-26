
class Animal(object):
    def __init__(self):
        self.color = "red"
        pass

    # 在python中，如果不重写new方法，默认结构如下。不能用身的new方法
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args,**kwargs)
        # return object.__new__(cls,*args,**kwargs)
        # pass
    pass

tigger = Animal() # 实例化自动调用__new__创建实例，再调用__init__

# 单例模式

class DataBaseClass(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):#若不存在，再创建
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance
    pass

d1 = DataBaseClass()
d2 = DataBaseClass()
d3 = DataBaseClass()
print(id(d1))
print(id(d2))
print(id(d3))
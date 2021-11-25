# 前提
# 1。继承  发生在子类和父类之间
# 2。重写  子类重写父类方法

class Animal:
    """
    父类
    """
    def say_who(self):
        print("我是一个动物")
        pass
    pass

class Duck(Animal):
    """
    子类
    """
    def say_who(self):
        print("是鸭子")
        pass
    pass

def commonInvoke(obj):
    obj.say_who()

listObj = [Duck()]

for item in listObj:
    commonInvoke(item)
# duck1 = Duck()
# duck1.say_who()
# self 是对类对象的引用

class Person:
    """定义类"""
    def eat(self):
        """实例方法"""
        print(id(self))
        pass

    pass

p = Person()
print(id(p))
p.eat()
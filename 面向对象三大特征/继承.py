class Animal:
    def eat(self):
        pass
    def drink(self):
        pass
    pass

class Dog(Animal):# 继承animal父类
    def wwj(self):
        print("小狗汪汪")
        pass
    pass

class Cat(Animal):
    def mmj(self):
        print("小猫喵喵")
        pass
    pass

d1 = Dog()
d1.eat()
d1.wwj()
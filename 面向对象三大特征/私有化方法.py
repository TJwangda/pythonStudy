# 方法名前加两个下划线

class Animal:
    def eat(self):
        print("chile")
        self.__run()
        pass
    def __run(self):
        print("paole")
        pass
    pass

class Bird(Animal):
    pass

b = Bird()
# b.run()
b.eat()
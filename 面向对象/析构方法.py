# del()  对象销毁时自动调用

class Animal:
    def __init__(self,name):
        self.name = name
        print("构造初始化方法")
        pass

    def __del__(self):
        print("{}对象销毁，析构方法".format(self.name))
        pass
    pass

cat = Animal("猫")
# del cat
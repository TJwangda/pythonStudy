# 防止被篡改，可添加调用入口使用
# 语法：变量名前加两个下划线

class Person:
    def __init__(self):
        self.__name = "里斯" # 私有属性，外部无法访问
        self.age = 30
        pass
    def __str__(self):
        return "{}的年龄{}".format(self.__name,self.age)

    pass

class Student(Person):
    def printInfo(self):
        # print(self.__name)
        print(self.age)
    pass
stu = Student()
stu.printInfo()

# xl = Person()
# print(xl)
# print(xl.__name)

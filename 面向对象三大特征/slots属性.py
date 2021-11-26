# 只有在slots变量中的属性才会被添加，没在的会添加失败
# slots属性不会被继承，只在当前类生效
# 当子类声明__slots__时，继承父类的slots，子类slots范围是其自身的和父类的slots的并集

class Student:
    __slots__ = ("name","age")
    def __str__(self):
        return "{}---{}".format(self.name,self.age)
    pass

xw = Student()
xw.name = "xiaowang"
xw.age = 20
# xw.height = 188 # 添加失败
# print(xw.__dict__)# 所有可引用属性都存在这里。自由添加可造成性能问题
print(xw)
# 类属性 类对象所拥有，类对象和实例对象都可以访问
# 所有实例对象访问的是同一份类属性
# 实例对象无法修改类属性，只能使用。只能通过类对象修改
# 实例属性 只能实例对象访问
class Student:
    name="黎明" #类属性

    def __init__(self,age):
        self.age = age # 实例属性
        pass
    pass

lm = Student(18)
xh = Student(17)

print(lm.name)
print(lm.age)

print(xh.name)
print(xh.age)
print(Student.name)
# print(Student.age)

# 实现方式一  定义一个类属性 实现通过直接访问属性的形式去访问私有属性
# class Persion:
#     def __init__(self):
#         self.__age = 18 #定义私有属性
#         pass
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,age):
#         if age < 0:
#             print("age不能小于0")
#         else:
#             self.__age = age # 修改私有属性
#             pass
#     # 定义一个类属性 实现通过直接访问属性的形式去访问私有属性
#     age = property(get_age,set_age)
#     pass
# #
# p = Persion()
# print(p.age) # 调用get_age
# p.age = 25 # 调用set_age
# print(p.age)
# # p.set_age(13)
# # p.get_age()

# 实现方式二  通过装饰器声明
class Persion:
    def __init__(self):
        self.__age = 18 #定义私有属性
        pass

    @property #添加装饰器属性标识  提供一个get方法
    def age(self):
        return self.__age

    @age.setter # 使用装饰器修饰，提供一个set方法
    def age(self,params):
        if params < 0:
            print("age不能小于0")
        else:
            self.__age = params # 修改私有属性
            pass
    pass
#
p = Persion()
print(p.age) # 调用age @property
p.age = 25 # 调用age  @age.setter
print(p.age)
# p.set_age(13)
# p.get_age()
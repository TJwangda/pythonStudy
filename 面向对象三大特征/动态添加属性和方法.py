import types


# 动态添加实例方法
def dymicMethod(self):
    print("{}的体重是{},在{}上学".format(self.name,self.weight,Animal.school))
    pass
# 动态绑定类方法
@classmethod
def classTest(cls):
    print("这是一个类方法")
    pass

@staticmethod
def staticMethod():
    print("这是一个静态方法")
    pass

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return "{}年龄是{}".format(self.name,self.age)
        pass
    pass

Animal.classTest = classTest# 绑定类方法
Animal.classTest()

Animal.staticMethod = staticMethod #绑定静态方法
Animal.staticMethod()

z  = Animal("z",20)
z.weight = 80 # 动态添加实例属性
z.printInfo = types.MethodType(dymicMethod,z)# 动态绑定实例方法
print(z)

print(z.weight)
h = Animal("h",30)
# print(h.weight)

# 类对象添加属性=============
Animal.school = "北大"
# print(h.school)
z.printInfo()# 执行绑定的实例方法
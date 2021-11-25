# class People:
#
#     def __init__(self):
#         self.name = "小倩"
#         self.age = 20
#         self.sex = "女生"
#         pass
#
#     def eat(self):
#         '''
#         吃的实例方法
#         :return:
#         '''
#         print("喜欢吃榴莲")
#         pass
#     pass

# xq = People()
# xq.name = "小倩" # 添加实例属性
# xq.sex = "女生"
# xq.age = 20
# xq.eat()
# print(xq.name,xq.sex,xq.age)

# xl = People()
# xl.name = "小倩" # 添加实例属性
# xl.sex = "女生"
# xl.age = 20
#
# xm = People()
# print(xm.name)


class People:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        pass

    def eat(self,food):
        '''
        吃的实例方法
        :return:
        '''
        print("{}喜欢吃{}".format(self.name,food))
        pass
    pass


zp = People("韩媒","15","男士")
print(zp.name,zp.age)
zp.eat("香蕉")




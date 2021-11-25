# 类方法 第一个对象是cls 进而引用类属性和类方法
# 静态方法对参数无要求

class People:
    country = "中国"

    @classmethod
    def get_country(cls):
        """
        类方法用@classmethod修饰
        """
        return cls.country # 访问类属性
        pass

    @classmethod
    def change_country(cls,data):
        """
        修改类属性值，在类方法
        :param data:
        :return:
        """
        cls.country = data
        pass

    @staticmethod
    def getData():
        return People.country


    pass

# print(People.getData())
# p = People()
# print(p.getData())
# People.change_country("上海")
# print(p.get_country())
# print(People.get_country())

import time

class TimeTest:

    def __init__(self,hour,min,second):
        self.hour = hour
        self.min = min
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
        pass

    pass

print(TimeTest.showTime())
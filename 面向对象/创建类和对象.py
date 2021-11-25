
class Persion:

    # 类属性
    name = "wd"
    age = 23


    """
    实例方法，类内部定义
    第一个参数默认是self
    self可用其他值替换
    第一个参数必须是self占用
    """
    def eat(self):
        print("大口吃饭")
        pass

    def run(self):
        print("飞快的跑")
        pass

    """实例属性 方法内部 self点出来的"""
    def __init__(self):
        self.name = "小明"
        pass

    pass

"""普通方法"""
def normolDef():
    print("普通方法")
    pass


# 实例化
xiaoming = Persion();
xiaoming.run()
xiaoming.eat()
print("{}的年龄{}".format(xiaoming.name,xiaoming.age))
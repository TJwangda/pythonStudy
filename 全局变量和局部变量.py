
pro = "计算机"
name = "全局name"
def printInfo():
    name = "we"
    print(name)
    print(pro)
    pass

def test():
    print(name)

def changeGlobel():
    '''修改全局变量'''
    global pro # 声明要修改全局变量
    pro = "市场"
    pass

changeGlobel()
# test()
printInfo()
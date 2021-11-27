import sys
import psutil
import os
import gc

# 引用计数/标记清除（辅助）、分代回收
# 引用数量为0时清除
# sys.getrefcount(a) # 获取引用计数

# a = []
# print(sys.getrefcount(a))
# b = a
# print(sys.getrefcount(a))
# c = b
# d = b
# e = c
# f = e
# g = d
# print(sys.getrefcount(a))

def showMemSize(tag):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024/1024
    print("{} memory used:{}MB".format(tag,memory))
    pass

# 验证循环引用情况
def func():
    showMemSize("初始化")
    a = [i for i in range(100000)]
    b = [i for i in range(100000)]
    a.append(b)
    b.append(a)
    showMemSize("创建对象互相引用后")
    pass

func()
gc.collect()# 手动释放
showMemSize("函数执行完毕后")
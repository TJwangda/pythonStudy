# 必须满足一个结束条件
# 确定：容易导致栈溢出，严重可内存泄漏
# 求阶乘 n!=1×2×3×...×(n-1)×n

# 循环实现
# def jiecheng(n):
#     result = 1
#     for item in range(1,n+1):
#         result *= item
#         pass
#     return result

# print(jiecheng(5))

# def diguiJc(n):
#     if n == 1:
#         return 1
#     else:
#         return n*diguiJc(n-1)
#
# print(diguiJc(5))

# d递归模拟实现树形结构遍历
import os # 引入文件操作模块

def findFile(file_path):
    listRs =os.listdir(file_path)# 获取路径下所有文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_path,fileItem)#获取完整文件路径
        if os.path.isdir(full_path):#判读是否是文件夹
            findFile(full_path)# 如果是文件夹，继续递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass

findFile("/usr")
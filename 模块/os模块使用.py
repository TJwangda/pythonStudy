import os
import shutil

# os.rename("test.txt","test_重命名.txt")
# os.remove("./test_重命名.txt")
# os.mkdir("./testCreat")#创建文件夹，不能多级创建
# os.makedirs("/ss/ss/ss")# 可创建多级目录
# os.rmdir("testCreat")# 删除文件夹 不能级连删除
#删除非空目录，用shutil
# shutil.rmtree("/ss/ss")

# print(os.getcwd())# 当前目录
# 路径拼接
# os.path.join(os.getcwd(),"venv")
# print(os.path.join(os.getcwd(),"venv"))

# 目录列表
# listRs = os.listdir("/usr")
# for item in listRs:
#     print(item)
# rs = os.scandir("/usr")
# print(rs)
with os.scandir("/usr") as entires:
    for entry in entires:
        print(entry)

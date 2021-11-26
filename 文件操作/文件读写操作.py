
# 打开文件,不存在就创建
# 模式：w 创建，已存在会覆盖
# fobj = open("./test.txt","w",encoding="utf-8")
#
# # 读/写操作
# fobj.write("在苍茫的大海上")
# fobj.write("狂风卷集着乌云")
# fobj.close()

# 以二进制形式去写数据
# fobj = open("./test_1.txt","wb") # str-->bytes
# fobj.write("在乌云和大海之间".encode("utf-8"))
# fobj.close()

#模式 a 用于追加，不覆盖
# fobj = open("./test.txt","a") # str-->bytes
# fobj.write("在乌云和大海之间\r\n")
# fobj.write("海燕像黑色的闪电\r\n")
# fobj.close()

# 读取数据=======================================================
# f = open("test.txt","r")
# f = open("test.txt","rb")
# # print(f.read())# 读取所有数据
# # print(f.read(10)) # 读几个字符
# # print(f.read()) # 接替上次读取的光标位置
# # print(f.readline())# 读一行
# data = f.read()
#
# print(data.decode("utf-8"))
# f.close();


# with 上下午管理对象=======================================================
# 自动释放打开关联对象
with open("test.txt","r")as f:
    print(f.read())


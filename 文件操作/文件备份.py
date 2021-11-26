
# def copyFile():
#
#     #接受用户输入文件名
#     old_file = input("输入要备份的文件名：")
#     file_list = old_file.split(".")
#     # 构造新文件名
#     new_file = file_list[0]+"备份."+file_list[1]
#
#     old_f = open(old_file,"r")
#     new_f = open(new_file,"w")
#     content = old_f.read()
#     new_f.write(content)
#     old_f.close()
#     new_f.close()
#     pass

def copyFile():
    """大文件优化"""
    #接受用户输入文件名
    old_file = input("输入要备份的文件名：")
    file_list = old_file.split(".")
    # 构造新文件名
    new_file = file_list[0]+"备份."+file_list[1]

    try:
        with open(old_file,"r") as old_f,open(new_file,"w") as new_f:
            while True:
                content = old_f.read(1024)# 一次1024
                new_f.write(content)
                if len(content)<1024:
                    break
        pass
    except Exception as msg:
        print(msg)
        pass
    pass

copyFile()

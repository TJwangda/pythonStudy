# 返回指针当前位置

with open("test.txt","r") as f:
    print(f.read(3))
    print(f.tell())
    print(f.read(2))
    print(f.tell())
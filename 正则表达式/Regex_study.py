import re

# 语法 re.match(表达式，字符串，标志位[默认0])


str = "i like python in the world pei"
res = re.match("o",str,re.I|re.M)#只能从起始位置匹配匹配，什么开头
if res:
    print("success")
    print(res)
    print(res.group())
    pass
else:
    print("fail")
    # print(res)
    # print(res.group())
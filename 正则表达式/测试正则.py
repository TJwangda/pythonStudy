import re

str = "i like python in the world pei"
res = re.match("i",str)#只能从起始位置匹配匹配，什么开头
print(res.group())
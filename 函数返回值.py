# 函数返回值

# def sum(a,b):
#     sum=a+b
#     return sum
#
#
# su = sum(1,2)
# print(su)

def calComputer(num):
    li = []
    result = 0
    i = 1
    while i <= num:
        result+=i
        i+=1
        pass
    li.append(result)
    return li

value = calComputer(10)
print(type(value))
print(value)
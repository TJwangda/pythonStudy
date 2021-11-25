# 必须满足一个结束条件
# 确定：容易导致栈溢出，严重可内存泄漏
# 求阶乘 n!=1×2×3×...×(n-1)×n

# 循环实现
def jiecheng(n):
    result = 1
    for item in range(1,n+1):
        result *= item
        pass
    return result

# print(jiecheng(5))

def diguiJc(n):
    if n == 1:
        return 1
    else:
        return n*diguiJc(n-1)

print(diguiJc(5))
import sys
import argparse
# print("参数个数为：",len(sys.argv),"个参数")
# print("参数列表：",str(sys.argv[1:]))

# 创建一个解释器对象
parse = argparse.ArgumentParser(prog="mysql登陆",usage="%(prog)s [options] usage",description="my-编写自定义命令行文件",epilog="my-epliog")

# 添加必选参数
parse.add_argument("loginType",type=str,help="登陆系统类型")
# parse.add_argument("age",type=int,help="你的年龄")

# # 添加可选参数
# parse.add_argument("-s","--sex",action="append",type=str,help="你的性别")
# 限定范围
parse.add_argument("-u",dest="user",type=str,help="你的用户名")
parse.add_argument("-p",dest="pwd",type=str,help="你的密码")

# print(parse.print_help())

result = parse.parse_args()#开始解析参数
if (result.user == "root" and result.pwd == "123456"):
    print("登陆成功")
    pass
else:
    print("login fail")
print(result)
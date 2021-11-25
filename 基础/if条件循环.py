
#
# score = 60
# score = int(input('输入成绩：'))
# if score > 50:
#     print('及格')
# else:
#     print('不及格')
#     pass # 空语句，跳出循环

# if score > 80:
#     print('及格')
# elif score >50:
#     print('优秀')
# else:
#     print('不及格')
#     pass # 空语句，跳出循环
#
# print('结束')

import random # 直接导入产生随机数模块0


person = int(input('请出拳：[0石头,1剪刀,2布]'))
computer = random.randint(0,2)
print(computer)
if person == 0 and computer == 1:
    print('厉害，你赢了')
    pass
elif person == 1 and computer == 2:
    print('你赢了')
    pass
elif person == 2 and computer == 0:
    print('你赢了啊')
    pass
elif person == computer:
    print('平手')
    pass
else:
    print('你输了吧')
# print("小张的身高是%f"%(1.73))
# print("小张的体重是%f"%(160))
# print("小张的爱好是%s"%("计算机"))
# print("小张的专业是%s"%("机器学习"))
#
# # 再次输出小张信息
# print("小张的身高是%f"%(1.73))
# print("小张的体重是%f"%(160))
# print("小张的爱好是%s"%("计算机"))
# print("小张的专业是%s"%("机器学习"))

# def printInfo():
#     '''函数代码块'''
#     print("小张的身高是%f" % (1.73))
#     print("小张的体重是%f" % (160))
#     print("小张的爱好是%s" % ("计算机"))
#     print("小张的专业是%s" % ("机器学习"))
#     pass

def printInfo(name,height,weight,hobby,pro):
    '''函数代码块'''
    print("%s的身高是%f" % (name,height))
    print("%s的体重是%f" % (name,weight))
    print("%s的爱好是%s" % (name,hobby))
    print("%s的专业是%s" % (name,pro))
    pass

# 函数调用
printInfo("wd",188,120,"玩","计算机")
printInfo("范冰冰",160,120,"拍","电影")
# printInfo()
# printInfo()
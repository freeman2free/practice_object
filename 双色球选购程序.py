"""
需求：1.先让客户选购6个红球，再选购2个蓝球，最后统一打印用户选择的球号
     2.确保用户不能选择重复的，选择的数不能超出范围
"""
from time import sleep

print("welcome to my lottery")

# 准备两个空列表，存放所选的红球和蓝球
red_ball = []
count_red = 0
blue_ball = []
count_blue = 0

# 1.选购红球
while count_red < 6:
    user = input(f"请输入第{count_red + 1}个红球:")
    if user.isdigit():  # 如果输入为数字
        user = int(user)  # 将输入的转化为整型
        if 0 > user or user > 32:
            print("只能在1-32里选择")
            continue
        elif user in red_ball:
            print("不允许重复")
            continue
    else:
        print("请输入纯数字")  # 否则如果输入的不是纯数字，就回复错误信息并重新进入循环
        continue
    red_ball.append(user)
    count_red += 1
sleep(0.5)

# 2.选购蓝球
while count_blue < 2:
    user2 = input(f"请输入第{count_blue + 1}蓝球:")
    if user2.isdigit():  # 如果输入为数字
        user2 = int(user2)  # 将输入的转化为整型
        if user2 < 1 or user2 > 16:
            print("只能在1-16里选择")
            continue
        elif user2 in blue_ball:
            print("不允许重复")
            continue
    else:
        print("请输入纯数字")  # 否则如果输入的不是纯数字，回复错误信息并重新进入循环
        continue
    blue_ball.append(user2)
    count_blue += 1

# 3.展示所选号码
print(f"您所选的红球为:{red_ball}")
print(f"您所选的蓝球为:{blue_ball}")
input()

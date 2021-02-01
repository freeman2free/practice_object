# 提示用户猜一个数字，把 用户输入的数字A 与 一个程序随机生成的数字B 进行比较，
# 提示 数字A 大于/小于/等于 数字B。用户可以反复猜 数字B，直到猜中为止

# 增加功能2：程序在用户猜中答案后，输出猜中答案一共猜了多少轮（用户每输入一次计做一轮），并可以反复进行游戏（用户猜中一次后可选择“继续”还是“退出”）完成

# 增加功能3：统计游戏数据：玩家姓名、总游戏次数（玩家每猜中答案算玩了一次游戏）、总游戏轮数（玩家每猜一个数字算玩了一轮游戏）、最快猜中轮数，
# 并将结果保存在文件中（请大家本次任务都将数据写入 game_one_user.txt 中，以方便老师批改作业）

# 增加功能4: 通过 总游戏轮数/总游戏次数 算出一次游戏平均几轮猜中；实现
# 增加功能5: 通过对比已有最快猜中次数和本轮猜中次数，看本次成绩是否最好成绩，判断是否需要更新最好成绩。实现
# 增加功能6: 进入游戏时，从文件读取历史游戏记录，并将游戏数据赋值给一个字典 实现
# 增加功能7: 进入游戏时，输入玩家昵称，按玩家昵称读取之前的游戏数据。结束游戏后，根据玩家昵称，保存玩家的游戏数据到文本 实现

# 引入随机数模块
from random import *
import re

# 设置正则表达式，用于判断用户的输入
rule = re.compile(r"^[Yy]$")
rule2 = re.compile(r"^[Nn]$")

# 设置变量，分别用于记录总轮数
round_all = 0

# 总次数
count_all = 0

# 最快猜中轮数
min_round = 0

# 设置一个外层循环用于决定是否重新玩游戏
while True:
    # 用户输入自己的姓名，用于统计
    user_name = input("请输入您的姓名:")

    # 读取上次游戏保存的文件,并处理
    with open("game_one_user.txt", mode="r+") as record:
        # 使用readlines函数读取文件并将每一行换行符去掉，并再次将每一行分割成列表，再存入大列表中
        record_list = [i.strip().split() for i in record.readlines()]
        record_dict = {}
        # 循环遍历上述生成的列表，按照用户名为键，其余为值的方式存入字典内(值的数据类型为列表)
        for j in record_list:
            record_dict[j[0]] = j[1:]
    # 循环遍历生成的字典的key，如果存在该用户，那么将他的记录读出来并打印
    i = record_dict.get(user_name)
    while i:
        record_ave = float(record_dict[user_name][2]) / float(record_dict[user_name][0])
        print("""玩家%s,您已经玩了%s次,最快%s轮猜出答案,平均%.2f轮猜出答案,开始游戏!"""
              % (user_name, record_dict[user_name][0], record_dict[user_name][1],
                 record_ave))
        break
    # 如果不存在该键，则打印新用户
    else:
        print("新用户,开始游戏!")

    # 使用随机数模块，生成1-100间任意一个随机数
    num_randint = randint(1, 100)

    # 为了统计数据，可以引入一个变量，以方便统计用户玩了几轮（用户每输入一次就算一轮）
    round_times = 0
    # 为了统计数据，可以引入一个变量，以方便统计用户玩了几次（用户每猜中一次就算玩了一次）
    count_times = 0

    # 为了使用户可以反复猜数字，可以使用while循环
    while True:
        # 用户输入一个数字
        user_num = float(input("请输入一个数字"))
        # 用户每输入一次就算做一轮，累加并重新赋值变量
        round_times += 1
        # 将这两行数字进行对比,并产生不同的结果
        if user_num > num_randint:
            print("太大了")
        elif user_num < num_randint:
            print("太小了")
        elif user_num == num_randint:
            print("BINGO")
            count_times += 1
            # 显示玩家本次玩了几轮
            print(f"{user_name},您猜了{round_times}轮")
            break

    # 判断最快猜中的轮数，如果是第一次玩或者本次轮数小于最快轮数，便将本次轮数赋值给最快轮数变量，否则不变
    if count_all == 0 or round_times < min_round:
        min_round = round_times
    # 将本次的轮数累加到总轮数上
    round_all += round_times
    # 将本次游戏累加到总游戏次数上
    count_all += count_times
    # 平均多少轮猜中(总轮数除以总次数)
    round_ave = round_all / count_all
    print("%s,您已经玩了%d次,最快%d轮猜出答案,平均%.1f轮猜出答案" % (user_name, count_all, min_round, round_ave))

    # 判断是否退出
    quit_input = input("继续?y/n:")
    # 使用正则判断用户的输入
    if rule.findall(quit_input):
        continue
    elif rule2.findall(quit_input):
        # 输入q就退出该循环
        break
    else:
        print("输入错误,默认重新开始")

# 如果退出游戏将本次的统计结果保存在文件中
with open("game_one_user.txt", mode="w+", encoding="utf-8") as f:
    # 循环遍历游戏开始建立的字典的键，如果用户(该键)存在则修改该键的值
    for i in record_dict.keys():
        if user_name in i:
            record_dict[i] = [str(count_all), str(min_round), str(round_all)]
            # 之后将修改后的值按照用户名 总次数 最快轮数 总轮数(换行)写入文件内
            f.writelines([f"{user_name} {' '.join(record_dict[i])} \n"])
            break
    else:
        f.writelines([f"{user_name} {count_all} {min_round} {round_all} \n"])

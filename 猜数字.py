"""
高级猜数字

制作交互性强、容错率高的猜数字游戏程序。

要求：

    1.为猜数字游戏增加记录玩家成绩的功能，包括玩家用户名、玩的次数、平均猜中的轮数、最少猜中的轮数等； 完成
    2.如果记录里没有玩家输入的用户名，就新建一条记录，否则在原有记录上更新数据； 完成
    3.一局游戏结束后可选择继续进行新一局游戏（更新答案），或退出游戏 完成
    4.对玩家输入做检测，判定输入的有效性，并保证程序不会因异常输入而出错； 完成
    5.从网络上获取每一局的答案，请求地址：https://python666.cn/cls/number/guess/ 完成
    6.打开文件时，地址使用相对路径 完成
    (可选)如果记录文件不存在，就自动创建一个文件，避免程序报错跳出
"""

# 导入所需要的库
import requests
import re
import random
import os

# 设置正则表达式，用于判断用户的输入
rule = re.compile(r"^[Yy]$")
rule2 = re.compile(r"^[Nn]$")


def get_answer():
    # 通过网络接口获取答案
    try:
        answer = float(requests.get('https://python666.cn/cls/number/guess/').text)
    except TypeError:
        # 如果网络出现问题，那么就从随机数中生成一个答案
        answer = random.randint(1, 100)
    return answer


# 打开存放记录成绩的文件
def open_record_file():
    file_name = 'game_one_user.txt'
    # 判断该文件存不存在，如果存在则使用读取模式
    if os.path.exists(file_name):
        option = 'r'
    # 不存在则使用写入模式
    else:
        option = 'w+'
    with open(file_name, option) as r:
        record = r.readlines()
        re_dict = {}
        for i in record:
            row = i.split()
            # 以每行的第一位作为键，其余为值
            re_dict[row[0]] = row[1:]
        return re_dict


def match_username():
    while True:
        user_name = input('请输入你的名字(两位及以上中文字母数字下划线，开头不能是数字)：')
        if re.match(r'[\u4e00-\u9fa5a-zA-Z_]\w+', user_name):
            return user_name
        else:
            print('用户名格式有误，请重新输入')
            continue


# 写入纪录
def write_file(dict_data):
    with open('game_one_user.txt', 'w+') as f:
        for i in dict_data:
            # 将传入的数据转换数据类型
            dict_data[i] = [str(dict_data[i][0]), str(dict_data[i][1]), str(dict_data[i][2]), str(dict_data[i][3])]
            line = i + ' ' + ' '.join(dict_data.get(i)) + '\n'
            f.write(line)


def run_game(username):
    dict_record = open_record_file()  # 读取记录文件
    data = dict_record.get(username)  # 获取值

    if data:  # 如果data存在那么就读取
        times = int(data[0])  # 总次数
        total_rounds = int(data[1])  # 总轮数
        min_round = int(data[2])  # 最少的轮数
        avg_round = float(data[3])  # 平均几轮猜中
    else:  # 否则置为0
        times = 0
        min_round = 0
        total_rounds = 0
    if times == 0:
        avg_round = 0
    else:
        avg_round = total_rounds / times
    print('%s,你已经玩了%d次，总共玩了%d轮，最快%d轮猜出答案，平均%.2f轮猜出答案，开始游戏！' % (username, times, total_rounds, min_round, avg_round))
    while True:
        answer = get_answer()
        times += 1
        # 该变量用于记录一次游戏的轮数
        this_round = 0
        while True:
            total_rounds += 1
            this_round += 1
            # 对用户的输入进行排查防止出错，如果正确则开始游戏，否则重新输入
            try:
                user_input = float(input("请输入您所猜的数字(1-100):"))
            except Exception:
                print("输入有误，重新输入")
                continue
            if user_input > answer:
                print("太大了")
                continue
            elif user_input < answer:
                print("太小了")
                continue
            elif user_input == answer:
                print(f"Bingo!总共玩了{total_rounds}轮")
                break
        # 执行一个判断用于给最快轮数赋值
        if min_round == 0 or min_round >= total_rounds:
            min_round = total_rounds
        elif this_round < min_round:
            min_round = this_round
        print('%s,你已经玩了%d次，最快%d轮猜出答案，平均%.2f轮猜出答案' % (username, times, min_round, total_rounds / times))
        # 猜中后用于选择是否继续游戏
        choice = input("继续游戏？(y/n):")
        while True:
            if rule.findall(choice):
                print('继续游戏')
                break
            elif rule2.findall(choice):
                print('再见,欢迎下次来玩')
                dict_record[username] = [times, total_rounds, min_round, total_rounds / times]  # 新建一条记录
                return dict_record
            else:
                print("输入有误")
                continue
        continue


if __name__ == '__main__':
    # 获取用户名
    name = match_username()
    # 开始游戏
    data = run_game(name)
    # 写入记录
    write_file(data)

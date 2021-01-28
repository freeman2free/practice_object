# -*- coding: UTF-8 -*-

"""
【问题描述】

三人斗地主手牌规则：

一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。



要求：

将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。



可使用 list 和 random 完成。
"""
# 导入模块
import random
import time

card = []  # 准备空列表用于存放合成好的牌


def get_card():
    # 准备一副牌54张，有花色，有牌号
    ranks = ["♥", "♠", "♣", "♦"]  # 花色
    numbs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # 牌号
    global card

    # 双层循环，第一层循环花色，每个花色都有十三张牌，将十三张牌添加到card列表中
    for i in range(len(ranks)):  # 以花色列表的长度作为循环条件
        for j in range(len(numbs)):  # 以点数列表的长度作为循环条件
            card.append(ranks[i] + numbs[j])  # 每循环一次，往card列表中添加一种花色的13张牌(i此时为花色列表下标，通过该下标提取数据)
    # 往card列表中添加大小王，生成完整的一副牌
    card.append("BigJoke")
    card.append("SmallJoke")
    return card


def start():
    """
    分配给三个人，每个人17张牌
    底牌3张
    :return:
    """
    # 随机打乱（洗牌）,可多次调用
    random.shuffle(card)
    random.shuffle(card)

    # 未修改前
    # p1 = " ".join(card[0:17]).split()  # 将card列表中0-17号下标的元素，以每个字符串空格的格式合并成字符串，之后再将分割好的字符串合并成列表
    # p2 = " ".join(card[17:34]).split()
    # p3 = " ".join(card[34:51]).split()
    # last_card = " ".join(card[51:]).split()

    # print(f"玩家1: {p1}", end="\n")
    # print(f"玩家2: {p2}", end="\n")
    # print(f"玩家3: {p3}", end="\n")
    # print(f"底牌:  {last_card}")

    # 修改后
    global p1
    p1 = []  # 玩家1的列表
    p2 = []  # 玩家2的列表
    p3 = []  # 玩家3的列表
    cover_card = 3  # 底牌数
    for i in range(0, len(card) - cover_card):  # 循环条件为52次，减去3张底牌
        cardA = card[i]
        if i % 3 == 0:  # # 如果下标数，与3取余为0 给玩家1发牌，发的牌为card列表中的i下标元素
            p1.append(cardA)

        elif i % 3 == 1:  # 给玩家2发牌
            p2.append(cardA)

        else:  # 给玩家3发牌
            p3.append(cardA)

    print(f"玩家1:", len(p1), "张牌")
    for cardA in p1:
        print(' '.join(cardA))
        time.sleep(0.3)
    print(end="\n")

    print(f"玩家2:", len(p2), "张牌")
    for cardA in p2:
        print(' '.join(cardA))
        time.sleep(0.3)
    print(end="\n")

    print(f"玩家3:", len(p3), "张牌")
    for cardA in p3:
        print(' '.join(cardA))
        time.sleep(0.3)
    print(end="\n")

    rest_card = card[-3:]
    print(f"底牌:", " ".join(rest_card))


get_card()
start()
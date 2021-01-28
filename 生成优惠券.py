# 需求：设计并生成200个优惠券号码：
#     优惠码的字符由26个英文字符（大小写）组成
#     每个优惠码有8位

# 导入模块
import string
import random


def show_w():
    global lst_w2
    for i in range(1, 200):
        lst_w = list(string.ascii_letters)  # 使用string模块的全字母字符串 string.ascii_letters功能，并将其转换成列表
        random.shuffle(lst_w)  # 使用random模块的shuffle功能，将全字母字符串列表随机重新排列
        lst_w2 = []
        code = "".join(lst_w[0:8])  # 按照八位一组的顺序生成字符串
        if code not in lst_w2:  # 添加判断条件，如果该字符串不在lst_w2列表中，就把它添加进去，否则不添加
            lst_w2.append(code)
        print(format(lst_w2[0]))  # 用格式化字符串的方式，将前后引号去掉，再打印


show_w()  # 调用函数

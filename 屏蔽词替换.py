"""
需求：
给定一个屏蔽词列表的文件，文件中每一行都是一个词汇，可能是英文也可能是中文。

实现一个方法，输入一段文字，将其中存在于列表中的词汇字符替换成 *，返回处理后的文字。

验证这个方法时，从控制台输入待检测文字，调用方法处理，输出处理后的文字。
主要涉及内容：文件读取、字符串处理、函数调用
"""
import jieba


# 定义生成屏蔽词列表的功能函数
def block_list():
    # 读取屏蔽词列表文件
    with open("block_word.txt", "r") as f:
        global lst_block
        # 将读取出来的内容，先将换行符去掉后再存放到列表变量中
        lst_block = [word.strip() for word in f.readlines() if word]
        # 该行推导式效果等同于下方的代码
        # lst_block = []
        # lines = f.readlines()
        # for word in lines:
        #     if word:  # 如果word不为空，就去掉空行及换行符
        #         word = word.strip()
        #         lst_block.append(word)
        # print(lst_block)


# 定义屏蔽功能函数
def word_block(text, symbol="*"):
    # 遍历屏蔽词列表中的词,将text参数传入到该循环中,并用*代替
    # text参数表示输入的文本，将该字符串与屏蔽词列表匹配，将匹配到的屏蔽词列表中的词替换成*，再重新赋值给输入的文本
    for i in lst_block:
        text = text.replace(i, symbol * len(i))  # 替换的长度与屏蔽词列表的长度一样，即有多少替换多少,用symbol参数乘以字符串的长度
    return text


# 调用读取屏蔽词列表功能
block_list()
# 可以定义一个循环用于重复执行
while True:
    # 输入文本
    u_word = input("请输入您的文字: ")
    # 再加一个条件判断，用于检测用户输入，如果输入为空，则提示用户重新输入
    if not u_word:  # 如果输入为空则提示输入有误，并重新进入循环
        print("请重新输入")
        continue
    # 将输入的内容传入
    print(word_block(u_word))

# 现在，对于任一个英文的纯文本 txt 文件，请统计其中的单词总数
# 结果示例：
# There are 687 words in words.txt.
# 导入模块
import re
import os


def search():
    # 设定查找规则
    pattern = re.compile(r"[A-z]+")
    path = os.listdir(path="D:\\pythonwork\\小应用")

    while True:
        user_input = input("请输入您想查询的文件:")
        # 设置判断如果搜索的文件名在该目录下的话执行查找，否则告知文件不存在，并重新搜索
        if user_input in path:
            # 打开文件
            with open(f"{user_input}", encoding="utf-8") as f:
                result = pattern.findall(f.read())
                num_word = len(result)
                print(f"There are {num_word} words in {f.name}")
        else:
            print("你搜索的文件不存在")
        continue


search()

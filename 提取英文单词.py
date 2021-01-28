# -*-utf-8-*-
# from.txt 是一个混杂了英文单词和中文的文本文件。
# 要求：把 from.txt 里的文件复制到 to.txt 里，但只复制其中的英文单词，并按字母序排序。

# 导入模块
import re
# 设定正则表达式，匹配所有大小写英文字母组成的单词
pattern = re.compile(r"[A-Za-z]+")
with open("from.txt", "r+", encoding="utf-8") as f:
    # 用设定好的正则表达式查找文件里的字符串，返回列表一个结果
    result = pattern.findall(f.read())
    # 以升序给返回的列表结果排序
    result.sort()
    print(result)
# 以写入模式打开一个文件，将上述列表里的元素以每个元素之间换行的形式写入新文件
with open("to.txt", "w+", encoding="utf-8") as f2:
    f2.write("\n".join(result))

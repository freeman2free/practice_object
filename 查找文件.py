# -*- coding: utf-8 -*-
# 用 Python 做运维或写自动化脚本时，难免要和文件打交道
# 要求：输入关键字，列出指定文件夹中的所有文件名中含有此关键字的文件/目录，以及文件内容中含有此关键字的文件
# 提示：建议使用 os 模块的 listdir 方法获取指定目录下的所有文件

# 导入模块
import os

# 输入关键字，使用input
search_input = input("请输入您想要的文件名：")
# 输入要搜索的盘符
path_input = input("""请输入您想要搜索的盘(格式为: 盘符:\\文件夹名(选填)): 
""")
# 准备一个空列表用于添加搜索到的数据
search_list = []

# 使用os模块的listdir方法获取指定目录(你输入的目录)下的所有文件及文件夹,返回的是列表
file = os.listdir(path=f"{path_input}")
# 循环遍历指定的目录
for item in file:
    # 将名字重新组合格式为：盘符:\盘符下属文件及目录
    name_path = path_input + "\\" + item
    # 添加条件,如果用户输入的字符串与文件名匹配，则将该文件添加到上述列表中
    if search_input in item:
        search_list.append(item)
    # 否则,打开指定目录下的文件夹并对其进行循环遍历,如果匹配则将该文件添加到上述列表中,不匹配则捕获错误信息
    else:
        try:
            with open(name_path, "r+") as t:
                for line in t:
                    if search_input in line:
                        search_list.append(item)
                        break
        except Exception as e:
            print(e)
# 输出结果列表
print(search_list)
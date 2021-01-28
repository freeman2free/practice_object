"""
需求：
    读取 report.txt 文件中的成绩；
    统计每名学生总成绩、计算平均并从高到低重新排名；
    汇总每一科目的平均分和总平均分（见下表第一行）；
    添加名次，替换60分以下的成绩为“不及格”；
    将处理后的成绩另存为一个新文件（result.txt）。

"""

# 1.读取成绩
# 1.1 只读模式打开文件
with open("report.txt", "r", encoding="utf-8") as f:
    # 以readlines函数读取文件，并以行形式添加到列表中
    data = [i.split() for i in f.readlines()]
    # print(data)

# 设定表格头部
headers = data[0]
# 按照要求设定表格头部
headers.append("总分")
headers.append("平均分")
headers.insert(0, "名次")
# print(headers)

# 2.读取成绩 并计算每名学生的总成绩及平均分，并重新排序
data_2 = data[1:]  # 分数区域含姓名
# print(data_2)
# 将成绩提取出来
for i in data_2:
    sum = 0  # 总分
    avg = 0  # 平均分
    score = i[1:]   # 将成绩提取出来
    # 遍历提取出来的列表
    for j in score:
        sum += int(j)   # 算出每人的总分
        avg = '%.2f' % (sum/len(score))     # 算出每人的平均分
    i.append(str(sum))   # 将总成绩追加到列表中
    i.append(avg)   # 将平均分追加到列表中
    # print(i)

# 将该列表重新排序，按照每人的平均分从高到低排
data_2.sort(key=lambda x: x[-1], reverse=True)
# print(data_2)

# 3.计算科目的平均分
# 准备一个空列表
avg_list = ['总平均分']
for i in range(1, len(data_2[0])):
    avg_sum = 0
    for j in data_2:
        # 此为每门课的所有人相加的总分，
        avg_sum += float(j[i])
    # 保留2位小数，计算每门课的平均分，每门课的总分除以所有人
    avg_final = '%.2f' % (avg_sum / len(data_2))
    # 将计算出的结果添加到准备好的列表中
    avg_list.append(avg_final)
# 在data_2列表的下标0位置添加一行，即每门课的平均分和总平均分
data_2.insert(0, avg_list)

# 4.添加名次，替换60分以下为不及格
for i in data_2[0:]:
    # 此为，在每一行的下标0添加在data_2中该行的下标位置，并将其转成字符串，相当于添加名次
    i.insert(0, str(data_2.index(i)))
    # print(i)
    # 遍历所有的分数(不包含总分和平均分)，并添加判断条件，低于六十分的不及格
    for j in i[2:-2]:
        if float(j) < 60:
            i[i.index(j)] = "不及格"

# 再将先前定好的表格头部添加到data_2中
data_2.insert(0, headers)
# print(data_2)

# 5.将处理后的成绩另存为一个新文件（result.txt）
# 以写模式打开一个文件
with open("result.txt", mode="w+", encoding="utf-8") as f:
    # 遍历整理好的列表data_2
    for i in data_2:
        # 以每个元素之间有空格，加换行符合并成一个字符串
        result = " ".join(i) + "\n"
        # 将组合好的写入文件
        f.write(result)
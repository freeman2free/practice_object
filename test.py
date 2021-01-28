# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
# num = [1, 2, 3, 4]
#
# for i in num[0:]:
#     for j in num[0:]:
#         for k in num[0:]:
#             if i != j !=k and i != k:
#                 print(i, j, k)

"""
需求：
程序启动后，给用户提供查询接口，允许用户重复查股票行情信息;
允许用户通过模糊查询股票名，比如输入“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来;
允许按股票价格、涨跌幅、换手率这几列来筛选信息，比如输入“价格>50”则把价格大于50的股票都打印，输入“市盈率<50“，则把市盈率小于50的股票都打印，不用判断等于。
"""

# # 控制台输入三个数，输出三个数中的最大值
# i = 0
# num_list = []   # 准备一个空列表用于存储输入的数据
# while i < 3:
#     num = float(input("请输入数字:"))
#     num_list.append(num)
#     i += 1
#
# # 改进前的
# # if num_list[2] < num_list[0] > num_list[1]:
# #     print(str(num_list[0]).strip())
# # elif num_list[2] < num_list[1] > num_list[0]:
# #     print(str(num_list[1]).strip())
# # elif num_list[0] < num_list[2] > num_list[1]:
# #     print(str(num_list[2]).strip())
#
# # 改进后的
# print(f"最大值为:{max(num_list)}")
#
#
# # 需求：有一个全部由数字组成的列表 list_x，输出列表中的最大值
# list_num = [2, 5, 1.1, 3.5, 6, 12]
# # 设置最大值为列表下标为0的数
# max_num = list_num[0]
#
# # 循环遍历该列表
# for x in list_num:
#     # 设定条件，如果当前数大于max_num的值就将它重新赋值为当前数
#     if x > max_num:
#         max_num = x
#
# # 输出最大值
# print(max_num)

# 需求：控制台输入一个数字，判断是否为素数
# 素数：一个大于1的自然数，除了1和它本身外，不能被其他自然数整除。换句话说就是该数除了1和它本身以外不再有其他的因数。

# # 用户输入一个数字
# num = int(input("请输入数字："))
#
# # 这个数必须大于1
# if num > 1:
#     # 设置循环条件:循环遍历2至输入的数之间，查看有没有(除本身以及1以外)的因子，如果有则不是质数
#     for i in range(2, num):
#         if num % i == 0:
#             print("不是质数")
#             break
#     else:
#         print("是质数")
#
# else:
#     print("必须大于1")
#


# 要求：依次输入每门课程的分数与学分，最终得到平均绩点
# 计算公式:(课程学分1*绩点 + 课程学分2*绩点 + ... + 课程学分n*绩点) / (课程学分1 + 课程学分2 + ... + 课程学分n)

# 创建三个变量分别用于存储不同的数据

result_all = 0  # 除数，(课程学分*绩点)再相加
score_all = 0  # 被除数，课程学分总数
gpa_all = 0  # 平均绩点,用于存储平均绩点累加的数据


# 设置循环，用于重复累加
# while True:
#     record = float(input("请输入科目1的成绩:"))
#     score = float(input("请输入科目1的学分:"))
#     credit = 0  # 绩点初始属性
#
#     # 通过输入的成绩判断绩点，并给绩点赋值
#     if 90 <= record <= 100:
#         credit = 4
#     elif 85 <= record <= 89:
#         credit = 3.7
#     elif 82 <= record <= 84:
#         credit = 3.3
#     elif 78 <= record <= 81:
#         credit = 3
#     elif 75 <= record <= 77:
#         credit = 2.7
#     elif 71 <= record <= 74:
#         credit = 2.3
#     elif 66 <= record <= 70:
#         credit = 2
#     elif 62 <= record <= 65:
#         credit = 1.7
#     elif 60 <= record <= 61:
#         credit = 1.3
#     elif record < 60:
#         credit = 0
#
#     score_all += score
#     # 再优化一下,无需再多设置一个变量
#     # result = (score * credit)
#     result_all += score * credit
#     gpa = result_all / score_all
#     # 给循环体外的变量赋值，用于存储，以便最后的输出
#     gpa_all = gpa
#     print("现在平均绩点为: %.2f" % gpa_all)

# 要求：运用面向对象的知识，构造一个类来描述每个国家的奖牌情况。
# 类的属性包括：国家名、金/银/铜牌数量
# 再提供方法：新增奖牌、输出奖牌榜信息、获取奖牌总数等

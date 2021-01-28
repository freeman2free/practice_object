# 需求：
# 输入：身高、体重值
# 输出：BMI 指数、是否正常
# 是用体重公斤数除以身高米数平方得出的数字
#  BMI < 18.5 体重偏轻
#
#     18.5 <= BMI < 24 体重正常
#
#      BMI >= 24 体重偏重

# 定义装饰器
def decorator(func):
    def inner(a, b):
        print("""BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），
        是用体重公斤数除以身高米数平方得出的数字
        看看自己体重是否正常吧""")
        input("回车继续")
        print()
        func(a, b)

    return inner


# 设计计算功能
@decorator
def BMI(w, h):
    result = w / h * h
    if result < 18.5:
        print("体重偏轻")
    elif 18.5 <= result < 24:
        print("体重正常")
    elif result >= 24:
        print("体重偏重")


while True:
    # 输入体重
    weight = float(input("请输入您的体重:"))
    # 输入身高
    height = float(input("请输入您的身高:"))

    BMI(weight, height)
    end = input("退出?(q):")
    if end == "q":
        break

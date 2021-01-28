menu = {
    '北京': {'海淀': {'五道口': {'soho': {}, '网易': {}, 'google': {}}, '中关村': {'爱奇艺': {}, '汽车之家': {}, 'youku': {}, },
                  '上地': {'百度': {}, }, }, '昌平': {'沙河': {'老男孩': {}, '北航': {}, }, '天通苑': {}, '回龙观': {}, }, '朝阳': {},
           '东城': {}, },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

menu_list = []
while True:
    for i in menu:
        print(i)  # 打印菜单内容，所有的键：北京 上海 山东
    choice = input("选择进入:(退出:q 返回上一层:t)").strip()  # 可选择进入下一级菜单，strip() 方法用于移除字符串头尾指定的字符，防止误输入

    if choice in menu:  # 如果输入的内容在menu里
        menu_list.append(menu)  # 将该键的值追加到menu_list列表中
        menu = menu[choice]  # 更新菜单 进入下一层(该键的值)

    elif choice == "t":  # 如果输入的是t
        if menu_list:
            menu = menu_list.pop()  # .pop用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

    elif choice == "q":
        exit("退出")

    else:
        print("输入有误")  # # 判断用户如果输入的字符非q/t以及键，便重新进入循环
        continue

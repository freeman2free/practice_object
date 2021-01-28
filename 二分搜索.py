"""
二分搜索（binary search）：
在有序数组（arr）中，指定区间[left right]范围内，查找元素x
如果该元素不存在，则返回-1
"""


def binarysearch(arr, left, right, x):
    while left <= right:

        # 求中点公式，这样写不容易溢出 如果写成(left+right)/2更容易溢出，所以改成这样
        mid = int((left + (right - left) / 2))

        # 检查x是否在mid下标处
        if arr[mid] == x:  #
            print("发现%d在下标%d处" % (x, mid))
            return mid

        # 如果x大于中点，那么就不可能出现在左半部分，只需要再比较右半部分的元素
        elif arr[mid] < x:
            left = mid + 1
            print("调整搜索区间为[%d, %d]" % (mid + 1, right))

        # 如果x小于中点，那么就不可能出现在右半部分，只需要再比较左半部分的元素
        elif arr[mid] > x:
            right = mid - 1
            print("调整搜索区间为[%d, %d]" % (left, mid - 1))

    # 如果循环完毕仍未找见x的话，说明不在该数组内，返回
    return print(f"未在该组中找到{x}")  # 或return -1


# 参数arr填数组列表（必须为有序的），left和right填下标，x填想要查找到的元素
binarysearch([1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107], 0, 18, 22)


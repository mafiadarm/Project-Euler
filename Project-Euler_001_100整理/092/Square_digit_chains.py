#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
平方数字链
将一个数的所有数字的平方相加得到一个新的数，不断重复直到新的数已经出现过为止，这构成了一条数字链。
例如，
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
可见，任何一个到达1或89的数字链都会陷入无尽的循环。更令人惊奇的是，从任意数开始，最终都会到达1或89。
有多少个小于一千万的数最终会到达89？
"""
def get_sum(x):
    number_list = []
    while x:
        x, temp = divmod(x, 10)
        number_list.append(temp)
    return sum([t * t for t in number_list])

def xxx():
    """
    10000000以下平方和最大的数是9999999，其平方和为81*7=567。所以，可以先建立一个600以下的字典，
    其他数在运行过程中一旦碰到字典中的数，马上将1或89作为结果反馈。这样，可以加速运算过程。
    :return:
    """
    dict_600 = {}
    for x in range(1, 600):
        d = x
        while x != 1 and x != 89:
            x = get_sum(x)
        dict_600[d] = x

    count = 0
    for num in range(1, 10**7):
        ss = get_sum(num)
        if dict_600[ss] == 89:
            count += 1

    return count

print(xxx())
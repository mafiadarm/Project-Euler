#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
最小倍数
2520是最小的能够被1到10整除的数。

最小的能够被1到20整除的正数是多少？


"""

def lcm(x, y):  # 最小公倍数 详见 005
    """
        求最小公倍数就是把两个数的最大公约数找出来，分别除开，然后再把结果和公约数相乘
    """
    a, b = x, y
    while y:
        x, y = y, x % y

    result = a / x * b / x * x
    return result

def common_multiple(scope):
    li = list(range(scope+1))[1:]
    while len(li) > 1:  # 挨个求出两个数的最小公倍数
        a = li.pop()
        b = li.pop()
        li.append(lcm(a, b))

    print(li[0])

if __name__ == '__main__':
    common_multiple(20)
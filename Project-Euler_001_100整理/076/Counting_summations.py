#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
加和计数
将5写成整数的和有6种不同的方式：
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
将100写成整数的和有多少种不同的方式？
有多少总方式100=1+99、100=2+98、100=1+1+98......
"""

def divide_count(num, dig, tmp_dict):  # num写成+dig的所有方式 见076
    if num == dig or dig == 1:
        return 1
    elif dig > num:
        return 0
    else:
        if tmp_dict.get(str(num) + ',' + str(dig)) is None:
            tmp = divide_count(num - 1, dig - 1, tmp_dict) + divide_count(num - dig, dig, tmp_dict)  # 递归
            tmp_dict[str(num) + ',' + str(dig)] = tmp
            return tmp
        else:
            return tmp_dict.get(str(num) + ',' + str(dig))

def xxx(num=100):
    tmp_dict = {}
    count = 0
    for m in range(2, num + 1):
        count += divide_count(num, m, tmp_dict)
    return count
    
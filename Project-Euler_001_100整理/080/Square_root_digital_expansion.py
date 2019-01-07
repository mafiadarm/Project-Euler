#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
平方根数字展开
众所周知，如果一个自然数的平方根不是整数，那么就一定是无理数。这样的平方根的小数部分是无限不循环的。
2的平方根为1.41421356237309504880…，它的小数点后一百位数字的和是475。
对于前一百个自然数，求所有无理数平方根小数点后一百位数字的总和。

这里用到decimal库，计算高精度小数
"""
import decimal
decimal.getcontext().prec = 102

def xxx():
    sum_count = 0
    square_list = [x ** 2 for x in range(1, 11)]

    for i in range(1, 100):  # 前100个自然数0-99
        if i in square_list: continue  # 排除平方数
        r = decimal.Decimal(i).sqrt()  # 带精度的开方
        d = str(r)[2:102]  # 小数点后就从第3个字符串开始计算，如果要加整数部分则需要 + str(r)[0]
        d = "+".join(d)
        sum_count += eval(d)

    return sum_count

print(xxx())
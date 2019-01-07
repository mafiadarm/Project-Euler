#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
最大回文乘积
回文数就是从前往后和从后往前读都一样的数。由两个2位数相乘得到的最大回文乘积是 9009 = 91 × 99。

找出由两个3位数相乘得到的最大回文乘积

两个最大三位数相乘=999*999，所以先找出998001以内所有的回文数
最小的两个三位数相乘=100*100，所以回文数要大于10000
从大的开始检查是否有三位数的因子，从999开始，如果被整除则为最大
"""

def palindromic():
    ask = 998002
    mut_min = 10000
    ss = [i for i in range(ask) if str(i) == str(i)[::-1] and i > mut_min]

    for check in ss[::-1]:
        for test in range(100, 1000):
            if check % test == 0 and check/test<1000:
                return check


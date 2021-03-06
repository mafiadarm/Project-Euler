#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
有序分数
考虑形如n/d的分数，其中n和d均为正整数。如果n < d且其最大公约数为1，则该分数称为最简真分数。
如果我们将d ≤ 8的最简真分数构成的集合按大小升序列出，我们得到：
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
可以看出2/5是3/7直接左邻的分数。
将所有d ≤ 1,000,000的最简真分数按大小升序排列，求此时3/7直接左邻的分数的分子。

分析：
分母小于等于100W，无限接近 3/7 的真分数的分子[小于3/7]
分子和分母 互质
猜测 范围固定在 40w/100w < x < 50w/100w 所以就10w个数字
从大到小的递减
分子分母增加或者减少1 并且检测是否是互质[最大公约数为1]，低于3/7的加入列表
比较最大数
"""

from math import gcd

def xxx(num=10 ** 6):
    x = d = num
    f = {}
    while d > 0:
        while x / d >= 3 / 7:
            x -= 1

        while x / d < 3 / 7:
            if gcd(x, d) == 1:
                f[x, d] = x / d
            d -= 1
            if not d:
                break
    return max(f, key=f.get)[0]

print(xxx())
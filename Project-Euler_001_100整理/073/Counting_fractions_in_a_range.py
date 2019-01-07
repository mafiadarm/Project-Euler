#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
分数有范围计数
考虑形如n/d的分数，其中n和d均为正整数。如果n < d且其最大公约数为1，则该分数称为最简真分数。
如果我们将d ≤ 8的最简真分数构成的集合按大小升序列出，我们得到：
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
可以看出在1/3和1/2之间有3个分数。
将d ≤ 12,000的最简真分数构成的集合排序后，在1/3和1/2之间有多少个分数？
"""
from math import gcd

def xxx(max_range=12000):
    f = {}
    for i in range(1, max_range):
        for j in range(i + 1, max_range):
            if 1 / 3 < i / j < 1 / 2 and gcd(i, j) == 1:
                f[i, j] = i / j
    return len(f)

def other():
    # 更科学的方法
    count = {}  # 削去重复项
    for i in range(3, 12001):
        for j in range(int(i / 3), int(i / 2 + 1)):  # 把范围缩小,而且过滤了非互质数
            if 1 / 2 > j / i > 1 / 3:
                count[(j / i)] = j / i

    return len(count)

print(other())
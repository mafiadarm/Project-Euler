#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
不同的质因数
首次出现连续两个数均有两个不同的质因数是在：
14 = 2 × 7
15 = 3 × 5
首次出现连续三个数均有三个不同的质因数是在：
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
首次出现连续四个数均有四个不同的质因数时，其中的第一个数是多少？

分析：
找出第一个数，这个有4个不同的质因数
遍历每一个数，分析它的质因数，一旦有4个，放入列表，当连续有4个时，即为结果
"""

from itertools import count

def prime_factor(n):  # 列出所有质因子，如果传1进去，列表会是空值
    result_set, f = set(), 2
    while f * f <= n:
        while not n % f:
            result_set.add(f)
            n //= f
        f += 1
    if n != 1:
        result_set.add(n)
    return result_set

flag = 0  # 连续性标记
container = []  #
for i in count(1):
    if len(prime_factor(i)) == 4:  # 有4个质因子
        container.append(i)  # 则放到列表
        flag += 1
        if flag == 4:  # 代表列表里面有4个连续的数了
            break
    else:  # 如果没有连续，则归零
        flag = 0
        container.clear()

print(container)
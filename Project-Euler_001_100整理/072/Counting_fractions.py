#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
分数计数
考虑形如n/d的分数，其中n和d均为正整数。如果n < d且其最大公约数为1，则该分数称为最简真分数。
如果我们将d ≤ 8的最简真分数构成的集合按大小升序列出，我们得到：
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
可以看出该集合中共有21个元素。
d ≤ 1,000,000的最简真分数构成的集合中共有多少个元素？

分析：
其实本题是求 1~100W 每个数的互质数的个数的和
"""

def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def xxx(num=10 ** 6):  # 欧拉公式来标记列表
    p_list = prime_list(num)  # 建立num以内的素数列表
    h_list = [0] * (num + 1)  # 建立一个有num+1个0的列表

    for i in p_list:  # 先处理所有素数
        h_list[i] = i - 1  # 素数的互质数为[素数-1]

    for index, value in enumerate(p_list):  # 用素数来处理倍数[一层一层的覆盖]

        for n in range(value * value, num + 1, value):  # 处理素数的倍数
            h_list[n] = h_list[int(n / value)] * (value - 1)

        for m in range(value * value, num + 1, value * value):  # 处理素数倍数的倍数
            h_list[m] = h_list[int(m / value)] * value

    return sum(h_list)

print(xxx())
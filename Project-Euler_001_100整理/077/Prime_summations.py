#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
素数加和
将10写成素数的和有5种不同的方式：
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2
写成素数的和有超过五千种不同的方式的数最小是多少？
"""
def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def xxx(num=100, min_range=5000):
    primes = [True] * num
    prime = prime_list(num)
    P = len(prime)

    # R = [[0] * P] * num  # 等价，但是结果不同
    R = []
    for i in range(100):
        R.append([0] * P)

    for k in range(P):
        R[0][k] = 1
    for n in range(0, num, 2):
        R[n][0] = 1
    for n in range(2, num):
        for k in range(1, P):
            R[n][k] = R[n][k - 1]
            if prime[k] <= n:
                R[n][k] += R[n - prime[k]][k]
        if R[n][-1] >= min_range and not primes[n] or R[n][-1] >= min_range + 1:
            return n
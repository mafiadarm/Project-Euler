#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
素数幂三元组
最小的可以表示为一个素数的平方，加上一个素数的立方，再加上一个素数的四次方的数是28。实际上，在小于50的数中，一共有4个数满足这一性质：
28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4
有多少个小于五千万的数，可以表示为一个素数的平方，加上一个素数的立方，再加上一个素数的四次方？
"""

def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def xxx():
    ask = 50000000
    # 2\3\4次幂的上限
    log2 = int(ask ** (1 / 2)) + 1
    log3 = int(ask ** (1 / 3)) + 1
    log4 = int(ask ** (1 / 4)) + 1
    # 各边界内的值
    n2 = [i ** 2 for i in prime_list(log2)]
    n3 = [i ** 3 for i in prime_list(log3)]
    n4 = [i ** 4 for i in prime_list(log4)]
    # 把组合放到集合
    count = set()
    for two in n2:
        for three in n3:
            for four in n4:
                if two + three + four < ask:
                    count.add(two + three + four)
                else:
                    break
    return len(count)

print(xxx())
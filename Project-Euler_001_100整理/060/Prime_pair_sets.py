#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
素数对的集合
3、7、109和673是非常特别的一组素数。任取其中的两个并且以任意顺序连接起来，其结果仍然是个素数。例如，选择7和109，我们得到
7109和1097均为素数。这四个素数的和是792，这是满足这个性质的一组四个素数的最小和。
若有一组五个素数，任取其中的两个并且以任意顺序连接起来，其结果仍然是个素数，求这样一组素数的最小和。
"""
from itertools import combinations  # 不重复的组合

def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def is_prime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def xxx():
    lis = prime_list(10000)  # 给定一个上限，再多也没意义了
    ll = []
    for i in combinations(lis, 5):
        flag = True
        for o in combinations(i, 2):
            num1 = int(str(o[0]) + str(o[1]))
            num2 = int(str(o[1]) + str(o[0]))
            if not is_prime2(num1) or not is_prime2(num2):
                flag = False
                break
        if flag:
            ll.append(sum(i))
    return min(ll)
    
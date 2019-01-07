#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
全数字的素数
如果一个n位数恰好使用了1至n每个数字各一次，我们就称其为全数字的。例如，2143就是一个4位全数字数，同时它恰好也是一个素数。
最大的全数字的素数是多少？

分析：
猜想小于10**9-1以内的素数，条件是各个数字只用了一次，所以只能用排列组合
以位数递减，找到最大的即可
"""
from itertools import permutations

def is_prime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def result():
    for decimal in range(9, 0, -1):
        digit = "123456789"[:decimal]
        for test in permutations(digit[-1::-1]):  # 翻转切片，排列从最大开始
            answer = int("".join(test))
            if is_prime2(answer):
                return answer  # 只要成立就是结果

print(result())
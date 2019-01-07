#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
素数的和
所有小于10的素数的和是2 + 3 + 5 + 7 = 17。

求所有小于两百万的素数的和
"""

def is_prime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

ask = 2000000
su = 0
for test in range(ask):  # 也是用遍历了
    if is_prime2(test):
        su += test

print(su)
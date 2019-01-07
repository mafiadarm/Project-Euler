#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
二次“素数生成”多项式

欧拉发现了这个著名的二次多项式：

n² + n + 41

对于连续的整数n从0到39，这个二次多项式生成了40个素数。然而，当n = 40时，40² + 40 + 41 = 40(40 + 1) + 41能够被41整除，同时显然当n = 41时，41² + 41 + 41也能被41整除。

随后，另一个神奇的多项式n² − 79n + 1601被发现了，对于连续的整数n从0到79，它生成了80个素数。这个多项式的系数-79和1601的乘积为-126479。

考虑以下形式的二次多项式：

    n² + an + b, 满足|a| < 1000且|b| < 1000

    其中|n|指n的模或绝对值
    例如|11| = 11以及|−4| = 4

这其中存在某个二次多项式能够对从0开始尽可能多的连续整数n都生成素数，求其系数a和b的乘积。
"""

def is_prime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for t in range(2, int(n ** 0.5) + 1):
            if n % t == 0:
                return False
        return True

result_a, result_b, count = 0, 0, 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):  # 设定范围
        u, c = 0, 0  # 递变量，计数器
        test = u ** 2 + a * u + b  # 公式
        if test < 0:
            continue

        while is_prime2(test):
            c += 1
            u += 1
            test = u ** 2 + a * u + b  # 公式变化
            if test < 0:
                break

        if count < c:
            count = c
            result_a = a
            result_b = b

print(result_a, result_b, count, "****", result_a*result_b)



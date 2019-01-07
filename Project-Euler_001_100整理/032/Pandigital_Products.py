#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
全数字的乘积

如果一个n位数包含了1至n的所有数字恰好一次，我们称它为全数字的；例如，五位数15234就是1至5全数字的。

7254是一个特殊的乘积，因为在等式39 × 186 = 7254中，被乘数、乘数和乘积恰好是1至9全数字的。

找出所有被乘数、乘数和乘积恰好是1至9全数字的乘法等式，并求出这些等式中乘积的和。

注意：有些乘积可能从多个乘法等式中得到，但在求和的时候只计算一次
"""

# 同时满足1~9个数字,位数上限只能是5位数9*9999 99*999上限都是5位数
count = set()
container = []
target = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(1, 100):
    for j in range(100, 10000):
        digit = str(i) + str(j) + str(i*j)
        nine_bit = len(digit)  # 统计数字数量
        nine_series = sorted(digit)  # 统计数字内容
        if nine_bit == 9 and nine_series == target:
            container.append(f"{i}x{j}={i*j}")
            count.add(i * j)

print(sum(count))
print(container)
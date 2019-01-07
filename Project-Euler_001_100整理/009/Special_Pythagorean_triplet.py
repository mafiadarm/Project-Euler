#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
特殊毕达哥拉斯三元组
毕达哥拉斯三元组是三个自然数a < b < c组成的集合，并满足

a² + b² = c²
例如，3² + 4² = 9 + 16 = 25 = 5²。

有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc。

枚举就行了
"""

ask = 1000
for a in range(1, ask):
    for b in range(a + 1, ask):
        c = ask - a - b
        if a * a + b * b == c * c:
            print(a, b, c, a * b * c)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
阶乘数字和
n! 的意思是 n × (n − 1) × … × 3 × 2 × 1

例如，10! = 10 × 9 × … × 3 × 2 × 1 = 3628800，所以10!的各位数字和是 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27。

求出100!的各位数字和。
"""

ask = 100
import math
from functools import reduce

fac_100 = math.factorial(ask)

result = 0
while fac_100 != 0:
    result += fac_100 // 10
    fac_100 = fac_100 % 10


# 或者直接用
reduce(lambda a, b: a + b, [int(i) for i in str(math.factorial(ask))])
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
各位数字的阶乘

145是个有趣的数，因为1! + 4! + 5! = 1 + 24 + 120 = 145。

找出所有各位数字的阶乘和等于其本身的数，并求它们的和。

注意：因为1! = 1和2! = 2不是和的形式，所以它们并不在讨论范围内。
"""

# 因为8*9!<8位，所以范围定在7*9!以内,遍历此范围内所有数，比较"阶乘和"与此数
from math import factorial

ask = 1000000
result = 0
for digit in range(3, ask):
    count = 0
    for i in str(digit):
        count += factorial(int(i))

    if count == digit:
        result += digit
        print(digit)

print(result)

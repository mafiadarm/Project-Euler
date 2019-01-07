#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
幂的数字和
2**15 = 32768，而32768的各位数字之和是 3 + 2 + 7 + 6 + 8 = 26。

2**1000的各位数字之和是多少？
"""

ask = 2 ** 1000

# 用循环来做，不给内存增加负担
result = 0
while ask != 0:
    result += ask%10
    ask = ask//10

# 或者直接用转换计算
sum([int(i) for i in str(ask)])
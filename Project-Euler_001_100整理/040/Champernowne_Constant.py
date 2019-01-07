#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
钱珀瑙恩常数
将所有正整数连接起来构造的一个十进制无理数如下所示：
0.123456789101112131415161718192021…
可以看出小数点后第12位数字是1。
如果dn表示上述无理数小数点后的第n位数字，求下式的值：
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

分析：
构造一个1000000位的数，然后通过索引直接拿
"""
from itertools import count

ask = 1000000

# 构造这个数
str_num = ""
for i in count(1):
    str_num += str(i)
    if len(str_num) > ask:
        break

# 取索引
result = int(str_num[0])
for j in range(1, 7):
    result *= int(str_num[10 ** j - 1])

print(result)

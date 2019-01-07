#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自幂
十项的自幂级数求和为 1¹ + 2² + 3³ + … + 10[10次方] = 10405071317。
求如下一千项的自幂级数求和的最后10位数字：1¹ + 2² + 3³ + … + 1000[1000次方]。

return str(sum([i**i for i in range(1, 1001)]))[-10::]
"""


n = 1
for i in range(2, 1001):
    n += i ** i
print(str(n)[-10::])
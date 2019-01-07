#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数长方形
如果数得足够仔细，能看出在一个3乘2的长方形网格中包含有18个不同大小的长方形，如下图所示：
尽管没有一个长方形网格中包含有恰好两百万个长方形，但有许多长方形网格中包含的长方形数目接近两百万，求其中最接近这一数目的
长方形网格的面积。

以1为单位，划分网格，长=3个格子，宽=2个格子  所以就是（3+2+1）*（2+1）= 6 * 3 = 18
三角形公式 （1+3）* 3 / 2 = 6   （1+2）* 2 * 2 = 3
(（1 + large）* large / 2） * (( 1 + wide) * wide / 2) < 200W

【先求范围】确定范围 wide, large = 100, 100 上面公式会达到25502500，所以可以把遍历范围放到100以内
"""


def xxx(n=2000000):
    max_range, value = 1, 0
    while value < n:
        max_range *= 10
        value = ((1 + max_range) * max_range / 2) ** 2

    x, y, z = 0, 0, n
    for large in range(1, max_range):
        for wide in range(large, max_range):
            total = ((1 + large) * large / 2) * ((1 + wide) * wide / 2)
            if z > abs(n - total):
                x, y, z = large, wide, abs(n - total)
            if total > n:
                break
    return x, y, z, x*y

print(xxx())
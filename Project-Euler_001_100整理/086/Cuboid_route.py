#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
长方体路径
蜘蛛S位于一个6乘5乘3大小的长方体屋子的一角，而苍蝇F则恰好位于其对角。沿着屋子的表面，从S到F的最短“直线”距离是10，路径如下图所示：
然而，对于任意长方体，“最短”路径实际上一共有三种可能；而且，最短路径的长度也并不一定为整数。
当M=100时，若不考虑旋转，所有长、宽、高均不超过M且为整数的长方体中，对角的最短距离是整数的恰好有2060个；这是使得该数目超过两千的最小M值；当M=99时，该数目为1975。
找出使得该数目超过一百万的最小M值。

分析：
把长方体想想成一个纸盒子，把盒子打开，这条线就是对角线，就是求直角三角形的组合
当直角三角形，最短两条边均不大于100的情况下，有2060种情况可以满足
"""


def xxx():
    max_range = 1000000
    count_kind, large = 0, 0
    while True:
        large += 1
        for sortSide in range(2, 2 * large + 1):
            n = large ** 2 + sortSide ** 2
            if n ** 0.5 % 1 == 0:
                count_kind += (sortSide // 2 - max(1, sortSide - large) + 1)
            if count_kind > max_range:
                return large
print(xxx())

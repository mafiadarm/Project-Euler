#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
五边形数
五边形数由公式Pn=n(3n−1)/2生成。前十个五边形数是：
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, …
可以看出P4 + P7 = 22 + 70 = 92 = P8。然而，它们的差70 − 22 = 48并不是五边形数。
在所有和差均为五边形数的五边形数对Pj和Pk中，找出使D = |Pk − Pj|最小的一对；此时D的值是多少？

分析：
差值肯定会越来越大，jk越接近，差值越小，找出第一对，就是最小的
先造列表 数量大的时候用set来查询，效率更高！
"""

def find_min(num=1):
    while True:
        num *= 10  # 不知道上限，就10倍往上找
        nums = [int(i * (3 * i - 1) / 2) for i in range(1, num)]  # 构造集合
        pen = set(nums)

        for x in range(1, num - 1):
            for n in range(0, x):
                if nums[x] - nums[n] in pen and nums[x] + nums[n] in pen:
                    return nums[x] - nums[n]
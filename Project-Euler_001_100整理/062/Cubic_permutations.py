#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
立方数重排
立方数41063625（345的3次方）可以重排为另外两个立方数：56623104（384的3次方）和66430125（405的3次方）。
实际上，41063625是重排中恰好有三个立方数的最小立方数。
求重排中恰好有五个立方数的最小立方数。

分析：
取数范围必定是同位的，不然结果的位数不一样
既然是重排，最好就是用sorted(str(
统计列表然后取五个一样的数，返回列表去找第一次出现此数的索引，索引+1则是这个数
"""
from itertools import count
from collections import Counter

def xxx():
    for cloth in count(2):
        test_range = 10 ** cloth
        start = int(test_range / 10)

        all_cubic = [sorted(str(i ** 3)) for i in range(start, test_range)]  # 所有经过重排的立方数
        # list.count的统计是按遍历来的，所以会按列表的顺序，从左到右的统计，all_cubic是从小到大排序，故若有取值，必为最小
        topmost = max(all_cubic, key=all_cubic.count)  # 取出现次数最多的数字,如果有一样大的，取左边第一个；

        if all_cubic.count(topmost) == 5:  # 如果这个数是出现刚好5次
            return (all_cubic.index(topmost) + start) ** 3  # 则取索引+1（index取第一个），就是他的值，返回这个值构造成立方数

def other():
    for cloth in count(2):
        test_range = 10 ** cloth
        start = int(test_range / 10)
        all_cubic = ["".join(sorted(str(i ** 3))) for i in range(start, test_range)]
        topmost = [k for k, v in Counter(all_cubic).items() if v == 5]  # Counter是有序的
        result = topmost[0] if topmost else ""  # 取第一个值，可能有多个值

        if result: return (all_cubic.index(result) + start) ** 3

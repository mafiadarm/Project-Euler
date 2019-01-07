#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数字阶乘链
145之所以广为人知，是因为它的各位数字的阶乘之和恰好等于本身：
1! + 4! + 5! = 1 + 24 + 120 = 145
而169则可能不太为人所知，尽管从169开始不断地取各位数字的阶乘之和构成了最长的循环回到169；事实上，只存在三个这样的循环：
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872
不难证明，从任意数字出发最终都会陷入循环。例如，
69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)
从69开始可以得到一个拥有五个不重复项的链，但是从一个小于一百万的数出发能够得到的最长的无重复项链包含有60项。
从小于一百万的数出发，有多少条链恰好包含有60个不重复项？
"""
from math import factorial

def xxx():
    max_range = 10 ** 6
    count = 0
    for num in range(2, max_range):  # 遍历100W以内所有数字
        num_set = {num}  # 链条要从数字本身开始
        flag = True  # while的结束条件

        while flag:  # 循环链条
            tmp = 0  # 链条变化的数字
            for i in str(num):
                tmp += factorial(int(i))

            if tmp in num_set:  # 如果链条集合已经有了，则统计一共有多少个链
                if len(num_set) == 60:
                    count += 1  # 计数+1
                flag = False
            else:
                num_set.add(tmp)
                num = tmp

    return count

print(xxx())
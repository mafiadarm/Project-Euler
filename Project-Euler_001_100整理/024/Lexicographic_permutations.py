#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
字典序排列
排列指的是将一组物体进行有顺序的放置。例如，3124是数字1、2、3、4的一个排列。如果把所有排列按照数字大小或字母先后进行排序，我们称之为字典序排列。0、1、2的字典序排列是：

012   021   102   120   201   210
数字0、1、2、3、4、5、6、7、8、9的字典序排列中第一百万位的排列是什么？
"""

ask = 1000000
dic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 有工具可以直接解决
from itertools import permutations

ite = permutations(dic)

while ask != 0:
    result = next(ite)
    ask -= 1

print(result)
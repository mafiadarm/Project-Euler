#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
大和
计算出以下一百个50位数的和的前十位数字。
"""

# 处理下文本
with open("large.txt", "r") as large:
    text = large.readlines()

# 转成数字集合
gather = [int(i.replace("\n", "")) for i in text]

# 计算
sum_gather = sum(gather)
a = sum_gather

# 计算是多少位的，如果用str去格式化，在数字很大的情况下，很耗内存
c = -10  # 因为求前10，使用先空出来
while a != 0:
    a = a//10
    c += 1

print(sum_gather//10**c)


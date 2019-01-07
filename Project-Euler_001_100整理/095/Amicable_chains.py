#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
亲和数链
一个数除了本身之外的因数称为真因数。例如，28的真因数是1、2、4、7和14。这些真因数的和恰好为28，因此我们称28是完全数。
有趣的是，220的真因数之和是284，同时284的真因数之和是220，构成了一个长度为2的链，我们也称之为亲和数对。
有一些更长的序列并不太为人所知。例如，从12496出发，可以构成一个长度为5的链：
12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → …)
由于这条链最后又回到了起点，我们称之为亲和数链。
找出所有元素都不超过一百万的亲和数链中最长的那条，并给出其中最小的那个数。

分析：
找出最长链中最小的数字
先构造一个列表，为每个数字的公倍数，用于查询，索引为这个数，值为这个数的真因数之和
"""

def make_list(num):
    factor_sum = [0, 1] + [0] * (num - 2)  # 构造列表
    for i in range(1, num):
        for j in range(i * 2, num, i):
            factor_sum[j] += i
    return factor_sum

def xxx():
    ask = 1000000
    factor_sum_list = make_list(ask)

    # 开始计算最长链的最小值
    min_num = 0
    count_len = 0

    for kk in range(2, ask):
        flag = 1
        container = []
        chain= factor_sum_list[kk]
        copy_num = chain
        while chain not in container:  # 判断是否重复，终止链
            container.append(chain)
            if chain > 1e6 or chain == 1:
                flag = 0
                break
            chain = factor_sum_list[chain]
        if flag and chain == copy_num:  # 开始结束均为同一个数
            length = len(container)
            if length > count_len:  # 选取最长的链
                count_len = length
                min_num = min(container)
    return min_num

print(xxx())
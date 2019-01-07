#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
子串的可整除性
1406357289是一个0至9全数字数，因为它由0到9这十个数字排列而成；但除此之外，它还有一个有趣的性质：子串的可整除性。
记d1是它的第一个数字，d2是第二个数字，依此类推，我们注意到：
d2d3d4=406能被2整除
d3d4d5=063能被3整除
d4d5d6=635能被5整除
d5d6d7=357能被7整除
d6d7d8=572能被11整除
d7d8d9=728能被13整除
d8d9d10=289能被17整除
找出所有满足同样性质的0至9全数字数，并求它们的和。

分析：
0-9全数字数，用组合的方式获取
d2-d4、d3-d5...以此类推 用遍历切片[n:n+2]
2-17的质数
"""
from itertools import permutations

container = permutations("0123456789")  # 全组合
prime_list = [2, 3, 5, 7, 11, 13, 17]  # 质数列表
result = []

def xxx(test_num):
    for n in range(1, 8):  # 索引范围
        if int(test_num[n:n+3]) % prime_list[n-1]: return  # 如果过程中有不满足条件的情况，则打断
    return 1

for test in container:
    if test[0] == "0": continue  # 如果是0开始的，则放弃
    num = "".join(test)

    if xxx(num): result.append(int(num))  # 满足条件则加到结果

print(result, sum(result))
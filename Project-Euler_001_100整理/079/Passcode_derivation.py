#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
密码推断
网上银行常用的一种密保手段是向用户询问密码中的随机三位字符。
例如，如果密码是531278，询问第2、3、5位字符，正确的回复应当是317。
在文本文件keylog.txt中包含了50次成功登陆的正确回复。
假设三个字符总是按顺序询问的，分析这个文本文件，给出这个未知长度的密码最短的一种可能。

分析：
先考虑没有重复数字的可能
筛选出所有出现过的数字
用冒泡排序，对接每一次密码提出来的数字
"""


def xxx():
    with open("p079_keylog.txt", "r") as rr:
        ss = rr.readlines()

    digits = list({i[j] for i in ss for j in range(3)})  # 按规律找出数字，去重,转列表
    auth_list = [i[:3] for i in ss]  # 使用过的数字列表

    for i in auth_list:  # 逐一提出数字，这个数字一定是按规律提出来的
        a, b, c = [digits.index(j) for j in i]  # 获取各位数所在digits的索引，这个索引就是按照顺序排列的
        digits[a], digits[b], digits[c] = [digits[j] for j in sorted([a, b, c])]  # 做冒泡排序，把数字排回去

    return "".join(digits)

print(xxx())
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
姓名得分
在这个46K的文本文件names.txt（右击并选择“目标另存为……”）中包含了五千多个姓名。首先将它们按照字母序排列，然后计算出每个姓名的字母值，乘以它在按字母顺序排列后的位置，以计算出姓名得分。

例如，按照字母序排列后，位于第938位的姓名COLIN的字母值是3 + 15 + 12 + 9 + 14 = 53。因此，COLIN的姓名得分是938 × 53 = 49714。

文件中所有姓名的姓名得分之和是多少？ 324536 s = open(names.txt,r+) ss = s.read()
"""

with open("p022_names.txt", "r") as rr:
    ask = rr.readline()

# 处理下文本
ask = ask.replace('"', "").replace(",", "")

# 做一个分数字典
letter_score = dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), list(range(1,27))))

# 遍历计算
result = 0
for i in ask:
    result += letter_score.get(i)

print(result)

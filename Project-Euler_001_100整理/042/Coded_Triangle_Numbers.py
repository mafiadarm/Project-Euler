#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
编码三角形数
三角形数序列的第n项由公式tn[t的n次方] = 1/2 n(n+1)[1/2的n(n+1)次方]给出；因此前十个三角形数是：
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
将一个单词的每个字母分别转化为其在字母表中的顺序并相加，我们可以计算出一个单词的值。例如，单词SKY的值就是 19 + 11 + 25 = 55 = t10。如果一个单词的值是一个三角形数，我们就称这个单词为三角形单词。

在这个16K的文本文件words.txt （右击并选择“目标另存为……”）中包含有将近两千个常用英文单词，这其中有多少个三角形单词？
"""

from itertools import count

# 处理下文本
with open("p042_words.txt", "r") as word:
    lis = word.readlines()[0]

word_list = set(lis.split("\""))
word_list.remove("")
word_list.remove(",")

# 构造三角形数的集合
num_list = []
larg = max([len(l) for l in word_list])  # 用最长的单词做上限
for i in count(1):
    num_list.append(int((1 / 2) * i * (i + 1)))
    if num_list[-1] > larg * 26:  # 大于上限就不要了
        break

# 构造一个字母对应数字值的
di = {value: num for num, value in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}

# 把单词变成值
num_form = [sum([di.get(n) for n in word]) for word in word_list]

# 统计，如果在三角形数集合里面有，就记为1
result = (sum([1 for num in num_form if num in num_list]))

    
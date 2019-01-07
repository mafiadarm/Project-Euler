#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
罗马数字
要正确地用罗马数字表达一个数，必须遵循一些基本规则。尽管符合规则的写法有时会多于一种，但对每个数来说总是存在一种“最好的”写法。
例如，数16就至少有六种写法：
IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI
然而，根据规则，只有XIIIIII和XVI是合理的写法，而后一种因为使用了最少的数字而被认为是最有效的写法。
在这个11K的文本文件roman.txt （右击并选择“目标另存为……”）中包含了一千个合理的罗马数字写法，但并不都是最有效的写法；有关罗马数字的明确规则，可以参考关于罗马数字。
求出将这些数都写成最有效的写法所节省的字符数。
注意：你可以假定文件中的所有罗马数字写法都不包含连续超过四个相同字符。
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
数字必须按大小的顺序排列
M，C和X不能等同或超过较小的面值
D，L和V每个只能出现一次
减法原则：
只有一个I，X和C可以用作减法对的一部分的主要数字。
I只能放在V和X之前。
X只能放在L和C之前。
C只能放在D和M之前。
"""

def xxx():
    text = "p089_roman.txt"
    with open(text, "r") as rr:
        ss = rr.readlines()

    ss = "".join(ss)
    X = (("IIII", 2), ("XXXX", 2), ("CCCC", 2), ("VIIII", 1), ("LXXXX", 1), ("DCCCC", 1))  # 规定一个统计方式
    return sum([ss.count(num) * x for num, x in X])
    
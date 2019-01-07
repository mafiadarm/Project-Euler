#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
幂的数字和
一古戈尔（10的100次方）是一个巨大的数字：一后面跟着一百个零。100的100次方则更是无法想像地巨大：一后面跟着两百个零。然而，
尽管这两个数如此巨大，各位数字和却都只有1。
若a, b < 100，所有能表示为a的b次方的自然数中，最大的各位数字和是多少？
"""

def xxx():
    num = 0
    for a in range(100):
        for b in range(100):
            n = 0
            for i in str(a ** b):
                n += int(i)
            if num < n:
                num = n
    return num
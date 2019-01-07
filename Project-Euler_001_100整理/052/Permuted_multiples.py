#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
重排的倍数
可以看出，125874和它的两倍251748拥有同样的数字，只是排列顺序不同。
有些正整数x满足2x、3x、4x、5x和6x都拥有相同的数字，求其中最小的正整数。
"""
from itertools import count

def xxx():
    for test in count(1):
        flag = 0
        flag_num = sorted(str(test))
        for i in range(2, 7):
            if sorted(str(test * i)) == flag_num:
                flag += 1
                if flag == 5:
                    return test
            else: continue

print(xxx())
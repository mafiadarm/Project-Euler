#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
幂次与位数
五位数16807=7的5次方 同时也是一个五次幂。同样的，九位数134217728=8的9次方 同时也是九次幂。
有多少个n位正整数同时也是n次幂？

分析：
因为10的n次方肯是n+1位数，所以以9为准，往上排查，看看上边界是多少
在此边界内统计其他的数
或者直接获取

用数学分析一下：
如果使得某个数k的n次方是一个n位数，k显然必须小于10，且k^n>10^(n-1)
后面的不等式在取对数后，最终可化为
n<1/(1-log10(k)),当然，这里n是允许等于1的（即5的1次方是1位数，这是计数在内的）。
import math
num=0
for k in range(1,10):
    temp = 1/(1-math.log10(k))
    num+=int(temp)
得出n要小于21.8，则范围取值为1-22
"""
from itertools import count

def xxx():
    test_border = 1
    while 1:
        if len(str(9 ** test_border)) < test_border:
            break
        test_border += 1

    answer = test_border -1
    for num in range(1, 9):  # 9的边界也计数了，所以直接加上去了
        for cloth in range(1, test_border):
            digit = len(str(num ** cloth))
            if digit == cloth:
                answer += 1
            elif digit < cloth: break

    return answer

def other():
    result = 0
    for num in range(1, 10):
        for cloth in count(1):
            if len(str(num ** cloth)) == cloth:
                result += 1
            elif len(str(num ** cloth)) < cloth: break
    return result

print(other())
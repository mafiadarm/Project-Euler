#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
格点直角三角形
点P(x1, y1)和点Q(x2, y2)都是格点，并与原点O(0,0)构成ΔOPQ。
当点P和点Q的所有坐标都在0到2之间，也就是说0 ≤ x1, y1, x2, y2 ≤ 2时，恰好能构造出14个直角三角形。
如果0 ≤ x1, y1, x2, y2 ≤ 50，能构造出多少个直角三角形？
"""

def xxx():
    """
    直角三角形公式：两短边长平方相加等于长边平方
    除去重复的
    :return:
    """
    count = 0
    for x1 in range(51):
        for y1 in range(51):
            for x2 in range(51):
                for y2 in range(51):
                    aa = x1**2 + y1**2
                    bb = x2**2 + y2**2
                    cc = (x1-x2)**2 + (y1-y2)**2
                    if (aa == bb + cc or bb == aa + cc or cc == aa + bb) and aa != 0 and bb != 0 and cc != 0:
                        count += 1
    return count/2

#方法二：根据几何知识，互相垂直的直线斜率乘积为-1**
def Euclidean(a, b):#计算最大公因数，辗转相除法
    d = a % b
    if d == 0:
        return b
    else:
        while d != 0:
            a, b = b, a % b
            d = a % b
        return b

count= 0
for i in range(1, 51):
    for j in range(1, 51):
        k = Euclidean(i, j)
        count += min(int((50 - i) * k / j), int((j * k / i))) * 2
count += 50 * 50 * 3 #在边上的
print(count)

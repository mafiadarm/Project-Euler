#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
硬币分拆
记p(n)是将n枚硬币分拆成堆的不同方式数。例如，五枚硬币有7种分拆成堆的不同方式，因此p(5)=7。
OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O
找出使p(n)能被一百万整除的最小n值。

分析：
被100W整除的就是2   100W是被除数就是以下...
维基百科的公式
p(k) = p(k-(3*n*n-n)/2) + p(k-(3*n*n+n)/2) - p(k-(3*n*n+5*n+2)/2) - p(k-(3*n*n+7*n+4)/2) +... (n from 1 to ...) while p(0) = 1 and p(1) = 1
"""


def xxx():
    from itertools import count
    tmpDict = {0: 1, 1: 1}
    for k in count():
        s = 0
        if k == 0 or k == 1:
            continue
        for n in range(1, int(k ** 0.5 + 1), 2):
            a = k - (3 * n * n - n) / 2
            b = k - (3 * n * n + n) / 2
            c = k - (3 * n * n + 5 * n + 2) / 2
            d = k - (3 * n * n + 7 * n + 4) / 2
            if a >= 0:
                s += tmpDict[a]
            else:
                break
            if b >= 0:
                s += tmpDict[b]
            else:
                break
            if c >= 0:
                s -= tmpDict[c]
            else:
                break
            if d >= 0:
                s -= tmpDict[d]
            else:
                break
        tmpDict[k] = s

        if not s % 1000000:
            return k
    
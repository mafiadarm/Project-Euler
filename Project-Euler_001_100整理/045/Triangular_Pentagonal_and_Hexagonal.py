#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
三角形数、五边形数和六角形数
三角形数、五边形数和六角形数分别由以下公式给出：
三角形数	Tn=n(n+1)/2	1, 3, 6, 10, 15, …
五边形数	Pn=n(3n−1)/2	1, 5, 12, 22, 35, …
六边形数	Hn=n(2n−1)	1, 6, 15, 28, 45, …
可以验证，T285 = P165 = H143 = 40755。
找出下一个同时是三角形数、五边形数和六角形数的数。

分析：
构造三个集合
用集合去比较，出来的最小的，即是下一个
"""
ask = 100
while True:
    ask *= 10  # 10的指数扩大范围
    # 分别构造集合，从已知的开始
    triangle_set = {int(i * (i + 1) / 2) for i in range(286, ask)}
    Pentagonal_set = {int(j * (3 * j - 1) / 2) for j in range(166, ask)}
    Hexagonal_set = {k * (2 * k - 1) for k in range(144, ask)}

    result = triangle_set & Pentagonal_set & Hexagonal_set
    if result:
        print(min(result))  # 怕同时出现多个
        break
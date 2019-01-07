#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
立方体数字对
在一个立方体的六个面上分别标上不同的数字（从0到9），对另一个立方体也如法炮制。将这两个立方体按不同的方向并排摆放，我们可以得到各种各样的两位数。
例如，平方数64可以通过这样摆放获得：
事实上，通过仔细地选择两个立方体上的数字，我们可以摆放出所有小于100的平方数：01、04、09、16、25、36、49、64和81。
例如，其中一种方式就是在一个立方体上标上{0, 5, 6, 7, 8, 9}，在另一个立方体上标上{1, 2, 3, 4, 8, 9}。
在这个问题中，我们允许将标有6或9的面颠倒过来互相表示，只有这样，如{0, 5, 6, 7, 8, 9}和{1, 2, 3, 4, 6, 7}这样本来无法表示09的标法，才能够摆放出全部九个平方数。
在考虑什么是不同的标法时，我们关注的是立方体上有哪些数字，而不关心它们的顺序。
{1, 2, 3, 4, 5, 6}等价于{3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6}不同于{1, 2, 3, 4, 5, 9}
但因为我们允许在摆放两位数时将6和9颠倒过来互相表示，这个例子中的两个不同的集合都可以代表拓展集{1, 2, 3, 4, 5, 6, 9}。
对这两个立方体有多少中不同的标法可以摆放出所有的平方数？
"""
from itertools import combinations

def xxx():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    con = set()
    for i in combinations(nums, 6):
        for j in combinations(nums, 6):
            if j + i not in con:
                if (0 in i and 1 in j) or (1 in i and 0 in j):
                    if (0 in i and 4 in j) or (4 in i and 0 in j):
                        if (0 in i and (9 in j or 6 in j)) or ((9 in i or 6 in i) and 0 in j):
                            if (1 in i and (6 in j or 9 in j)) or ((6 in i or 9 in i) and 1 in j):
                                if (2 in i and 5 in j) or (5 in i and 2 in j):
                                    if (3 in i and (6 in j or 9 in j)) or ((6 in i or 9 in i) and 3 in j):
                                        if (4 in i and (9 in j or 6 in j)) or ((9 in i and 6 in i) and 4 in j):
                                            if ((6 in i or 9 in i) and 4 in j) or (4 in i and (6 in j or 9 in j)):
                                                if (8 in i and 1 in j) or (1 in i and 8 in j):
                                                    con.add(i + j)

    return len(con)

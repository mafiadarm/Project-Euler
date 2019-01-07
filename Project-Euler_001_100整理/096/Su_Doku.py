#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数独
数独（日语原意为数的位置）是一种热门的谜题。
它的起源已不可考，但是与欧拉发明的一种类似而更加困难的谜题拉丁方阵之间有着千丝万缕的联系。
数独的目标是替换掉9乘9网格中的空白位置（或0），使得每行、每列以及每个九宫格中恰好都包含数字1~9。
如下是一个典型的数独谜题以及它的解答。
0 0 3	0 2 0	6 0 0	*	4 8 3	9 6 7	2 5 1
9 0 0	3 0 5	0 0 1	*	9 2 1	3 4 5	8 7 6
0 0 1	8 0 6	4 0 0	*	6 5 7	8 2 1	4 9 3
0 0 8	1 0 2	9 0 0	*	5 4 8	7 2 9	1 3 6
7 0 0	0 0 0	0 0 8	*	1 3 2	5 6 4	7 9 8
0 0 6	7 0 8	2 0 0	*	9 7 6	1 3 8	2 4 5
0 0 2	6 0 9	5 0 0	*	3 7 2	8 1 4	6 9 5
8 0 0	2 0 3	0 0 9	*	6 8 9	2 5 3	4 1 7
0 0 5	0 1 0	3 0 0	*	5 1 4	7 6 9	3 8 2
一个构造精良的数独谜题应该包含有唯一解，且能够通过逻辑推断来解决，尽管有时可能必须通过“猜测并检验”来排除一些选项（这一要求目前还颇受争议）。
寻找答案的复杂度决定了题目的难度；上面这个谜题被认为是简单的谜题，因为我们可以通过直截了当的演绎推理来解决它。
在这个6K的文本文件sudoku.txt（右击并选择“目标另存为……”）中包含有50个不同难度的数独谜题，但保证它们都只有唯一解（文件中的第一个谜题就是上述样例）。
解开这50个谜题，找出每个谜题解答左上角的三个数字并连接起来，给出这些数的和；
举例来说，上述样例解答左上角的三个数字连接起来构成的数是483。
"""
from pymprog import model, iprod

g = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]]

p = model("sudoku")
I = range(1, 10)
J = range(1, 10)
K = range(1, 10)
T = iprod(I, J, K)  # 标记元组
x = p.var('x', T, bool)
# x[i,j,k] = 1 means cell [i,j] is assigned number k
# assign pre-defined numbers using the "givens"
[x[i, j, k] == (1 if g[i - 1][j - 1] == k else 0) for (i, j, k) in T if g[i - 1][j - 1] > 0]

# each cell must be assigned exactly one number
[sum(x[i, j, k] for k in K) == 1 for i in I for j in J]

# cells in the same row must be assigned distinct numbers
[sum(x[i, j, k] for j in J) == 1 for i in I for k in K]

# cells in the same column must be assigned distinct numbers
[sum(x[i, j, k] for i in I) == 1 for j in J for k in K]

# cells in the same region must be assigned distinct numbers
[sum(x[i, j, k] for i in range(r, r + 3) for j in range(c, c + 3)) == 1 for r in range(1, 10, 3) for c in range(1, 10, 3) for k in K]

# there is no need for an objective function here

p.solve()

for i in I:
    if i in range(1, 10, 3):
        print(" +-------+-------+-------+")
    print('', end=' ')
    for j in J:
        if j in range(1, 10, 3): print("|", end=' ')
        print("%g" % sum(x[i, j, k].primal * k for k in K), end=' ')
        if j == 9: print("|")
    if i == 9:
        print(" +-------+-------+-------+")
p.end()

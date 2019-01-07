#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
最大路径和 II
从下面展示的三角形的顶端出发，不断移动到在下一行与其相邻的元素，能够得到的最大路径和是23。
3
7 4
2 4 6
8 5 9 3
如上图，最大路径和为 3 + 7 + 4 + 9 = 23。
在这个15K的文本文件triangle.txt（右击并选择“目标另存为……”）中包含了一个一百行的三角形，求从其顶端出发到达底部，所能够得到的最大路径和。
注意：这是第18题的强化版。由于总路径一共有299条，穷举每条路经来解决这个问题是不可能的！即使你每秒钟能够检查一万亿（1012）条路径，全部检查完也需要两千万年。存在一个非常高效的算法能解决这个问题。;o)
"""


def xxx():
    with open("P067_triangle.txt", "r") as rr:
        li = rr.readlines()
    tri = [i.replace("\n", "").split() for i in li]

    for i in range(1, len(tri)):
        count_last_line = len(tri[-(i + 1)])
        tri[-(i + 1)] = [max(int(tri[-i][j]) + int(tri[-(i + 1)][j]), int(tri[-i][j + 1]) + int(tri[-(i + 1)][j])) for j
                         in range(count_last_line)]
    return print(tri[0][0])
    
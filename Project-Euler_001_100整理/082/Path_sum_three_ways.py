#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
路径和：三个方向
注意：这是第81题的一个更具挑战性的版本。
在如下的5乘5矩阵中，从最左栏任意一格出发，始终只向右、向上或向下移动，到最右栏任意一格结束的最小路径和为994，由标注红色的路径给出。
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
在这个31K的文本文件matrix.txt（右击并选择“目标另存为……”）中包含了一个80乘80的矩阵，求出从最左栏到最右栏的最小路径和。
"""

def xxx():
    path_list = []
    with open("p081_matrix.txt", "r") as rr:
        for i in range(80):
            str_num = rr.readline().replace("\n", "").split(",")
            path_list.append([int(i) for i in str_num])

    targ_list = [path_list[i][79] for i in range(80)]
    for i in range(78, -1, -1):
        targ_list[0] = targ_list[0] + path_list[0][i]

        for j in range(1, 80):
            targ_list[j] = min(targ_list[j] + path_list[j][i], targ_list[j - 1] + path_list[j][i])

        for k in range(78, -1, -1):
            targ_list[k] = min(targ_list[k], targ_list[k + 1] + path_list[k][i])

    return min(targ_list)
    
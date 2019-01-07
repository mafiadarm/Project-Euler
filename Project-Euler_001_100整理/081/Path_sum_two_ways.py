#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
路径和：两个方向
在如下的5乘5矩阵中，从左上方到右下方始终只向右或向下移动的最小路径和为2427，由标注红色的路径给出。
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
在这个31K的文本文件matrix.txt（右击并选择“目标另存为……”）中包含了一个80乘80的矩阵，求出从该矩阵的左上方到右下方始终
只向右和向下移动的最小路径和。
"""

def xxx():
    path_list = []
    with open("p081_matrix.txt", "r") as rr:
        for i in range(80):
            str_num = rr.readline().replace("\n", "").split(",")
            path_list.append([int(i) for i in str_num])

    side = len(path_list)
    for i in range(side):
        for j in range(side):
            if i == 0 and j == 0:
                pass
            elif i == 0:
                path_list[i][j] += path_list[i][j - 1]
            elif j == 0:
                path_list[i][j] += path_list[i - 1][j]
            else:
                if path_list[i][j - 1] < path_list[i - 1][j]:
                    path_list[i][j] += path_list[i][j - 1]
                else:
                    path_list[i][j] += path_list[i - 1][j]
    return path_list[side - 1][side - 1]

print(xxx())
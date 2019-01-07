#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
路径和：四个方向
注意：这是第81题的一个极具挑战性的版本。
在如下的5乘5矩阵中，从左上角到右下角任意地向上、向下、向左或向右移动的最小路径和为2297，由标注红色的路径给出。
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
在这个31K的文本文件matrix.txt（右击并选择“目标另存为……”）中包含了一个80乘80的矩阵，求出从左上角到右下角任意地向上、向下、向左或向右移动的最小路径和。
"""

import numpy as np
an =[]
with open("p081_matrix.txt", "r") as fan:
    #读取数据
    while 1:
        x=fan.readline()
        if len(x) == 0:
            break
        du = []
        for jjj in list(x.split(',')):
            du.append(jjj)
        an.append(du)

n_pan = np.array(an, dtype=int)#转化为np数组形式转置
copy_n_pan = np.array(n_pan.copy(), dtype = float)

#开始
for jj in range(len(n_pan)):
    for gg in range(len(n_pan)):
        copy_n_pan[jj, gg] = float('inf')
copy_n_pan[0, 0] = n_pan[0, 0]

#构建联通字典
lian_tong = {}
for gg in range(len(n_pan)):
    for hh in range(len(n_pan)):
        dd = [[gg - 1, hh],[gg + 1, hh],[gg, hh - 1],[gg, hh + 1]]
        lian_tong[(gg, hh)] = []
        for ff in dd:
            if 0 <= ff[0] < len(n_pan) and 0 <= ff[1] < len(n_pan):
                lian_tong[(gg, hh)].append(ff)
#Dijkstra 算法
def dijkstra(start_list, li_dict=lian_tong, yuan_shi=n_pan, com=copy_n_pan):
    start = []
    if not start_list:
        return com
    else:
        for kk in start_list:
            fu_list = li_dict[(kk[0], kk[1])]
            for sss in fu_list:
                com_number = com[kk[0], kk[1]] + yuan_shi[sss[0], sss[1]]
                if com_number < com[sss[0], sss[1]]:
                    com[sss[0], sss[1]] = com_number
                    start.append(sss)
    return dijkstra(start)

print(int(dijkstra([[0, 0]])[-1,-1]))

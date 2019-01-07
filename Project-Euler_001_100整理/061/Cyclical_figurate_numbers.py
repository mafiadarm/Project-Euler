#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
循环的多边形数
三角形数、正方形数、五边形数、六边形数、七边形数和八边形数统称为多边形数。它们分别由如下的公式给出：
三角形数	P3,n=n(n+1)/2	1, 3, 6, 10, 15, …   n = (num*2+0.5**2)**0.5-0.5
正方形数	P4,n=n2	1, 4, 9, 16, 25, …           n = num**0.5
五边形数	P5,n=n(3n−1)/2	1, 5, 12, 22, 35, …  n = (1+(1+num*4*3*2)**0.5)/6
六边形数	P6,n=n(2n−1)	1, 6, 15, 28, 45, …  n = (1+(1+4*2*num)**0.5)/4
七边形数	P7,n=n(5n−3)/2	1, 7, 18, 34, 55, …  n = (3+(9+4*5*2*num)**0.5)/10
八边形数	P8,n=n(3n−2)	1, 8, 21, 40, 65, …  n = (2+(4+4*3*num)**0.5)/6
由三个4位数8128、2882、8281构成的有序集有如下三个有趣的性质。
这个集合是循环的，每个数的后两位是后一个数的前两位（最后一个数的后两位也是第一个数的前两位）。
每种多边形数——三角形数（P3,127=8128）、正方形数（P4,91=8281）和五边形数（P5,44=2882）——在其中各有一个代表。
这是唯一一个满足上述性质的4位数有序集。

存在唯一一个包含六个4位数的有序循环集，每种多边形数——三角形数、正方形数、五边形数、六边形数、七边形数和八边形数——在其中各有一个代表。
求这个集合的元素和。

分析：
确定是在4位数里面找
可以构造每个多边形数在同等位数的集合，再遍历实现，但是这样就有6个指数的量
前两位=后两位 可以用num % 100 == num // 100 或者 str(num)[:2]==str(num)[2:]表达
因为是在确定的元素里面找，一定能找到，所以选择用递归查询
"""
from itertools import count

def x_shape_list(lambda_func, max_range, min_range=1):  # lambda_func= lambda x:公式 范例见061
    # 构造在一个范围内的多边形数的集合
    polygons_list = []
    for i in count(1):
        polygons = lambda_func(i)
        if polygons < min_range:  # 不取小于此值的
            continue
        if polygons > max_range:  # 超过此值说明构造完成
            return polygons_list
        polygons_list.append(polygons)

def recursion(result_list, polygons_list, flag):
    """
    :param result_list: 传进来的时候是包含起始数的列表，会在迭代中增加，当达到6的时候，会完成
    :param polygons_list: 包含各个多边形数集合的列表
    :param flag: 寻址标记
    :return:
    """
    # 当列表达到6个元素，并且首尾相连的时候，完成搜寻
    if len(result_list) == 6 and str(result_list[-1])[:2] == str(result_list[0])[2:]:
        return print(result_list, sum(result_list))

    # 进入递归
    for i in range(6):
        if flag[i]: continue  # 如果为真则说明在这个集合已经查到了

        # 用flag标记位置是避免循环不是按从小到大的多边形顺序
        flag[i] = True  # 标记此条列表已用，如果在下面的遍历中达成，进入递归的时候也带进去。

        for polygons in polygons_list[i]:
            if str(polygons)[:2] == str(result_list[-1])[2:]:  # 和列表最后一个数比较，列表在变化，所以每次最后一个数也在变
                recursion(result_list.extend(polygons), polygons_list, flag)

        flag[i] = False  # 如果没找到，则重新标记为待用

def xxx(min_num=1000, max_num=10000):
    p3 = x_shape_list(lambda n: n * (n + 1) // 2, max_num, min_num)
    p4 = x_shape_list(lambda n: n * n, max_num, min_num)
    p5 = x_shape_list(lambda n: n * (3 * n - 1) // 2, max_num, min_num)
    p6 = x_shape_list(lambda n: n * (2 * n - 1), max_num, min_num)
    p7 = x_shape_list(lambda n: n * (5 * n - 3) // 2, max_num, min_num)
    p8 = x_shape_list(lambda n: n * (3 * n - 2), max_num, min_num)
    p_list = [p3, p4, p5, p6, p7, p8]

    flag = [False] * 6
    flag[-1] = True  # 从p8开始找，则是前两位是p3的后两位

    for i in p8:  # 以p8为开始，因为p8必定是最后那个数，既是结束又是开始
        recursion([i], p_list, flag)


    
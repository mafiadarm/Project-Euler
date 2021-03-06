#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
e的有理逼近
2的算术平方根可以写成无限连分数的形式。
这个无限连分数可以简记为√2 = [1;(2)]，其中(2)表示2无限重复。同样的，我们可以记√23 = [4;(1,3,1,8)]。
可以证明，截取算术平方根连分数表示的一部分所组成的序列，给出了一系列最佳有理逼近值。让我们来考虑√2的逼近值：
√2的前十个逼近值为：
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, …
最令人惊讶的莫过于重要的数学常数e有如下连分数表示
e = [2; 1,2,1, 1,4,1, 1,6,1 , … , 1,2k,1, …]。
e的前十个逼近值为：
2/1, 6/2, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, …
第10个逼近值的分子各位数字之和为1+4+5+7=17。
求e的第100个逼近值的分子各位数字之和。

分析：
以下对应关系：
 1   1   2    1    1    4      1     1       6
2/1 3/1 8/3 11/4 19/7 87/32 106/39 193/71 1264/465
可以发现
1264/465 = 193*6+106 / 71*6+39
193/71 = 106*1+87 / 39*1+32
106/39 = 87*1+19 / 32*1+7
87/32 = 19*4+11 / 7*4+4
19/7 = 11*1+8 / 4*1+3
11/4 = 8*1+3 / 3*1+1
8/3 = 3*2+2 / 1*2+1
有点像菲波拉契数，需要乘以对应的系数，即a3/b3 = a1+a2*a3系数/b1+b2*b3系数
所以求分子，就只需要出来分子即可
"""


def xxx():
    # 构造系数列表
    coefficient_list = []
    for i in range(1, 101):
        coefficient = 1 if i%3 else int(i/3*2)
        coefficient_list.append(coefficient)

    # 构造分子列表
    e_value = [2, 3]
    for j in range(98):
        new_member = e_value[j]+e_value[j+1]*coefficient_list[j+2]
        e_value.append(new_member)

    result = eval("+".join(str(e_value[-1])))
    return result

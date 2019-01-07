#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
整数边长直角三角形
若三边长{a,b,c}均为整数的直角三角形周长为p，当p = 120时，恰好存在三个不同的解：
{20,48,52}, {24,45,51}, {30,40,50}
在所有的p ≤ 1000中，p取何值时有解的数目最多？

分析：
直角三角形都满足毕达哥拉斯
周长为p，则上限为p，遍历的方式取2条边，计算第3条边；如果三条边都是整数，且和小于p则纳入集合
通过最大的value，找对应的key 这里用到collections里面的Counter
max(dict(Counter([11,22,33,22])), key=dict(Counter([11,22,33,22])).get)
"""
from collections import Counter
ask = 1000
container = set()
for side_1 in range(1, ask):
    for side_2 in range(side_1+1, ask):
        side_3 = (side_1**2 + side_2**2) ** 0.5  # 按毕达哥拉斯定理计算出第三条边

        if not side_3%1 and side_1+side_2+side_3 <= ask:  # 如果三条边都是整数，且和小于p
            combo = tuple([side_1, side_2, int(side_3)])  # Counter只能统计tuple[不可变]
            container.add(combo)
        elif side_1+side_2+side_3 > ask:  # 过边界就打断
            break

p_list = [sum(c) for c in container]  # 获取边长合集
count = Counter(p_list).items()  # 统计合集
result = sorted(count, key=lambda x: x[1], reverse=True)[0][0]  # 排列并取值

print(result)
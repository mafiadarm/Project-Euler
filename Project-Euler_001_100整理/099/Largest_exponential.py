#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
最大的幂
比较两个如2^11和3^7这样写成幂的形式的数并不困难，任何计算器都能验证2^11 = 2048 < 3^7 = 2187。
然而，想要验证632382^518061 > 519432^525806就会变得非常困难，因为这两个数都包含有超过三百万位数字。
22K的文本文件base_exp.txt（右击并选择“目标另存为……”）有一千行，每一行有一对底数和指数，找出哪一行给出的幂的值最大。
注意：文件的前两行就是上述两个例子。

分析：
比较两个指数幂的大小时，化同底或同指：
当底同指不同时：构造同一指数函数,比大小（用这个，构造e为同底）
当指同底不同时：构造两个指数函数,利用图象比大小

相当于51^36 42^70比较转化为e^n = 51^36 e^n = 42^70
n = 36*loge(51)  n = 70*loge(42)
"""
import math

def xxx():
    # 处理下文本
    with open("p099_base_exp.txt") as ww:
        data_list = [data.replace("\n", "").split(",") for data in ww.readlines()]

    result, flag = 0, 0
    for log_group in data_list:
        count = int(log_group[1]) * math.log(int(log_group[0]))  # math.log(对数，底(默认为e))
        if flag < count:
            flag, result = count, log_group
    return data_list.index(result)+1

print(xxx())
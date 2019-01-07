#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
消去数字的分数

49/98是一个有趣的分数，因为缺乏经验的数学家可能在约简时错误地认为，等式49/98 = 4/8之所以成立，是因为在分数线上下同时抹除了9的缘故。

我们也会想到，存在诸如30/50 = 3/5这样的平凡解。

这类有趣的分数恰好有四个非平凡的例子，它们的分数值小于1，且分子和分母都是两位数。

将这四个分数的乘积写成最简分数，求此时分母的值。
"""
ask = 100
result = 1
view = []

# 100以内的两位数相比较
for numerator in range(10, ask):
    for denominator in range(numerator, ask):
        count = numerator / denominator  # 正常值
        # 处理消掉相同的数字
        a, b = sorted(str(numerator)), sorted(str(denominator))

        # 确保不是回文
        if a == b:
            continue

        # 去掉普通，因为有0，要么分母，要么分子，或者在普通实例里面
        elif "0" in a + b:
            continue

        # 去掉分子分母没有相同数字的
        elif not set(a) & set(b):
            continue

        # 去掉相同的数字
        for t in a:
            if t in b:
                a.remove(t)
                b.remove(t)

        # 处理完之后进行比较
        if int(a.pop())/int(b.pop()) == count:
            # 求乘积
            result *= denominator/numerator
            view.append(f"{numerator}/{denominator}=1/{int(denominator/numerator)}")

print(result, view)
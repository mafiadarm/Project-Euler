#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
消去数字的分数

49/98是一个有趣的分数，因为缺乏经验的数学家可能在约简时错误地认为，等式49/98 = 4/8之所以成立，是因为在分数线上下同时抹除了9的缘故。

我们也会想到，存在诸如30/50 = 3/5这样的平凡解。

这类有趣的分数恰好有四个非平凡的例子，它们的分数值小于1，且分子和分母都是两位数。

将这四个分数的乘积写成最简分数，求此时分母的值。
"""

def gys(x, y):  # 求x,y的最大公约数  可以用math.gcd()
    while y:
        x, y = y, x % y
    return x

ask = 100
num_result = 1
den_result = 1
view = []

# 100以内的两位数相比较
for numerator in range(10, ask):
    for denominator in range(numerator+1, ask):
        count = numerator / denominator  # 正常值
        # 字符串化,用于比较
        a, b = sorted(str(numerator)), sorted(str(denominator))

        # 确保不是回文或者相同
        if a == b:
            continue

        # 去掉平凡解，因为有0，要么分母，要么分子，或者在普通实例里面
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
        a = int(('').join(a))
        b = int(('').join(b))
        if a / b == count:
            k = gys(a, b)
            s_a = int(a / k)
            s_b = int(b / k)
            num_result *= s_a
            den_result *= s_b
            view.append(f"{numerator}/{denominator}={s_a}/{s_b}")

rk = gys(num_result, den_result)
result = int(den_result / rk)
print(result, view)

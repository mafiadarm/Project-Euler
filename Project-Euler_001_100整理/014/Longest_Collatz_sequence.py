#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
最长考拉兹序列
在正整数集上定义如下的迭代序列：

n → n/2 （若n为偶数）
n → 3n + 1 （若n为奇数）

从13开始应用上述规则，我们可以生成如下的序列：

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
可以看出这个序列（从13开始到1结束）共有10项。尽管还没有被证明，但我们普遍认为，从任何数开始最终都能迭代至1（“考拉兹猜想”）。

从小于一百万的哪个数开始，能够生成最长的序列呢？

注： 序列开始生成后允许其中的项超过一百万。
"""

ask = 1000000

container = []
result = 0
c = 0
for i in range(1, ask):  # 依然用遍历的方式在计算了
    # 计算转换了几次
    a = i
    count = 0
    while i != 1:
        if i%2 == 0:
            i /= 2
            count += 1
        else:
            i = 3*i + 1
            count += 1
    # 记录最大值
    if c < count:
        c = count
        result = a
        print(c, result)

print(result)

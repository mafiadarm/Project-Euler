#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
素数重排
公差为3330的三项等差序列1487、4817、8147在两个方面非常特别：其一，每一项都是素数；其二，两两都是重新排列的关系。
一位素数、两位素数和三位素数都无法构成满足这些性质的数列，但存在另一个由四位素数构成的递增序列也满足这些性质。
将这个数列的三项连接起来得到的12位数是多少？

分析：
在所有4位素数中，找出一个递增3330的序列
构建4位数的素数集合
遍历每一个素数，并构建3330、6660的差的数字，检查是否都在集合里面
如果都在，则检查重排关系，如果是，则为结果
"""

def is_prime2(n):  # 短除法，验证数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


prime_set = {i for i in range(10 ** 3, 10 ** 4) if is_prime2(i)}  # 数字少就不用排除法了
prime_set -= {1487, 4817, 8147}  # 排除

for j in prime_set:
    j_3330 = j + 3330
    j_6660 = j + 6660
    if j_3330 not in prime_set or j_6660 not in prime_set:
        continue

    align = str(j)
    align_3 = str(j_3330)
    align_6 = str(j_6660)
    if sorted(align)==sorted(align_3)==sorted(align_6):
        print("".join([align, align_3, align_6]))
        break
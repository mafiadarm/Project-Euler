#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
欧拉总计函数与重排
在小于n的数中，与n互质的数的数目记为欧拉总计函数φ(n)（有时也称为φ函数）。例如，因为1、2、4、5、7和8均小于9且与9互质，故φ(9)=6。
1被认为和任意正整数互质，所以φ(1)=1。
有趣的是，φ(87109)=79180，而79180恰好是87109的一个重排。
在1 < n < 10的7次方中，有些n满足φ(n)是n的一个重排，求这些取值中使n/φ(n)最小的一个。

8319823 跑了好久，终于出来了
用69题的思路，本题的分解质因子的集合越少，最好是n=2个质因子相乘[因为肯定不是质数]
"""
def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def xxx(max_range=10 ** 7):
    lis = prime_list(int(max_range / 2), 2)  # 要保证2*最大质数 刚好在范围内
    num = 0
    cha = 10

    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            if lis[i] * lis[j] < max_range:
                x = y = lis[i] * lis[j]
                x *= 1 - 1 / lis[i]
                x *= 1 - 1 / lis[j]
                if sorted(str(y)) == sorted(str(int(x))):
                    if cha > y / x:
                        cha = y / x
                        num = y
            else:
                break
    return num
print(xxx())
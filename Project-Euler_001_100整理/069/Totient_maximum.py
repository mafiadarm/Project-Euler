#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
欧拉总计函数与最大值
在小于n的数中，与n互质的数的数目记为欧拉总计函数φ(n)（有时也称为φ函数）。例如，因为1、2、4、5、7和8均小于9且与9互质，故φ(9)=6。
n	互质的数	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666…
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
可以看出，对于n ≤ 10，当n=6时n/φ(n)取得最大值。
当n ≤ 1,000,000时，求使得n/φ(n)取得最大值的n。
1、不能为质数
2、因子越多，结果越大
结果：100W内，因子(除自己和1外)最多的合数
再分析，如果分解质因子的集合越多，说明欧拉总计函数越小[集合中包含相同的数，即为不互质]
所以直接从第一个质数开始往上乘[2x3x5x7x9x....]，在规定范围内，组成的最大的数就是 使得n/φ(n)取得最大值的n
如果在此范围内，数值过小，可以用这个数再从头开始乘以这些质数，试试会不会超过范围
"""
def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def xxx(max_range=10 ** 6):
    num_list = prime_list(int(max_range ** (1 / 2)))
    num = 1
    pri_list = []
    for i in num_list:
        num *= i
        pri_list.append(i)
        if num > max_range:
            num /= i
            pri_list.pop()
            break
    # 校验最大数 比如在100以内是90[2,3,5,3]
    while True:
        if num * pri_list[-1] > max_range:
            pri_list.pop()
        else:
            num *= pri_list[-1]
        if len(pri_list) == 0: return int(num)
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
连续素数的和
素数41可以写成六个连续素数的和：
41 = 2 + 3 + 5 + 7 + 11 + 13
在小于一百的素数中，41能够被写成最多的连续素数的和。
在小于一千的素数中，953能够被写成最多的连续素数的和，共包含连续21个素数。
在小于一百万的素数中，哪个素数能够被写成最多的连续素数的和？
"""
def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def answer(ask=10**6):
    # 测试连加到100w的范围
    nn = 1000
    test = 0  # 停止条件
    while test < ask:
        nn *= 10  # 按10的指数扩大范围
        primes_list = prime_list(nn)  # 会用到下面的函数中
        test = sum(primes_list)

    million_list = prime_list(ask)
    primes_set = set(million_list)  # 在set里面查询会快很多

    # 开始切取并计算
    count = len(primes_list)  # 统计素数个数
    for length in range(count, 0, -1):  # 反过来，先取最大的数字
        for i in range(0, count - length + 1):  # 补位，为下面的截取解决问题[从最长开始，逐渐缩小范围]
            sum_nums = sum(primes_list[i: i + length])  # 截取此段值加总[索引i到length的范围]
            if sum_nums > ask:  # 如果这个和大于100W，则length个列表里的数相加不成立
                break  # 之后的连加也不会成立，打断
            elif sum_nums in primes_set:  # 如果这个数字小于100W，而且在列表中，就是这个数
                return sum_nums, i, i + length
        pass  # 如果这个数字小于100W，但是不在列表内[非质数]，则i+1

print(answer())
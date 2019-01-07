#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
哥德巴赫的另一个猜想
克里斯蒂安·哥德巴赫曾经猜想，每个奇合数可以写成一个素数和一个平方的两倍之和。
9 = 7 + 2×1²
15 = 7 + 2×2²
21 = 3 + 2×3²
25 = 7 + 2×3²
27 = 19 + 2×2²
33 = 31 + 2×1²
最终这个猜想被推翻了。
最小的不能写成一个素数和一个平方的两倍之和的奇合数是多少？

分析：
奇合数即不能被2整除的合数，就是非素数且除2余1的数
按范围去找，构建质数和奇合数的集合
一个一个的去构建等式，出现无法构建的，找到最小的，即是答案
"""
def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表

def is_prime2(n):  # 短除法，验证数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

range_num = 10
while True:
    range_num *= 10  # 以10的指数扩大范围
    prime_nums = prime_list(range_num)  # 构造质数集合
    odd_divisible_num = [i for i in range(2, range_num) if i not in prime_nums and i % 2 == 1]  # 构造奇合数集合

    delete_num = []
    for odd in odd_divisible_num:
        for num in prime_nums:
            if odd > num:  # 必须要奇合数大于质数，才可能成立等式
                if (((odd - num) / 2) ** 0.5) % 1 == 0:  # 如果验证等式成功
                    delete_num.append(odd)  # 则把这个奇合数放到列表
                    break  # 等式成立就不用往下找素数去斗公式了，打断
            else:
                break  # 之后的负数没意义，所以打断

    result_set = set(odd_divisible_num) - set(delete_num)  # 比较列表
    if len(result_set) != 0:  # 如果有差异
        result = min(result_set)  # 则找出最小值，即是结果
        break
    else:
        print(range_num, "内无此数")

print(result)
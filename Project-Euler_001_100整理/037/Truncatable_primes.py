#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
可截素数
3797有着奇特的性质。不仅它本身是一个素数，而且如果从左往右逐一截去数字，剩下的仍然都是素数：3797、797、97和7；
同样地，如果从右往左逐一截去数字，剩下的也依然都是素数：3797、379、37和3。
只有11个素数，无论从左往右还是从右往左逐一截去数字，剩下的仍然都是素数，求这些数的和。
注意：2、3、5和7不被视为可截素数。
方法是切片[i::]和[:-i:]
"""
def isPrime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# 开始截取
def left_right_cut(num, flag):
    test_num = str(num)
    scope = range(len(test_num)) if flag else range(1, len(test_num))
    for t in scope:
        get_num = int(test_num[t:]) if flag else int(test_num[:-t:])
        if isPrime2(get_num):
            pass
        else: return
    return True

def main():
    result = []  # 用集合来装，避免重复
    num = 11  # 10以下的都不计算，从11开始计算
    # 如果一个数是可截数，截出来的数也应该是可截数，直到2位数为止
    while len(result) < 11:  # 因为只有11个，所以往上遍历，直到第11个出现
        num += 1
        if not left_right_cut(num, 1): continue
        if not left_right_cut(num, 0): continue
        result.append(num)
    return result

print(main())

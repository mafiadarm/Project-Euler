#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
圆周素数

197被称为圆周素数，因为将它逐位旋转所得到的数：197/971和719都是素数。

小于100的圆周素数有十三个：2、3、5、7、11、13、17、31、37、71、73、79和97。

小于一百万的圆周素数有多少个？
"""

"""
先整理去掉一些数字
[j for i in range(2,num) for j in range(i*i,num,i)]去除此列表内所有数字
用替换的方式
"""
ask = 1000000

placeholder = [1] * ask  # 要用占位的方式来处理掉非质数
placeholder[0], placeholder[1] = 0, 0

for i in range(2, ask):  # 能整除掉数字的数字都消掉
    if placeholder[i]:  # 加快速度，过滤已经被消掉的
        for j in range(i * i, ask, i):
            placeholder[j] = 0

prime_list = {str(digit) for digit, flag in enumerate(placeholder) if flag}  # 直接做成集合
result = prime_list.copy()  # 要copy下，不然会提示set不能再遍历的时候修改

for digit in prime_list:
    cycle = digit
    for _ in range(len(digit)):  # 根据位数
        cycle = cycle[-1] + cycle[:-1]  # 旋转交换
        if cycle not in result:  # 如果交换出来的数没有在素数列表(因为算法，在集合查比在列表快)
            result.remove(digit)  # 则从列表删除这个数
            break  # 并且停止循环，进入下一个数的测试

print(len(result), result)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
亲和数
记d(n)为n的所有真因数（小于n且整除n的正整数）之和。
如果d(a) = b且d(b) = a，且a ≠ b，那么a和b构成一个亲和数对，a和b被称为亲和数。

例如，220的真因数包括1、2、4、5、10、11、20、22、44、55和100，因此d(220) = 284；而284的真因数包括1、2、4、71和142，因此d(284) = 220。

求所有小于10000的亲和数的和。
"""

ask = 10000
result = 0
test_list = list(range(ask))

while len(test_list) != 0:  # 为了避免重复，把计算过的从列表删除
    num = test_list.pop()
    x, y = 0, 0

    for i in range(1, num):
        if num % i == 0:
            x += i

    for j in range(1, x):
        if x % j == 0:
            y += j

    if y == num and y != x:
        result += x+y
        if x < ask:  # 确保他在列表里面
            test_list.remove(x)

print(result)
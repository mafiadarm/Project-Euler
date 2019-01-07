#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
第10001个素数
列出前6个素数，它们分别是2、3、5、7、11和13。我们可以看出，第6个素数是13。

第10,001个素数是多少？
"""

from itertools import count

def is_prime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

ask = 10001
for test in count(2):  # 用遍历的方式，用短除法一个一个的验证
    if ask > 0 and is_prime2(test):
        ask -= 1
    elif is_prime2(test):
        print(test)
        break

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
双进制回文数

十进制数585 = 10010010012（二进制表示），因此它在这两种进制下都是回文数。

找出所有小于一百万，且在十进制和二进制下均回文的数，并求它们的和。

（请注意，无论在哪种进制下，回文数均不考虑前导零。）

2进制可以这么来表示 "{:b}".format(i) 或者 str(bin(i)[2:]
"""

def is_palindrome(n):  # 回文检测
    return str(n) == str(n)[::-1]

ask = 1000000
result = 0
for i in range(ask):
    if is_palindrome(str(bin(i))[2:]) and is_palindrome(i):
        result += i

print(result)

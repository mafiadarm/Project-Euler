#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
并非盈数之和
完全数是指真因数之和等于自身的那些数。例如，28的真因数之和为1 + 2 + 4 + 7 + 14 = 28，因此28是一个完全数。

一个数n被称为亏数，如果它的真因数之和小于n；反之则被称为盈数。

由于12是最小的盈数，它的真因数之和为1 + 2 + 3 + 4 + 6 = 16，所以最小的能够表示成两个盈数之和的数是24。通过数学分析可以得出，所有大于28123的数都可以被写成两个盈数的和；尽管我们知道最大的不能被写成两个盈数的和的数要小于这个值，但这是通过分析所能得到的最好上界。

----找出所有不能被写成两个盈数之和的正整数，并求它们的和。----
"""

def true_divisors(num):  # 列出一个数的所有真因数
    divisors = {1}
    for j in range(2, int(num**0.5)+1):
        if num % j == 0:
            divisors.add(j)
            divisors.add(num/j)
    return divisors

ask = 28123
result = list(range(28123+1))

# 找出12到28123内所有的盈数
abundant = []
for i in range(1, 28123+1):
    if sum(true_divisors(i)) > i:
        abundant.append(i)

# 让其两两组合，并排除于28123内
rang = len(abundant)
for t1 in range(rang):
    for t2 in range(t1, rang):
        got = abundant[t1] + abundant[t2]
        if got < ask and got in result:
            result.remove(got)
        else: break

# 剩下的数即是
print(result, sum(result))
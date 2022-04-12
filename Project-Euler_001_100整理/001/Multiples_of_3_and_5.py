#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3的倍数和5的倍数
如果我们列出10以内所有3或5的倍数，我们将得到3、5、6和9，这些数的和是23。

求1000以内所有3或5的倍数的和。

看成是梯形排列，汇总所有"."

            ...
          ... ...
        ... ... ...
      ... ... ... ...

这样就成了求梯形面积（三角形+顶） 数值范围整除3是多少，就是多少层（高、底）计算出多少个3，然后在乘以3
def suma(xrange,num): #效率较低的方法
    return sum(list(filter(lambda x:x%num == 0,range(1,xrange))))

def sumb(xrange=0,num=0): #省略大部分遍历时间
    return (num+num*(xrange//num))*(xrange//num)/2
"""

ask = 1000

three_high = ask // 3
five_high = ask // 5
repetition_high = ask // 15

sum_three = (three_high * 3 + 3) * three_high / 2
sum_five = (five_high * 5 + 5) * five_high / 2
repetition = (repetition_high * 15 + 15) * repetition_high / 2

all_sum = sum_three + sum_five - repetition

print(sum_three, sum_five, repetition, all_sum)

# 或者直接计算为
three_five_in_thousand = sum([n for n in range(1001) if n%3==0 or n%5==0])
print(three_five_in_thousand)

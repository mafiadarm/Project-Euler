#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
数星期日
下列信息是已知的，当然你也不妨自己再验证一下。

1900年1月1日是星期一。
三十天在九月中，
四六十一也相同。
剩下都是三十一，
除去二月不统一。
二十八天平常年，
多加一天在闰年。
闰年指的是能够被4整除却不能被100整除的年份，或者能够被400整除的年份。
在二十世纪（1901年1月1日到2000年12月31日）中，有多少个月的1号是星期天？
"""

import datetime

# 遍历日历来计算
result = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.datetime(year, month, 1).weekday() == 6:
            result += 1

print(result)
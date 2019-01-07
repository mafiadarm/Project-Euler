#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
表达数字的英文字母计数
如果把1到5写成英文单词，分别是：one, two, three, four, five，这些单词一共用了3 + 3 + 5 + 4 + 4 = 19个字母。

如果把1到1000都写成英文单词，一共要用多少个字母？

注意： 不要算上空格和连字符。例如，342（three hundred and forty-two）包含23个字母，而115（one hundred and fifteen）包含20个字母。单词“and”的使用方式遵循英式英语的规则。
"""

# 组合规则
str1 = {"one": 3, "two": 3, "three": 5, "four":4, "five":4, "six":3, "seven":5, "eight":5, "nine":4}
str2 = {"ten":3, "eleven":6, "twelve":6, "thirteen":8, "fourteen":8, "fifteen":7, "sixteen":7, "seventeen":9, "eighteen":8, "nineteen":8}
str3 = {"twenty":6, "thirty":6, "forty":5, "fifty":5, "sixty":5, "seventy":7, "eighty":6, "ninety":6}
str4 = {"hundred": 7, "and": 3}
str5 = {"thousand": 8}
# 经过统计，在100以内的时候，各出现的频率为 1-9为9次，10-19为1次，20-90为10次
# 从100开始，会多一个 1 hundred and 循环使用第一条一次，所以每100会循环使用1-9 100次，hundred 100次 and使用99次
# 1000的时候 1使用1次 thousand使用1次

sum_99 = sum(str1.values())*9 + sum(str2.values()) + sum(str3.values())*10
sum_100_999 = sum(str1.values())*100 + str4.get("hundred")*100*9 + str4.get("and")*99*9 + sum_99*9
sum_1000 = str5.get("thousand") + str1.get("one")

result =sum_99 + sum_100_999 + sum_1000

print(result)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
倒数的循环节

单位分数指分子为1的分数。分母为2至10的单位分数的十进制表示如下所示：

1/2= 0.5
1/3= 0.(3)
1/4= 0.25
1/5= 0.2
1/6= 0.1(6)
1/7= 0.(142857)
1/8= 0.125
1/9= 0.(1)
1/10= 0.1

这里0.1(6)表示0.166666…，括号内表示有一位循环节。可以看出，1/7有六位循环节。

找出正整数d < 1000，其倒数的十进制表示小数部分有最长的循环节。
"""

ask = 1000

def is_prime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# 问题化简，首先不是素数的数的循环节长度必定可以由其他数组成比如14可以由2*7组成
# 那么1/14与1/7有相同的循环节长度，所以只需找出所有的素数(不包括2与5)，求的他们的循环节长度

# 所以前提是所有的数必须是质数（即素数）循环节的长度是使分母P整除10^k-1的最小k值。
# 例如：
# 9可以整除10^1-1,所以当分母为9时，循环节是1位。
# 7可以整除10^6-1=999999,所以当分母为7时，循环节是6位

def test_length(num):
    # 必须排除2 或者 5
    if num == 2 or num == 5:
        return 0
    length = 1
    while 1:
        if (10**length - 1)%num == 0:
            break
        length += 1
    return length

# 先把计算结果放到集合里面，再用max的key求出最大的值
result = []
for number in range(ask):
    if is_prime2(number):
        result.append([test_length(number), number])

print(max(result, key=lambda x: x[0]))
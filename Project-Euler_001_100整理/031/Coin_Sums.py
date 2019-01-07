#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
硬币求和

英国的货币单位包括英镑£和便士p，在流通中的硬币一共有八种：

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)

以下是组成£2的其中一种可行方式：

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

不限定使用的硬币数目，组成£2有多少种不同的方式？
"""


# 遍历硬币去合
num = 0
for i in range(3):
    for j in range(5):
        if i * 100 + j * 50 > 200:
            break
        for k in range(11):
            if i * 100 + j * 50 + k * 20 > 200:
                break
            for l in range(21):
                if i * 100 + j * 50 + k * 20 + l * 10 > 200:
                    break
                for m in range(41):
                    if i * 100 + j * 50 + k * 20 + l * 10 + m * 5 > 200:
                        break
                    for n in range(101):
                        if i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n * 2 > 200:
                            break
                        for o in range(201):
                            if i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n * 2 + o * 1 == 200:
                                print(i,j,k,l,m,n,o)
                                num += 1
                                break
                            elif i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n * 2 + o * 1 > 200:
                                break

print(num)
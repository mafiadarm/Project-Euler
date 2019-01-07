#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
安排概率
在一个盒子中装有21个彩色碟子，其中15个是蓝的，6个是红的。如果随机地从盒子中取出两个碟子，取出两个蓝色碟子的概率是P(BB) = (15/21)×(14/20) = 1/2。
下一组使得取出两个蓝色盘子的概率恰好为50%的安排，是在盒子中装有85个蓝色碟子和35个红色碟子。
当盒子中装有超过10^12 = 1,000,000,000,000个碟子时，找出第一组满足上述要求的安排，并求此时盒子中蓝色碟子的数量。

分析：
用pell公式获得递推形式
blue:b, total:t
(b/t)*((b-1)/(t-1))=1/2==>b(b-1)/t(t-1)=1/2==>2b(b-1)=t(t-1)==>8b^2-8b+1=(2t-1)^2==>2(2b-1)^2-1=(2t-1)^2
换算pell方程：
d=2t-1,u=2b-1 ==> 2u^2-1=d^2 ==> d^2-2u^2=-1
d=2t-1,u=2b-1 ==> t=(d+1)/2, b=(u+1)/2
"""
def xxx():
    # 初始解
    d = 1
    u = 1
    ask = 1e12  # 科学计数法

    while 1:  # 一组一组的往上递推计算，超过ask的即为结果
        d, u = 3 * d + 4 * u, 2 * d + 3 * u
        result_total, result_blue = (d+1)/2, (u+1)/2
        print('Total:', result_total, "blue:", result_blue)

        if result_total > ask:
            return int(result_blue)




print(xxx())


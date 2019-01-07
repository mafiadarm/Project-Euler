#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
丢番图方程
考虑如下形式的二次丢番图方程：
x² – Dy² = 1
举例而言，当D=13时，x的最小值出现在649² – 13×180² = 1。
可以断定，当D是平方数时，这个方程不存在正整数解。
对于D= {2, 3, 5, 6, 7}分别求出x取最小值的解，我们得到：
3² – 2×2² = 1
2² – 3×1² = 1
9² – 5×4² = 1
5² – 6×2² = 1
8² – 7×3² = 1
因此，对于所有D ≤ 7，当D=5时x的最小值最大。
对于D ≤ 1000，求使得x的最小值最大的D值。

分析：
Pell方程解题思路
由X^2-D*Y^2=1。可得根号D约等于X/Y。而根号D恰好可以变为连分数的形式
"""

def GetPell(number):
    sboot=number**0.5
    #判断是否为完全平方数
    if int(sboot)-sboot==0:
        return [number]
    else:
        #开始计算根号D的连分数形式
        P=0
        Q=1
        a=int(sboot)
        #第0和第1个渐进分数
        p=[1,a]#分子
        q=[0,1]#分母
        while p[1]**2-number*(q[1]**2)!=1:
            #中间变量
            P=a*Q-P
            Q=(number-P**2)/Q
            a=int((int(sboot)+P)//Q)
            #渐进分数
            pp=a*p[1]+p[0]#分子
            qq=a*q[1]+q[0]#分母
            #存储
            p=[p[1],pp]
            q=[q[1],qq]
        return [p[1],number,q[1]]
#开始计算
x=0
d=0
for ipell in range(1001):
    result=GetPell(ipell)
    if len(result)==3:#排除完全平方的数
        if x<result[0]:#选择最小值
            x=result[0]
            d=result[1]
        elif x==result[0] and d<result[1]:#一样的X值，选择D最小的值
            d=result[1]

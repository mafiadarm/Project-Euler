#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
扑克手牌
在扑克游戏中，玩家的手牌由五张牌组成，其等级由低到高分别为：
单牌：牌面最大的一张牌。
对子：两张牌面一样的牌。
两对：两个不同的对子。
三条：三张牌面一样的牌。
顺子：五张牌的牌面是连续的。
同花：五张牌是同一花色。
葫芦：三条带一个对子。
四条：四张牌面一样的牌。
同花顺：五张牌的牌面是连续的且为同一花色。
同花大顺：同一花色的10、J、Q、K、A。
牌面由小到大的顺序是：2、3、4、5、6、7、8、9、10、J、Q、K、A。
如果两名玩家的手牌处于同一等级，那么牌面较大的一方获胜；例如，一对8胜过一对5（参见例1）；如果牌面相同，例如双方各有一对Q，那么就比较玩家剩余的牌中最大的牌（参见例4）；如果最大的牌相同，则比较次大的牌，依此类推。
考虑以下五局游戏中双方的手牌：

手牌	    玩家1	                            玩家2	            胜者
1	红桃5 草花5 黑桃6 黑桃7 方片K	草花2 黑桃3 黑桃8 方片8 方片10	玩家2
 	        一对5	                             一对8
2	方片5 草花8 黑桃9 黑桃J 草花A	草花2 草花5 方片7 黑桃8 红桃Q	玩家1
 	        单牌A	                              单牌Q
3	方片2 草花9 黑桃A 红桃A 草花A	方片3 方片6 方片7 方片10 方片Q	玩家2
 	        三条A	                            同花方片
4	方片4 黑桃6 红桃9 红桃Q 草花Q	方片3 方片6 红桃7 方片Q 黑桃Q	玩家1
 	        一对Q	                            一对Q
 	        最大单牌9	                        最大单牌7
5	红桃2 方片2 草花4 方片4 黑桃4	草花3 方片3 黑桃3 黑桃9 方片9	玩家1
 	         葫芦	                             葫芦
 	        （三条4）	                        （三条3）

在这个文本文件poker.txt中，包含有两名玩家一千局的手牌。每一行包含有10张牌（均用一个空格隔开）：前5张牌属于玩家1，后5张牌属于玩家2。你可以假定所有的手牌都是有效的（没有无效的字符或是重复的牌），每个玩家的手牌不一定按顺序排列，且每一局都有确定的赢家。
其中有多少局玩家1获胜？

分析：
# 用模型获取分数
单牌：花色不同，数字不同，数字不相连
对子：花色不同，数字有相同，len(set)=4
两对：花色不同，数字有两个相同，len(set)=3
三条：花色不同，数字有三个相同，len(set)=3
顺子：花色不同，数字连续
同花：花色相同，数字不同
葫芦：花色不同，数字有三个相同，剩下两个也相同，len(set)=2
四条：花色不同，数字有四个相同，len(set)=2
同花顺：花色同，数字连续，[-1]!=14
同花大顺：花色，顺序，[-1]=14

# 模型判断条件
sorted("")=[]

花色不同 len(set([]))>1
花色相同 len(set([]))=1

数字不相连 ↓=False
数字相连 [-1]-[0]=4 and sum[int(i) for i in []]/5=[2]

数字不同 len(set([]))=5
数字有相同，只有2个相同 len(set([]))=4
数字有相同，有2个2个相同 len(set([]))=3
数字有相同，有3个相同，剩下两个不相同 len(set([]))=3
数字有相同，有3个相同，剩下两个也相同 len(set([]))=2
数字有相同，有4个相同 len(set([]))=2

# 算分方案

单牌：最大数*10**0
对子：对子的一张牌面*10**1
两对：最大对子的一张牌面数*10**2
三条：三条的一张牌面数*10**3
顺子：顺子最大的那张牌面*10**4
同花：最大数*10**5
葫芦：三条的一张牌面数*10**6
四条：四条的最大牌面*10**7
同花顺：最大的牌面*10**8+花色值
同花大顺：花色值*10**9
"""
def poker_soccer(poker_num, poker_fol):  # 判断规则详见054
    from collections import Counter
    point_dict = {j: i for i, j in enumerate("23456789abcdeSHDC", 2)}
    for char, letter in (("A", "e"), ("K", "d"), ("Q", "c"), ("J", "b"), ("T", "a")):
        poker_num = poker_num.replace(char, letter)

    lis = sorted(poker_num)  # 牌面
    lip = sorted(poker_fol)  # 花色
    poker_num_count = Counter(lis)
    if len(set(lip)) == 1:
        if point_dict.get(lis[-1]) - point_dict.get(lis[0]) == 4 and sum(
                [point_dict.get(i) for i in lis]) == point_dict.get(lis[2]) and point_dict.get(lis[-1]) == 14:
            return point_dict.get(lip[0]) * 10 ** 9
        elif point_dict.get(lis[-1]) - point_dict.get(lis[0]) == 4 and sum(
                [point_dict.get(i) for i in lis]) == point_dict.get(lis[2]):
            return point_dict.get(lis[-1]) * 10 ** 8 + point_dict.get(lip[0])
        else:
            return point_dict.get(lis[-1]) * 10 ** 5
    elif len(set(lip)) > 1:
        if point_dict.get(lis[-1]) - point_dict.get(lis[0]) == 4 and sum(
                [point_dict.get(i) for i in lis]) == point_dict.get(lis[2]):
            return point_dict.get(lis[-1]) * 10 ** 4
        else:
            return point_dict.get(lis[-1])
    else:
        try:
            four = max([i for i in poker_num_count if poker_num_count.get(i) == 4])
            return point_dict.get(four) * 10 ** 7
        except ValueError:
            try:
                three = max([i for i in poker_num_count if poker_num_count.get(i) == 3])
                try:
                    max([i for i in poker_num_count if poker_num_count.get(i) == 2])
                    return point_dict.get(three) * 10 ** 6
                except ValueError:
                    return point_dict.get(three) * 10 ** 3
            except ValueError:
                two = max([i for i in poker_num_count if poker_num_count.get(i) == 2])
                one = max([i for i in poker_num_count if poker_num_count.get(i) == 1])
                if min([i for i in poker_num_count if poker_num_count.get(i) == 2]) != two:
                    return point_dict.get(two) * 10 ** 2 + point_dict.get(one)
                else:
                    return point_dict.get(two) * 10 ** 1 + point_dict.get(one)

def xxx():
    win = 0
    with open(r"p054_poker.txt", "r") as rr:
        for i in range(1000):
            ll = rr.readline()
            p1_poker_num = ll[0] + ll[3] + ll[6] + ll[9] + ll[12]
            p1_poker_fol = ll[1] + ll[4] + ll[7] + ll[10] + ll[13]
            p2_poker_num = ll[15] + ll[18] + ll[21] + ll[24] + ll[27]
            p2_poker_fol = ll[16] + ll[19] + ll[22] + ll[25] + ll[28]
            if poker_soccer(p1_poker_num, p1_poker_fol) > poker_soccer(p2_poker_num, p2_poker_fol):
                win += 1
    return win
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
大富翁几率
大富翁游戏的标准棋盘大致如下图所示：
GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2										C1
T2										U1
H1										C2
CH3										C3
R4										R2
G3										D1
CC3										CC2
G2										D2
G1										D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP
玩家从标记有“GO”的方格出发，掷两个六面的骰子并将点数和相加，作为本轮他们前进的步数。如果没有其它规则，那么落在每一格上的概率应该是2.5%。但是，由于“G2J”（入狱）、“CC”（宝箱卡）和“CH”（机会卡）的存在，这个分布会有所改变。
除了落在“G2J”上，或者在“CC”或“CH”上抽到入狱卡之外，如果玩家连续三次都掷出两个相同的点数，则在第三次时将会直接入狱。
游戏开始时，“CC”和“CH”所需的卡片将被洗牌打乱。当一个玩家落在“CC”或“CH”上时，他们从宝箱卡和机会卡的牌堆最上方取一张卡并遵循指令行事，并将该卡再放回牌堆的最下方。宝箱卡和机会卡都各有16张，但我们只关心会影响到移动的卡片，其它的卡片我们都将无视它们的效果。
宝箱卡 (2/16 张卡):
回到起点“GO”
进入监狱“JAIL”
机会卡 (10/16 张卡):
回到起点“GO”
进入监狱“JAIL”
移动到“C1”
移动到“E3”
移动到“H2”
移动到“R1”
移动到下一个“R”（铁路公司）
移动到下一个“R”
移动到下一个“U”（公共服务公司）
后退三步
这道题主要考察掷出骰子后停在某个特定方格上的概率。显然，除了停在“G2J”上的可能性为0之外，停在“CH”格的可能性最小，因为有5/8的情况下玩家会移动到另一格。我们不区分是被送进监狱还是恰好落在监狱“JAIL”这一格，而且不考虑需要掷出两个相同的点数才能出狱的要求，而是假定进入监狱的第二轮就会自动出狱。
从起点“GO”出发，并将方格依次标记00到39，我们可以将这些两位数连接起来表示方格的序列。
统计学上来说，三个最有可能停下的方格分别是“JAIL”（6.24%）或方格10，E3（3.18%）或方格24以及“GO”（3.09%）或方格00。这三个方格可以用一个六位数字串表示：102400。
如果我们不用两个六面的骰子而是用两个四面的骰子，求出三个最有可能停下的方格构成的数字串。
"""
import random

def draw_cc(position):  # 084
    cc_map = {0: 0, 1: 10}
    card_num = random.randint(0, 15)
    if card_num in cc_map:
        return cc_map[card_num]
    return position

def draw_ch(position):  # 084
    ch_map = {0: 0, 1: 10, 2: 11, 3: 24, 4: 39, 5: 5}
    card_num = random.randint(0, 15)
    if card_num in ch_map:
        return ch_map[card_num]
    if card_num == 6 or card_num == 7:
        if position < 5:
            return 5
        if position < 15:
            return 15
        if position < 25:
            return 25
        if position < 35:
            return 35
        return 5
    if card_num == 8:
        if position < 12:
            return 12
        if position < 28:
            return 28
        return 12
    if card_num == 9:
        if position == 36:
            return draw_cc(33)
        return position - 3
    return position

def xxx():
    import random
    position = 0
    rolls = 100000
    square_count_map = {}
    for i in range(40):
        square_count_map[i] = 0
    doubles_count = 0

    for i in range(rolls):
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)
        if d1 == d2:
            doubles_count += 1
        else:
            doubles_count = 0
        if doubles_count == 3:
            position = 10
            doubles_count = 0
        else:
            position += (d1 + d2)
            position %= 40
        if position == 30:
            position = 10
        elif position in [2, 17, 33]:
            position = draw_cc(position)
        elif position in [7, 22, 36]:
            position = draw_ch(position)
        square_count_map[position] += 1

    for square in range(40):
        print(square, round(100 * square_count_map[square] / float(rolls), 4))

    print(sorted(square_count_map, key=lambda x: square_count_map[x])[:-4:-1])

print(xxx())
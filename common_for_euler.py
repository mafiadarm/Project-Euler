# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_17_2018  16:08
   File Name:      /GitHub/randomQuizGenerator
   Creat From:     PyCharm
- - - - - - - - - - - - - - -
   Description:    常用函数
   算法考虑：
                   使用公式
                   使用规律
                   使用点阵
                   使用倍数处理
                   使用递归
                   排序方法
==============================
"""
__author__ = 'Loffew'


def __init__():
    pass


def per_com(num_range, amount):
    from math import factorial
    per = int(factorial(num_range) / factorial(num_range - amount))
    com = int(factorial(num_range) / (factorial(amount) * factorial(num_range - amount)))
    chara_per = "If use permutations {}".format(per)
    chara_com = "If use combinations {}".format(com)
    print(chara_per.ljust(30, " "))
    print(chara_com.ljust(30, " "))


def isPrime2(n):  # 短除法，验证列表内的数字是否是质数
    if int(n ** 0.5) ** 2 != n and n != 1 and n != 0:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def isPrime_factor(n):  # 列出所有质因子，如果传1进去，列表会是空值
    li, f = [], 2
    while f * f <= n:
        while not n % f:
            li.append(f)
            n //= f
        f += 1
    if n != 1:
        li.append(n)
    return li


def common_Divisor(x, y, z, li):  # 最小公倍数 详见 005
    while y:
        x, y = y, x % y
    return li.append(z / x * li[-1] / x * x)


def gys(x, y):  # 求x,y的最大公约数  可以用math.gcd()
    while y:
        x, y = y, x % y
    return x


def cycles(x):  # 循环节
    a, lis = 1, []
    while a % x not in lis:  # 验证余数的重复
        lis.append(a % x)
        a *= 10
    if not lis[-1]:
        return 0  # 用0占位，同时把末尾是0的去掉
    else:
        return len(lis) - lis.index(a % x)  # -lis.index(a%x)是为了清理300/3=100这种数


def is_palindrome(n):  # 回文检测
    return str(n) == str(n)[::-1]


def prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表


def not_prime_list(n, f=0):  # 返回N以内所有的非素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if not v and k >= f]  # 返回处理后的列表


def replace_same_digital(original_number, replace_number_list):  # 传入一个数和一个替换重复数的数字列表
    import re
    replaced = {}
    for replace_number in replace_number_list:
        # ?=表示零宽断言，.表示匹配任意字符，*表示数量任意，/1表示重复
        replication_list = set(re.findall(r"(?=(.).*\1)", str(original_number)))
        for sre_num in replication_list:
            if sre_num in replaced:
                replaced[sre_num].add(int(str(original_number).replace(sre_num, str(replace_number))))
            else:
                replaced[sre_num] = {int(str(original_number).replace(sre_num, str(replace_number)))}
    return replaced  # 返回标记有重复数字为key和修改好的重复数字集合为value的字典


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


def x_shape_list(lamb_da, max_range, min_range=1):  # lamb_da= lambda x:公式 范例见061
    lis = []
    i = 0
    while True:
        i += 1
        n = lamb_da(i)
        if n < min_range:
            continue
        if n >= max_range:
            return lis
        lis.append(n)


def divide_count(num, dig, tmp_dict):  # num写成+dig的所有方式 见076
    if num == dig or dig == 1:
        return 1
    elif dig > num:
        return 0
    else:
        if tmp_dict.get(str(num) + ',' + str(dig)) is None:
            tmp = divide_count(num - 1, dig - 1, tmp_dict) + divide_count(num - dig, dig, tmp_dict)  # 递归
            tmp_dict[str(num) + ',' + str(dig)] = tmp
            return tmp
        else:
            return tmp_dict.get(str(num) + ',' + str(dig))

def draw_cc(position):  # 084
    import random
    cc_map = {0: 0, 1: 10}
    card_num = random.randint(0, 15)
    if card_num in cc_map:
        return cc_map[card_num]
    return position


def draw_ch(position):  # 084
    import random
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

def getpsn(num, sump, product, start, maxk, n):  # 088 用递归直接处理
    """
    对于一个数num   因式分解后因子个数为 product   这些因子的和为sump
    则需要添加的1 的个数为 num - sump，所以size k = num - sump + product
    """
    k = num - sump + product
    if k < maxk:
        if num < n[k]:
            n[k] = num
        for i in range(start, maxk // num * 2):  # 控制num<=2*maxk
            getpsn(num * i, sump + i, product + 1, i, maxk, n)
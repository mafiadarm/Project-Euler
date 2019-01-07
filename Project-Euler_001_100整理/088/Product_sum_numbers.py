#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
积和数
若自然数N能够同时表示成一组至少两个自然数{a1, a2, … , ak}的积和和，也即N = a1 + a2 + … + ak = a1 × a2 × … × ak，则N被称为积和数。
例如，6是积和数，因为6 = 1 + 2 + 3 = 1 × 2 × 3。
给定集合的规模k，我们称满足上述性质的最小N值为最小积和数。当k = 2、3、4、5、6时，最小积和数如下所示：
k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
因此，对于2≤k≤6，所有的最小积和数的和为4+6+8+12 = 30；注意8只被计算了一次。
已知对于2≤k≤12，所有最小积和数构成的集合是{4, 6, 8, 12, 15, 16}，这些数的和是61。
对于2≤k≤12000，所有最小积和数的和是多少？

统计流程：
用set k向上增加，数字从头开始遍历，k为组成元素个数
算法：
    分解质因子，从大往小连续相乘，或者某两个或多个相乘后，用1补位
    因子相加，用1补位，直到等于num
    各个因子组合相加后，被源数字减去再加上组合内元素个数即是k
    要考虑16 [2,2,2,2] 出现 [4,4] 的情况，
    所以要构造字典，小的数字的因子构造，在大的数字构造的时候，去取小数字的构造的组合，并补充进去
"""

# 获得一个数除去本身和1之外的含有2个因子的组合的列表，第一个因子为质因子，后面一个因子待用
def two_factor(num):
    result_list = []
    for divisor_test in range(2, int(num ** 0.5) + 1):
        if not num % divisor_test:
            result_list.append([divisor_test, num // divisor_test])
    return result_list

def creat_factor_dict(cap):
    # 把每一个数分解成两个因子的字典，第一个为最小质因子，把第二个数作为key到字典查
    # 因为是被分解的因子，所以前面必然有对应的组合
    factor_dict = {i:two_factor(i) for i in range(cap)}

    # 构造一个数的所有因子各种组合及乘积组合
    for key in factor_dict:
        if not factor_dict[key]: continue

        factor_container = []
        for divisor_list in factor_dict[key]:
            count_element = len(divisor_list)  # 统计这个列表有多少个元素
            get_divisor_list_of_key = factor_dict.get(divisor_list[-1])  # 以最后这个元素为key去搜寻这个key值的因子组合
            if get_divisor_list_of_key:  # 如果这个value不为空
                for get_divisor_list in get_divisor_list_of_key:  # 则遍历这个key的所有组合（可能多个）
                    cc = divisor_list[:count_element-1] + get_divisor_list  # 把这个数字变成对应key的组合值（挨着挨着的变，所以要用count_element）
                    factor_container.append(cc)  # 每变一个，增加一个进容器

        factor_dict[key] += factor_container  # 把新增的组合通过容器补充进原来的列表
    return factor_dict  # key里面可能会有很多重复的组合

def xxx(ask=None):
    ask = 100 if not ask else ask
    answer_list = [0] * (ask+1)
    answer_list[0], answer_list[1] = True, True

    for key, values in creat_factor_dict(ask*2).items():  # 构造2倍的字典以供查询
        for divisor_list in values:
            k = key - sum(divisor_list) + len(divisor_list)
            if k > ask: continue  # 如果超过边界则重新取值

            if answer_list[k]: answer_list[k] = key if key < answer_list[k] else answer_list[k]  # 取小的那个
            else: answer_list[k] = key

            if 0 not in answer_list: return sum(set(answer_list))-1  # True会被计算为1

    return "not enough dict"
print(xxx(12000))
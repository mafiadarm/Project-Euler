#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
素数数字替换
将两位数*3的第一个数字代换为任意数字，在九个可能值中有六个是素数：13、23、43、53、73和83。
将五位数56**3的第三和第四位数字代换为相同的任意数字，就得到了十个可能值中有七个是素数的最小例子，
这个素数族是：56003、56113、56333、56443、56663、56773和56993。56003作为这一族中最小的成员，也是最小的满足这个性质的素数。
通过将部分数字（不一定相邻）代换为相同的任意数字，有时能够得到八个素数，求满足这一性质的最小素数。

分析：
按10的指数扩大范围的找
构造素数集合，并过滤掉所有没重复数字的素数
再对比剩下的数字：
    思路1：以源素数为原型，把重复的数字替换成1-9，并把构建出来的返回集合去验证，如果成立的有8个即为答案
"""
import re

def replace_same_digital(original_number, replace_number_list):  # 传入一个数和一个替换重复数的数字列表
    replaced = {}
    for replace_number in replace_number_list:
        # ?=表示零宽断言，.表示匹配任意字符，*表示数量任意，/1表示重复1次以上
        replication_list = set(re.findall(r"(?=(.).*\1)", str(original_number)))
        for sre_num in replication_list:
            # 因为可能有多个重复的数字，所以构建字典
            if sre_num in replaced:
                replaced[sre_num].add(int(str(original_number).replace(sre_num, str(replace_number))))
            else:
                replaced[sre_num] = {int(str(original_number).replace(sre_num, str(replace_number)))}
    return replaced  # 返回标记有重复数字为key和修改好的重复数字集合为value的字典

def xxx(num=100):
    while True:
        num *= 10
        bool_list = [True] * num  # 构建一个只有True和False的bool表，用于打标记
        bool_list[0], bool_list[1] = False, False
        for i, prime in enumerate(bool_list):
            if prime:
                for j in range(i * i, num, i):  # 用跳距消除能被整除的数
                    bool_list[j] = False

        # 取数范围
        start = int(num/10)
        # 用标记构建一个素数集合
        prime_range = [k for k, prime_num in enumerate(bool_list[start:num], start) if prime_num and len(set(str(k))) < len(str(k))]

        for the_num in prime_range:  # 用素数集合
            # 因为有可能重复数字是0，所以范围是range(10)
            check_dict = replace_same_digital(the_num, range(10))  # 返回构建好准备测试的字典
            for value in check_dict.values():  # 取值
                # 遍历值，回bool表，用索引验证
                check = [n for n in value if bool_list[n] and len(str(n)) == len(str(the_num))]  # 如果位数前面是0，则会缩位，所以必须比较位数
                if len(check) == 8:
                    return the_num, check

print(xxx())


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
重排平方数
将单词CARE中的四个字母依次赋值为1、2、9、6，我们得到了一个平方数：1296 = 36^2。
神奇的是，使用同样的数字赋值，重排后的单词RACE同样构成了一个平方数：9216 = 96^2。
我们称CARE和RACE为重排平方单词对，同时规定这样的单词对不允许有前导零或是不同的字母赋相同的值。
在这个16K的文本文件words.txt（右击并选择“目标另存为……”）中包含了将近两千个常见英文单词，
找出所有的重排平方单词对（一个回文单词不视为它自己的重排）。
重排平方单词对所给出的最大平方数是多少？
注意：所有的重排单词必须出现在给定的文本文件中。

分析：
字母数量决定了在这个位数范围内的所有平方数，比如4个字母的单词，就对应4位数内的所有平方数
不允许有前导零或是不同的字母赋相同的值
"""

def get_pair_list():
    # 整理下文本
    with open("p098_words.txt") as ww:
        all_word = ww.readlines()[0].replace('"',"").split(",")

    # 重排字母配对
    pair_list = []
    count_words = len(all_word)
    for target_index in range(count_words - 1):
        for test_index in range(target_index, count_words):
            target_word, test_word = all_word[target_index], all_word[test_index]
            if sorted(target_word) == sorted(test_word) and target_word != test_word:
                pair_list.append([target_word, test_word])

    return pair_list

# 根据字母长度获得该长度范围内的完全平方数
def get_square_num_list(figures):
    if figures == 1:
        return [1, 4, 9]
    # 用四舍五入和限定范围的方式保证位数的准确性
    square_list = [num**2 for num in range(round((10**(figures-1))**0.5), round((10**figures)**0.5)+1) if 10**(figures-1)<num**2<10**figures]
    return square_list

# 根据字典，从单词排列获得数字
def word_get_num(test_dict, word):
    digit = ""
    for letter in word:
        digit += test_dict.get(letter, "")
    return int(digit)

# 按照规则判断数字和word是否对应
def check_rule(number, word):
    num_word_mapping = {}
    str_num = str(number)
    # 用数字做key来去掉有相同的值的字母
    for index in range(len(word)):
        if index not in num_word_mapping:
            num_word_mapping[str_num[index]] = word[index]
    # 根据字典反写数字与原来数字是否一样
    num_word_mapping = {v: k for k, v in num_word_mapping.items()} # 反转下字典，用来构造数字
    if word_get_num(num_word_mapping, word) == number:
        return num_word_mapping

# 根据配对的单词和平方数，求配对单词的对应数字
def get_num(word_list, squares_list):
    target_word, test_word = word_list[0], word_list[1]
    container = []
    for square_num in squares_list:
        # 已经保证了数字和单词的位数是匹配的
        word_num_dict = check_rule(square_num, target_word)  # 判断是否匹配且无不同字母赋相同的值
        if word_num_dict:  # 如果有值，则无不同字母赋相同的值（符合规则）
            test_word_num = word_get_num(word_num_dict, test_word)  # 按test_word造一个数字
            if test_word_num in squares_list:  # 如果这个数也是完全平方数
                print('%s ==> %s' %([target_word, test_word], [square_num, test_word_num]))
                container.append(max([square_num, test_word_num]))  # 输出结果
                return container
    return []

def xxx():
    result = []
    for pair_list in get_pair_list():  # 从单词列表中遍历
        squares_list = get_square_num_list(len(pair_list[0]))  # 生成相同位数的平方数列表
        number_list = get_num(pair_list, squares_list)  # 用单词和平方数列表进行匹配
        if number_list:  # 匹配成功，返回能匹配的数字列表
            result.append(max(number_list))  # 取最大的放到总列表
    return max(result)  # 返回最大值

print(xxx())
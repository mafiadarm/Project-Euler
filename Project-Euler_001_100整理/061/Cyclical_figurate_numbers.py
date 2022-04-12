#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
循环的多边形数
三角形数、正方形数、五边形数、六边形数、七边形数和八边形数统称为多边形数。它们分别由如下的公式给出：
三角形数	P3,n=n(n+1)/2	1, 3, 6, 10, 15, …   n = (num*2+0.5**2)**0.5-0.5
正方形数	P4,n=n2	1, 4, 9, 16, 25, …           n = num**0.5
五边形数	P5,n=n(3n−1)/2	1, 5, 12, 22, 35, …  n = (1+(1+num*4*3*2)**0.5)/6
六边形数	P6,n=n(2n−1)	1, 6, 15, 28, 45, …  n = (1+(1+4*2*num)**0.5)/4
七边形数	P7,n=n(5n−3)/2	1, 7, 18, 34, 55, …  n = (3+(9+4*5*2*num)**0.5)/10
八边形数	P8,n=n(3n−2)	1, 8, 21, 40, 65, …  n = (2+(4+4*3*num)**0.5)/6
由三个4位数8128、2882、8281构成的有序集有如下三个有趣的性质。
这个集合是循环的，每个数的后两位是后一个数的前两位（最后一个数的后两位也是第一个数的前两位）。
每种多边形数——三角形数（P3,127=8128）、正方形数（P4,91=8281）和五边形数（P5,44=2882）——在其中各有一个代表。
这是唯一一个满足上述性质的4位数有序集。

存在唯一一个包含六个4位数的有序循环集，每种多边形数——三角形数、正方形数、五边形数、六边形数、七边形数和八边形数——在其中各有一个代表。
求这个集合的元素和。

分析：
确定是在4位数里面找
可以构造每个多边形数在同等位数的集合，再遍历实现，但是这样就有6个指数的量
前两位=后两位 可以用num % 100 == num // 100 或者 str(num)[:2]==str(num)[2:]表达
因为是在确定的元素里面找，一定能找到，所以选择用递归查询
"""
from itertools import count
import copy

def x_shape_list(lambda_func, max_range, min_range=1):  # lambda_func= lambda x:公式 范例见061
    # 构造在一个范围内的多边形数的集合
    polygons_list = []
    for i in count(1):
        polygons = lambda_func(i)
        if polygons < min_range:  # 不取小于此值的
            continue
        if polygons > max_range:  # 超过此值说明构造完成
            return polygons_list
        
        c = str(polygons)  # 转换为str,后面好比较
        if c[2] == "0":  # 第3位肯定不为0
            continue
        polygons_list.append(c)
        
min_num=1000
max_num=10000

p3 = x_shape_list(lambda n: int(n*(n+1)/2), max_num, min_num)
p4 = x_shape_list(lambda n: n*n, max_num, min_num)
p5 = x_shape_list(lambda n: int(n*(3*n-1)/2), max_num, min_num)
p6 = x_shape_list(lambda n: n*(2*n-1), max_num, min_num)
p7 = x_shape_list(lambda n: int(n*(5*n-3)/2), max_num, min_num)
p8 = x_shape_list(lambda n: n*(3*n-2), max_num, min_num)

# 因为p8是最少的,所以从P8开始找
# 需要用 p3-p8的列表, 需要一个寻找的flag列表[Flase, Flase, Flase, ..., 已经寻找到的数字]
# 需要解决有相同前2位的数字问题(或者解决重复问题)
# 经过验证,P8没有前2位相同的数字 len(p8)==len(set([i[:2] for i in p8]))

p_dict = {
    'p8': p8,
    'p7': p7,
    'p6': p6,
    'p5': p5,
    'p4': p4,
    'p3': p3
}

def find_num_group(p_dict, p_key, num, result):
    """
        用回调函数不断匹配数字
    """
    result.append(num)  # 加入第一个数字
    new_dict = copy.deepcopy(p_dict)  # copy以备用[保留原来的,如果回调可以保证之前的存在]
    del new_dict[p_key]  # 去掉自身再往下匹配
    
    if not new_dict:  # 如果列表中有6个数字了
        if result[0][:2] == result[-1][2:]:  # 且第一个数和最后一个数能匹配头尾[和寻找时匹配相反]
            print(result)
        else:
            del result[-1]  # 说明没匹配上,删除最后一个数字,回调后重新匹配
    
    else:
        for k in new_dict:  # 遍历剩下的字典中的key
            for test in new_dict[k]:  # 遍历key的值,用于比较
                if num[2:] == test[:2]:  # 如果[目标数字的后面2位=匹配的数字的前面]能头尾匹配
                    find_num_group(new_dict, k, test, result)  # 按照剩下的继续往下传
                
        del result[-1]  # 说明第一个数字和所有的都不匹配,删除后重新匹配


for f_num in p_dict['p8']:  # 遍历这个key中所有的数字,作为对比使用
    find_num_group(p_dict, 'p8', f_num, [])

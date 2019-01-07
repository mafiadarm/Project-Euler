#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find(t):
    return sum([int(ii)**5 for ii in str(t)])


# 模糊查找，一个N位数的各位数字的5次幂相加依然是N位数，按位数最高值找出上限，从100位开始
c = 1
request = 9
while 1:
    request += 9 * 10 ** c
    test = find(request)
    if test//10**c == 0:  # 因为数字小，所以直接用str拆
        break
    else: c += 1

# 这里看出n的上限为6，也就是999999，那么999999的计算结果为：
upper_limit = find(request//10)

# 遍历这个范围内所有数，进行验证
result = []
for num in range(2, upper_limit):
    if find(num) == num:
        result.append(num)

print(sum(result), result)

# 更快的方式(用组合遍历会更快)
from time import time
import itertools
def euler030():
    l_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l_result = []
    #粗略算一下，只能是3-6位数之间
    for i in range(3, 7):
        for each in itertools.combinations_with_replacement(l_nums, i):  # 生成组合,用组合来遍历要比数字直接遍历快很多
            n_sum = sum([x ** 5 for x in each])  # 计算组合各位数5次幂之和

            t1 = list(each)  # 4,1,5,0
            t1.sort()
            t2 = [int(n) for n in list(str(n_sum))]  # 再把和转成单独的数字用于排序
            t2.sort()
            if t1 == t2:
                l_result.append(n_sum)

    print(sum(l_result))

start = time()
euler030()
print('cost %.6f sec' % (time() - start))
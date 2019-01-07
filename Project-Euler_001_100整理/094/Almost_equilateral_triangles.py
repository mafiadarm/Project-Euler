#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
几乎等边的三角形
可以证明，不存在边长为整数的等边三角形其面积也是整数。但是，存在几乎等边的三角形 5-5-6，其面积恰好为12。
我们定义几乎等边的三角形是有两条边一样长，且第三边与这两边最多相差1的三角形。
对于所有边长和面积均为整数且周长不超过十亿(1,000,000,000)的三角形，求其中几乎等边的三角形的周长之和。

分析：
    用python的math.sqrt（）配合海伦公式算面积的时候，有一个被忽略的问题，就是大数据的情况下，python的计算精度问题。
    三角形（302828,302828,302829）就是一个很好的例子。
    import math
    def area(a,b,c):
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    print(area(302828,302828,30282))
    答案是39709429597.0。但实际上，该三角形底边上的高为262256.45230146387，是个无理数，面积不会是真正的“整数”，这只不过是被python四舍五入了。
    所以，这道题的关键在于
    （1）避开sqrt（）函数直接作用于大的数，
    （2）将计算次数从上亿次降下来。

    假定第三边大于三角形的两腰，那么设三边为m，m，m+1。那么根据海伦公式，
    p=(m+m+m+1)/2=(3m+1)/2
    S= √((3m+1)(m+1)(m+1)(m-1)/16)
    所以，m必须是奇数才可以。设m=2k+1，那么代入，有
    S=（k+1）√(k（3k+2）)
    显然，k与3k+2没有大于2的公因子。
            假设两者互质，那么k和3k+2 都必须同时是完全平方数才能确保面积是整数，可以设k=x^2，检测3x^2+2是否为整数。这时，三角形的三边为2*x^2+1, 2*x^2+1,2*x^2+2，根据边长范围可得，x不大于12910。
            假设两者不互质，那么设k=2y，那么
    S=2（2y+1）√(y（3y+1）)
    Y与3y+1必然互质，所以y和（3y+1）必须是完全平方数，设y = x^2，检测 3*x^2 + 1 是否为完全平方数即可。此时，三角形的三边为 4^x2+1, 4^x2+1, 4^x2+2，x不大于9129。
    同样的，假定第三边小于三角形的两腰时，可以得到后面的结论：
        三角形三边为2*x^2-1, 2*x^2-1,2*x^2-2, x不大于12910，3*x^2-2须为完全平方数。
        三角形三边为4*x^2-1, 4*x^2-1,4*x^2-2, x不大于9129，3*x^2-1须为完全平方数。
"""

import math

def xxx():
    pri_sum = 0

    # case1
    for i in range(1, int(math.sqrt(10 ** 9 / 3 / 2)) + 1):
        test = math.sqrt(3 * i * i + 2)
        if round(test) == test:
            pri_sum += sum([2 * i * i + 1, 2 * i * i + 1, 2 * i * i + 2])
    # case2
    for i in range(1, int(math.sqrt(10 ** 9 / 3 / 4)) + 1):
        test = math.sqrt(3 * i * i + 1)
        if round(test) == test:
            pri_sum += sum([4 * i * i + 1, 4 * i * i + 1, 4 * i * i + 2])
    # case3
    for i in range(2, int(math.sqrt(10 ** 9 / 3 / 2)) + 1):
        test = math.sqrt(3 * i * i - 2)
        if round(test) == test:
            pri_sum += sum([2 * i * i - 1, 2 * i * i - 1, 2 * i * i - 2])
    # case4
    for i in range(1, int(math.sqrt(10 ** 9 / 3 / 4)) + 1):
        test = math.sqrt(3 * i * i - 1)
        if round(test) == test:
            pri_sum += sum([4 * i * i - 1, 4 * i * i - 1, 4 * i * i - 2])

    return pri_sum

def other():
    # Pell方程x^2 - 3y^2 = 1， 初始解为(2, 1)
    x = 2
    y = 1
    summ = 0
    while 1:
        ynum = 2 * y + 1 * x
        xnum = x * 2 + 3 * y * 1
        x = xnum
        y = ynum
        # 第一种(a, a+1, a+1)
        # 化为((3a+4)/2)^2-3h^2=1，利用Pell方程
        if 2 * xnum - 2 < 1e9:  # 周长限制
            if (2 * xnum - 4) / 3 % 2 == 0:  # 判断边长为整数
                squre = ynum * (xnum - 2) / 3
                if int(squre) - squre == 0:  # 面积为整数
                    summ += 2 * xnum - 2
        else:
            break
        # 第二种(a, a-1, a-1)
        # 化为((3a-4)/2)^2-3h^2=1，利用Pell方程
        if 2 * xnum + 2 < 1e9:  # 周长限制
            if (2 * xnum + 4) / 3 % 2 == 0:  # 判断边长为整数
                squre = ynum * (xnum + 2) / 3
                if int(squre) - squre == 0:  # 面积为整数
                    summ += 2 * xnum + 2
        else:
            break
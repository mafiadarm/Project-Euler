# -- coding = utf-8 -- version 3.6
# Project Euler No.1
# 第一次体会到算法的差别有多大
import common_for_euler
"""
3的倍数和5的倍数
如果我们列出10以内所有3或5的倍数，我们将得到3、5、6和9，这些数的和是23。

求1000以内所有3或5的倍数的和。

看成是一个三角形排列

            3
           3 3
          3 3 3
         3 3 3 3
这样就成了求梯形面积（三角形+顶） 数值范围整除3是多少，就是多少层（高、底）计算出多少个3，然后在乘以3
def suma(xrange,num): #效率较低的方法
    return sum(list(filter(lambda x:x%num == 0,range(1,xrange))))

def sumb(xrange=0,num=0): #省略大部分遍历时间
    return (num+num*(xrange//num))*(xrange//num)/2
"""


def No_1_Sums(xrange=1000, x=3, y=5):  # 减去被覆盖那部分
    return (x + x * (xrange // x)) * (xrange // x) / 2 + (y + y * (xrange // y)) * (xrange // y) / 2 - (
            x * y + x * y * (xrange // (x * y))) * (xrange // (x * y)) / 2


# Project Euler No.2
'''
偶斐波那契数
斐波那契数列中的每一项都是前两项的和。由1和2开始生成的斐波那契数列前10项为：

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
考虑该斐波那契数列中不超过四百万的项，求其中为偶数的项之和。

[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
求偶数项之和，我们看到第二个+第四个=第五个-1（2+5=8-1）、（2+5+13=21-1）由此推断小于400W的和实际等于400w这个数前或后最近那个数的奇数-1
'''


def No_2_Fibla(xrange=4000000, x=1, y=2):
    li = [1, 2]
    while y < xrange:
        x, y = y, x + y
        li.append(y)
    return [li[-1] - 1 if li.index(li[-1]) % 2 == 0 else li[-2] - 1][0]


# Project Euler No.3
'''
最大质因数
13195的所有质因数为5、7、13和29。

600851475143最大的质因数是多少？

假如一个数N是合数,它有一个约数a,a×b=N
则a、b两个数中必有一个大于或等于根号N,一个小于或等于根号N.
因此,只要小于或等于根号N的数（1除外）不能整除N,则N一定是素数.
如果值是：19874589103 这种大型质数，要从1开始遍历，就会很慢,用以下函数秒出结果
def pro(n=600851475143):
    f = 2
    while f*f <= n:
        while not n%f:
            n //= f
        f += 1
    print(n)
但是平方数或者平方数相乘就无法算
'''
'''
def No_3_IsPrime(num=600851475143):
    li = []
    for i in range(2,num):
        if num%i == 0: #把所有能除尽的数加入列表
            if i < num**0.5:
                li.append(i)
                li.append(int(num/i))
            elif i == num**0.5:
                print("这是%s平方"%int(num**0.5))
                li.append(i)
                return isPrime1(li)
            else:
                return isPrime1(li)
    print("这是一个质数")

def isPrime1(n):
    ls = []
    for j in n:
        if isPrime2(j):
           ls.append(j)#把是质数的因子加入列表
    return print("它的最大质因数为%s"%max(ls))
'''


def No_3_IsPrime(n=600851475143):
    f = 2
    while f * f <= n:
        while not n % f:
            n //= f
        f += 1
    if n == 1:
        return f - 1
    else:
        return n


# Project Euler No.4
'''
最大回文乘积
回文数就是从前往后和从后往前读都一样的数。由两个2位数相乘得到的最大回文乘积是 9009 = 91 × 99。

找出由两个3位数相乘得到的最大回文乘积

两个最大三位数相乘=999*999，所以先找出998001以内所有的回文数
最小的两个三位数相乘=100*100，所以回文数要大于10000
从大的开始检查是否有三位数的因子，从999开始，如果被整除则为最大


def palindromic_M():
    ss = []
    li = []
    for j in range(1,10):
        for i in range(0,10):
            ss.append(int(str(j)+str(i)+str(i)+str(i)+str(i)+str(j)))
            ss.append(int(str(j)+str(j)+str(i)+str(i)+str(j)+str(j)))
            ss.append(int(str(j)+str(j)+str(j)+str(j)+str(j)+str(j)))
    [li.append(x) for x in ss if x not in li]
    li.sort()
    for i in li[::-1]:
        for j in range(100,1000):
            if i%j == 0 and i/j < 1000:
                print("最大数为：%sX%s=%s"%(j,int(i/j),i))
                return
发现没有尽所有回文数，看到有这么种方式可以
def is_palindrome(n):   
    return str(n)==str(n)[::-1]
 
for i in filter(is_palindrome,range(1000000)):
    print(i)
'''


def No_4_Palindromic():
    ss = [i for i in range(998002) if str(i) == str(i)[::-1] and i > 10000]
    return print(["%s X %s = %s" % (j, int(i / j), i) for i in ss[::-1] for j in range(100, 1000) if
                  i % j == 0 and i / j < 1000][0])


# Project Euler No.5
'''
最小倍数
2520是最小的能够被1到10整除的数。

最小的能够被1到20整除的正数是多少？

就是求最小公倍数

def gg():
    li = [2]
    for i in [i for i in range(2,21)]:
        print("现在i是：%s"%i)
        if li[-1] < i:
            ss = i
            ll = li[-1]
            ls = ss
            gb(li,ls,ll,ss)
        else:
            ss = li[-1]
            ll = i
            ls = ss
            gb(li,ls,ll,ss)
    return li[-1]

def gb(li,ls,ll,ss):
    while True:
        if ls%ll == 0 and ls%ss == 0:
            print("ll：%s和ss:%s的最小公倍数：%s"%(ll,ss,ls))
            return li.append(ls)    
        else:
            ls += 1

最大公约数：
def gys(x,y):
    while y:
        x,y = y,x%y
    return x
    
欧几里德算法：   
最大公约数是最小公倍数的约数，且最小公倍数与最大公约数的商等于两个数分别与最大公约数的商的积。
即：若X、Y的最大公约数是A、最小公倍数是B，则有B/A=（X/A）（Y/A）。
'''


def No_5_Common_Multiple(ran=21):
    li = [1]
    for i in [i for i in range(2, ran)]:
        common_for_euler.common_Divisor(li[-1], i, i, li)
    return print(int(li[-1]))


# Project Euler No.6
'''
平方的和与和的平方之差
前十个自然数的平方的和是
1² + 2² + … + 10² = 385
前十个自然数的和的平方是
(1 + 2 + … + 10)² = 552 = 3025
因此前十个自然数的平方的和与和的平方之差是 3025 − 385 = 2640。

求前一百个自然数的平方的和与和的平方之差。
'''


def No_6_Square_Foot_Square(s=100):
    print(sum(list(range(s + 1))) ** 2 - sum([i ** 2 for i in range(s + 1)]))


# Project Euler No.7
'''
第10001个素数
列出前6个素数，它们分别是2、3、5、7、11和13。我们可以看出，第6个素数是13。

第10,001个素数是多少？
def No_7_Prime_X(num=10001):
    b,li = 2,[1]
    while li.index(li[-1]) != num:       
        if isPrime2(b):
            li.append(b)
            b += 1
        else:
            b += 1
    print(li[-1])
'''


def No_7_Prime_X(num=10001):
    from itertools import count
    for i in count(2):
        if common_for_euler.isPrime2(i) and num > 0:
            num -= 1
        elif num == 0:
            return i - 1


# Project Euler No.8
'''连续数字最大乘积
在下面这个1000位正整数中，连续4个数字的最大乘积是 9 × 9 × 8 × 9 = 5832。

找出这个1000位正整数中乘积最大的连续13个数字。它们的乘积是多少？'''


def No_8_Continued_Product(text='''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''):
    from functools import reduce
    ss = (text.replace("\n", "")).replace(" ", "")
    lis = []
    for i in range(len(str(ss)) - 12):
        lis.append(reduce(lambda a, b: a * b, [int(str(ss)[j]) for j in range(i, i + 13)]))
    return max(lis)


# Project Euler No.9
'''
特殊毕达哥拉斯三元组
毕达哥拉斯三元组是三个自然数a < b < c组成的集合，并满足

a² + b² = c²
例如，3² + 4² = 9 + 16 = 25 = 5²。

有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc。

枚举就行了
'''


def No_9_Pythagorean_Triples(ss=1000):
    for a in range(1, ss):
        for b in range(a + 1, ss):
            c = ss - a - b
            if a * a + b * b == c * c:
                return a, b, c, a * b * c


# Project Euler No.10
'''
素数的和
所有小于10的素数的和是2 + 3 + 5 + 7 = 17。

求所有小于两百万的素数的和
'''


def No_10_Sum_Prime(n=2000000):
    su = 0
    for i in range(n):
        if common_for_euler.isPrime2(i):
            su += i
    return su


# Project Euler No.11
'''
方阵中的最大乘积
在如下的20×20方阵中，有四个呈对角线排列的数被标红了。

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
这四个数的乘积是26 × 63 × 78 × 14 = 1788696。

在这个20×20方阵中，四个在同一方向（从下至上、从上至下、从右至左、从左至右或者对角线）上相邻的数的乘积最大是多少？

把这个坐标化，用嵌套list，用索引.索引来确定坐标点，四个方向，侧移一位来确定4个数
'''
'''
ss = \'''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48\'''
li,di = [],{}
ls = ss.replace(" ",",").split("\n")
for i in range(len(ls[0].split(","))):
    li.append([int(j) for j in ls[i].split(",")])

con_One = len(li[0])
maxNum = 0

def maxnum():
    array_Across()
    array_Vertical()
    array_RightOblique()
    array_LeftOblique()
    print(di.get(maxNum),maxNum)

def array_Across():
    contrast = 0
    global maxNum
    for i in range(con_One):
        for j in range(con_One-3):
            if li[i][j] and li[i][j+1] and li[i][j+2] and li[i][j+3]:
                contrast = li[i][j]*li[i][j+1]*li[i][j+2]*li[i][j+3]
                if contrast > maxNum:
                    di[li[i][j]*li[i][j+1]*li[i][j+2]*li[i][j+3]]="{},{},{},{}".format(li[i][j],li[i][j+1],li[i][j+2],li[i][j+3])
                    maxNum = contrast
    return maxNum

def array_Vertical():
    contrast = 0
    global maxNum
    for i in range(con_One-3):
        for j in range(con_One):
            contrast = li[i][j]*li[i+1][j]*li[i+2][j]*li[i+3][j]
            if contrast > maxNum:
                di[li[i][j]*li[i+1][j]*li[i+2][j]*li[i+3][j]]="{},{},{},{}".format(li[i][j],li[i+1][j],li[i+2][j],li[i+3][j])
                maxNum = contrast
    return maxNum


def array_LeftOblique():
    contrast = 0
    global maxNum
    for i in range(con_One-3):
        for j in range(con_One-3):
            contrast = li[i][j]*li[i+1][j+1]*li[i+2][j+2]*li[i+3][j+3]
            if contrast > maxNum:
                di[li[i][j]*li[i+1][j+1]*li[i+2][j+2]*li[i+3][j+3]]="{},{},{},{}".format(li[i][j],li[i+1][j+1],li[i+2][j+2],li[i+3][j+3])
                maxNum = contrast
    return maxNum

def array_RightOblique():
    contrast = 0
    global maxNum
    for i in range(con_One-3):
        for j in range(con_One-1,2,-1):
            contrast = li[i][j]*li[i+1][j-1]*li[i+2][j-2]*li[i+3][j-3]
            di[li[i][j]*li[i+1][j-1]*li[i+2][j-2]*li[i+3][j-3]]="{},{},{},{}".format(li[i][j],li[i+1][j-1],li[i+2][j-2],li[i+3][j-3])
            if contrast > maxNum:
                maxNum = contrast
    return maxNum
'''


def No_11_Maxnum(ss='''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''):
    li, di, maxNum, contrast = [], {}, 0, 0
    ls = ss.replace(" ", ",").split("\n")

    for i in range(len(ls[0].split(","))):
        li.append([int(j) for j in ls[i].split(",")])

    con_One = len(li[0])

    for i in range(con_One):
        for j in range(con_One - 3):
            if li[i][j] and li[i][j + 1] and li[i][j + 2] and li[i][j + 3]:
                contrast = li[i][j] * li[i][j + 1] * li[i][j + 2] * li[i][j + 3]
                if contrast > maxNum:
                    di[li[i][j] * li[i][j + 1] * li[i][j + 2] * li[i][j + 3]] = "{},{},{},{}".format(li[i][j],
                                                                                                     li[i][j + 1],
                                                                                                     li[i][j + 2],
                                                                                                     li[i][j + 3])
                    maxNum = contrast

    for i in range(con_One - 3):
        for j in range(con_One):
            contrast = li[i][j] * li[i + 1][j] * li[i + 2][j] * li[i + 3][j]
            if contrast > maxNum:
                di[li[i][j] * li[i + 1][j] * li[i + 2][j] * li[i + 3][j]] = "{},{},{},{}".format(li[i][j], li[i + 1][j],
                                                                                                 li[i + 2][j],
                                                                                                 li[i + 3][j])
                maxNum = contrast

    for i in range(con_One - 3):
        for j in range(con_One - 3):
            contrast = li[i][j] * li[i + 1][j + 1] * li[i + 2][j + 2] * li[i + 3][j + 3]
            if contrast > maxNum:
                di[li[i][j] * li[i + 1][j + 1] * li[i + 2][j + 2] * li[i + 3][j + 3]] = "{},{},{},{}".format(li[i][j],
                                                                                                             li[i + 1][
                                                                                                                 j + 1],
                                                                                                             li[i + 2][
                                                                                                                 j + 2],
                                                                                                             li[i + 3][
                                                                                                                 j + 3])
                maxNum = contrast

    for i in range(con_One - 3):
        for j in range(con_One - 1, 2, -1):
            contrast = li[i][j] * li[i + 1][j - 1] * li[i + 2][j - 2] * li[i + 3][j - 3]
            di[li[i][j] * li[i + 1][j - 1] * li[i + 2][j - 2] * li[i + 3][j - 3]] = "{},{},{},{}".format(li[i][j],
                                                                                                         li[i + 1][
                                                                                                             j - 1],
                                                                                                         li[i + 2][
                                                                                                             j - 2],
                                                                                                         li[i + 3][
                                                                                                             j - 3])
            if contrast > maxNum:
                maxNum = contrast

    return di.get(maxNum), maxNum


# Project Euler No.12
'''
高度可约的三角形数
三角形数数列是通过逐个加上自然数来生成的。例如，第7个三角形数是 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28。三角形数数列的前十项分别是：

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
让我们列举出前七个三角形数的所有约数：

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
我们可以看出，28是第一个拥有超过5个约数的三角形数。

第一个拥有超过500个约数的三角形数是多少？
'''
'''
def ss():
    from functools import reduce
    ini,con_N = 1,0
    while con_N < 5:
        tri_N = reduce(lambda a,b:a+b,list(range(1,ini+1)))
        con_N = len([i for i in range(1,tri_N+1) if tri_N%i==0 ])
        ini += 1
    print("当a={}时，三角形数为{}，约数有{}个".format(ini,tri_N,con_N))
#还是想用遍历列表配对
def ss():
    li = sorted([i for i in range(1,10)]+[i for i in range(1,10)])
    ls = sorted([1]+[i for i in range(3,10) if i%2 == 1]+[i for i in range(3,10) if i%2 == 1])
    for s in range(len(ls)):
        ll = li[s]*ls[s]
        kk = len([i for i in range(1,ll+1) if ll%i==0 ])
        print(kk)

def ss():
    a,b,ss = 1,3,0
    while ss < num:
        if len([i for i in range(1,a*b+1) if (a*b)%i==0]) < num:
            a += 1
            if len([i for i in range(1,a*b+1) if (a*b)%i==0]) < num:
                b += 2
            else:
                break
        else:
            break
    print(a,b,a*b)
把这个数先用2、3、5、7、11、13、......等质数的连乘积表示，比如
24=2*2*2*3=2³*3
再用各个质数的指数加一后再相乘即为此数的约数个数，
比如 (3+1)*(1+1)=4*2=8， 即表示24有8个约数。
#遍历还是太慢，在验证区还是要用其他办法

itertools.count(1)无限迭代1,2,3,4,5,...叠加成三角形数
'''


def No_12_Triangular_Number(num=500):
    from collections import Counter
    from functools import reduce  # reduce不能计算为空的迭代
    from itertools import count
    a = 1
    for i in count(2):
        a += i
        if reduce(lambda x, y: x * y, [Counter(common_for_euler.isPrime_factor(a)).get(j) + 1 for j in Counter(common_for_euler.isPrime_factor(a))]) > num:
            return a


# Project Euler No.13
'''
大和
计算出以下一百个50位数的和的前十位数字。
'''


def No_13_Large_Sum():
    from functools import reduce
    largeNum = '''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''
    return int(str(reduce(lambda a, b: a + b, [int(i) for i in largeNum.split("\n")]))[0:10:])


# Project Euler No.14
'''
最长考拉兹序列
在正整数集上定义如下的迭代序列：

n → n/2 （若n为偶数）
n → 3n + 1 （若n为奇数）

从13开始应用上述规则，我们可以生成如下的序列：

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
可以看出这个序列（从13开始到1结束）共有10项。尽管还没有被证明，但我们普遍认为，从任何数开始最终都能迭代至1（“考拉兹猜想”）。

从小于一百万的哪个数开始，能够生成最长的序列呢？

注： 序列开始生成后允许其中的项超过一百万。
'''


def No_14_Longest_Collatz_sequence(num=1000000):
    ss, ls = 0, []
    for n in range(1, num):
        li = [n]
        while n != 1:
            if n % 2 == 0:
                n /= 2
                li.append(n)
            else:
                n = n * 3 + 1
                li.append(n)
        if len(li) > ss:
            ss, ls = len(li), li
    return ls[0]


# Project Euler No.15
'''
网格路径
从一个2×2方阵的左上角出发，只允许向右或向下移动，则恰好有6条通往右下角的路径。

对于20×20方阵来说，这样的路径有多少条？
'''
'''
如果是阵列，从到点的步数规律如下：
0   1   1   1    1
1   2   3   4    5
1   3   6   10   15
1   4   10  20   35
1   5   15  35   70
用numpy可以计算(1-17)，但是到18的时候，结果是负数，在矩阵里面也是唯一负数
def ss(num=2):
    import numpy as np
    arr = np.zeros((num,num),dtype=np.long)
    for i in range(num):
        for j in range(num):
            arr[i][0]=1
            arr[0][j]=1
            arr[0][0]=0

    for i in range(1,num):
        for j in range(1,num):
            arr[i][j]=arr[i-1][j]+arr[i][j-1]
    print (arr[num-1,num-1], arr)
'''
'''
def No_15_arr(num=20):
    from functools import reduce
    sum1,sum2 = 1,1
    return int(reduce(lambda a,b:a*b, [i for i in range(num*2,num,-1)]) / reduce(lambda a,b:a*b, [i for i in range(num,0,-1)]))
'''
'''
用排列组合即可解决：C(n,m) = n!/(m!(n-m)!)
20*20的方格中，从左上角到右下角，不论怎么走，都是20步向左和20步向右，
即：在40步中，20个“向右”和20个“向下”共有几种排法？
C(40,20)=40!/20!/（40-20）!
'''


def No_15_arr(num=20):
    import math
    return int(math.factorial(num * 2) / math.factorial(num) / math.factorial(num))


# Project Euler No.16
'''
幂的数字和
2**15 = 32768，而32768的各位数字之和是 3 + 2 + 7 + 6 + 8 = 26。

2**1000的各位数字之和是多少？
'''


def No_16_Power_Digit_sum(n=2, m=1000):
    return sum([int(i) for i in str(n ** m)])


# Project Euler No.17
'''
表达数字的英文字母计数
如果把1到5写成英文单词，分别是：one, two, three, four, five，这些单词一共用了3 + 3 + 5 + 4 + 4 = 19个字母。

如果把1到1000都写成英文单词，一共要用多少个字母？

注意： 不要算上空格和连字符。例如，342（three hundred and forty-two）包含23个字母，而115（one hundred and fifteen）包含20个字母。单词“and”的使用方式遵循英式英语的规则。
'''
# 1位数
'''
di1.get(1-11)
'''
# 10位数
'''
di3.get(1-9)+di1.get(1-10)
di2.get(1-10)
'''
# 100位数
'''
di1.get(1-10)+"hundred and"+di1.get(1-10)
di1.get(1-10)+"hundred and"+di2.get(1-9)
di1.get(1-10)+"hundred and"+di2.get(1-9)+di1.get(1-10)
'''
'''
用字典做
def ss():
    str1 = "one two three four five six seven eight nine"
    str2 = "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
    str3 = "twenty thirty fourty fifty sixty seventy eighty ninety"
    di1 = {i:j for i,j in enumerate(str1.split(" "),1)}
    di2 = {i:j for i,j in enumerate(str2.split(" "),1)}
    di3 = {i:j for i,j in enumerate(str3.split(" "),1)}
    l0 = ["ten","hundred"]
    l1 = [di1.get(i+1) for i in range(len(di1))]
    l2 = [di3.get(i+1)+di1.get(j+1) for i in range(len(di3)) for j in range(len(di1))]
    l3 = [di2.get(i+1) for i in range(len(di2))]
    l4 = [di1.get(i+1)+"hundredand"+di1.get(j+1) for i in range(len(di1)) for j in range(len(di1))]
    l5 = [di1.get(i+1)+"hundredand"+di2.get(j+1) for i in range(len(di1)) for j in range(len(di2))]
    l6 = [di1.get(i+1)+"hundredand"+di3.get(j+1)+di1.get(k+1) for i in range(len(di1)) for j in range(len(di3)) for k in range(len(di1))]
    return len("".join(l0 + l1 + l2 + l3 + l4 + l5 + l6))
'''


def No_17_Number_Letter_counts():
    str1 = "one two three four five six seven eight nine"
    str2 = "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
    str3 = "twenty thirty fourty fifty sixty seventy eighty ninety"
    di1 = [i for i in str1.split(" ")]
    di2 = [i for i in str2.split(" ")]
    di3 = [i for i in str3.split(" ")]
    l1 = ["ten", "onethousand"]
    l2 = [i + j for i in di3 for j in di1]
    l3 = [i + "hundredand" for i in di1]
    l4 = [i + "hundredand" + j for i in di1 for j in di1]
    l5 = [i + "hundredand" + j for i in di1 for j in di2]
    l6 = [i + "hundredand" + j + k for i in di1 for j in di3 for k in di1]
    return len("".join(di1 + di2 + di3 + l1 + l2 + l3 + l4 + l5 + l6))


# Project Euler No.18
'''
最大路径和 I
从下面展示的三角形的顶端出发，不断移动到在下一行与其相邻的元素，能够得到的最大路径和是23。

       3
      7 4
     2 4 6
    8 5 9 3

如上图，最大路径和为 3 + 7 + 4 + 9 = 23。

求从下面展示的三角形顶端出发到达底部，所能够得到的最大路径和：

 ↓---↓
 
注意： 在这个问题中，由于只有16384条路径，通过尝试所有的路径来解决问题是可行的。但是，对于第67题，虽然是一道相同类型的题目，但是三角形将拥有一百行，此时暴力破解将不能解决，而需要一个更加聪明的办法！;o)

用倒数第二行，每个数都能往下分别加2个近邻的数，留下最大的，成为新的倒数第二行（重复动作）；从最下面一层往上面算，最后加出来的数就是最大路径和
'''


def No_18_Maximum_Path():
    li = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
    Tri = [li.split("\n")[i].split(" ") for i in range(len(li.split("\n")))]
    for i in range(1, 15):
        Tri[-i - 1] = [max(int(Tri[-i - 1][j]) + int(Tri[-i][j]), int(Tri[-i - 1][j]) + int(Tri[-i][j + 1])) for j in
                       range(len(Tri[-i - 1]))]
    return Tri[0][0]


# Project Euler No.19
'''
数星期日
下列信息是已知的，当然你也不妨自己再验证一下。

1900年1月1日是星期一。
三十天在九月中，
四六十一也相同。
剩下都是三十一，
除去二月不统一。
二十八天平常年，
多加一天在闰年。
闰年指的是能够被4整除却不能被100整除的年份，或者能够被400整除的年份。
在二十世纪（1901年1月1日到2000年12月31日）中，有多少个月的1号是星期天？
'''
'''
def No_19_Counting_Sundays():
    week = 365%7+1
    ss = []
    for y in range(1901,2001):
        month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if (y%4==0 and y%100!=0) or y%400==0:
            month[2]=29
        for i in range(1,13):
            week += month.get(i)%7
            if week%7 == 0:
                if i+1 > 12:
                    ss.append((y+1,1))
                else:ss.append((y,i+1))
    return len(ss)
'''


def No_19_Counting_Sundays():
    import datetime
    a = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                a += 1
    return a


# Project Euler No.20
'''
阶乘数字和
n! 的意思是 n × (n − 1) × … × 3 × 2 × 1

例如，10! = 10 × 9 × … × 3 × 2 × 1 = 3628800，所以10!的各位数字和是 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27。

求出100!的各位数字和。
'''


def No_20_Factorial_Digit_sum(num=100):
    import math
    from functools import reduce
    return reduce(lambda a, b: a + b, [int(i) for i in str(math.factorial(num))])


# Project Euler No.21
'''亲和数
记d(n)为n的所有真因数（小于n且整除n的正整数）之和。
如果d(a) = b且d(b) = a，且a ≠ b，那么a和b构成一个亲和数对，a和b被称为亲和数。

例如，220的真因数包括1、2、4、5、10、11、20、22、44、55和100，因此d(220) = 284；而284的真因数包括1、2、4、71和142，因此d(284) = 220。

求所有小于10000的亲和数的和。'''


def No_21_Amicable_Numbers(num=10000):
    from functools import reduce
    li = []
    for num in range(1, num + 1):
        x, y = 0, 0
        for i in range(1, num):
            if num % i == 0:
                x += i

        for j in range(1, x):
            if x % j == 0:
                y += j

        if y == num and y != x:
            li.append(num)
            li.append(x)

    return reduce(lambda a, b: a + b, li) / 2


# Project Euler No.22
'''
姓名得分
在这个46K的文本文件names.txt（右击并选择“目标另存为……”）中包含了五千多个姓名。首先将它们按照字母序排列，然后计算出每个姓名的字母值，乘以它在按字母顺序排列后的位置，以计算出姓名得分。

例如，按照字母序排列后，位于第938位的姓名COLIN的字母值是3 + 15 + 12 + 9 + 14 = 53。因此，COLIN的姓名得分是938 × 53 = 49714。

文件中所有姓名的姓名得分之和是多少？ 324536 s = open(names.txt,r+) ss = s.read()
'''


def No_22_Names_Score():
    from functools import reduce
    ss = "MARY", "PATRICIA", "LINDA", "BARBARA", "ELIZABETH", "JENNIFER", "MARIA", "SUSAN", "MARGARET", "DOROTHY"
    sorted(ss)
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    di = dict(zip([i for i in char], list(range(1, 27))))
    return reduce(lambda a, b: a + b, [di.get(j) for i in ss for j in i])


# Project Euler No.23
'''
并非盈数之和
完全数是指真因数之和等于自身的那些数。例如，28的真因数之和为1 + 2 + 4 + 7 + 14 = 28，因此28是一个完全数。

一个数n被称为亏数，如果它的真因数之和小于n；反之则被称为盈数。

由于12是最小的盈数，它的真因数之和为1 + 2 + 3 + 4 + 6 = 16，所以最小的能够表示成两个盈数之和的数是24。通过数学分析可以得出，所有大于28123的数都可以被写成两个盈数的和；尽管我们知道最大的不能被写成两个盈数的和的数要小于这个值，但这是通过分析所能得到的最好上界。

----找出所有不能被写成两个盈数之和的正整数，并求它们的和。----

在28123范围内，找出所有盈数(一个数平方根+1之内的范围内，遍历，能整除的，就是因子，这个数除以因子就是另一个因子)，两两相加小于28124的储存起来，用set去除相同元素，然后想加，最后用1到28123的和减去set后的和，

 x = reduce(lambda a,b:a+b,[j for j in range(1,i) if i%j==0]) #遍历速度太慢，要找到其他算法

可惜列表推到里面不能放break，不然就可以ls = [li[k]+li[l]  if li[k]+li[l] < num else break for k in len(li) for l in range(k,len(li))]
'''


def No_23_Non_Abundant_sums(num=28124):
    li, ls = [], []
    for i in range(12, num):
        if sum([j + int(i / j) for j in range(2, int(i ** 0.5) + 1) if not i % j]) + 1 > i:
            li.append(i)

    for k in range(len(li)):
        for l in range(k, len(li)):
            if li[k] + li[l] < num:
                ls.append(li[k] + li[l])
            else:
                break

    return sum(range(num)) - sum(set(ls))


# Project Euler No.24
'''
字典序排列
排列指的是将一组物体进行有顺序的放置。例如，3124是数字1、2、3、4的一个排列。如果把所有排列按照数字大小或字母先后进行排序，我们称之为字典序排列。0、1、2的字典序排列是：

012   021   102   120   201   210
数字0、1、2、3、4、5、6、7、8、9的字典序排列中第一百万位的排列是什么？
'''


def No_24_Lexicographic_Permutations(num=1000000, lis={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}):
    from itertools import permutations
    return list(permutations(lis))[num - 1]


# Project Euler No.25
'''
一千位斐波那契数
斐波那契数列是按如下递归关系定义的数列：
F1 = 1 F2 = 1
Fn = Fn−1 + Fn−2

因此斐波那契数列的前12项分别是：
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

第一个有三位数字的项是第12项F12。

在斐波那契数列中，第一个有1000位数字的是第几项？
'''


def No_25_1000_Digit_Fibonacci_number(num=1000, x=1, y=1, z=2):
    while len(str(y)) != num:
        x, y, z = y, x + y, z + 1
    return z


# Project Euler No.26
'''
倒数的循环节

单位分数指分子为1的分数。分母为2至10的单位分数的十进制表示如下所示：

1/2= 0.5
1/3= 0.(3)
1/4= 0.25
1/5= 0.2
1/6= 0.1(6)
1/7= 0.(142857)
1/8= 0.125
1/9= 0.(1)
1/10= 0.1

这里0.1(6)表示0.166666…，括号内表示有一位循环节。可以看出，1/7有六位循环节。

找出正整数d < 1000，其倒数的十进制表示小数部分有最长的循环节。

1、上轮余数确定后，下一轮的余数和商也就确定了
2、当某一次的余数在之前出现过时，即出现循环节
3、1/n循环节最长为（n-1）位，因为余数最多为n种，余数为0代表除尽了

如果一个数的质因子全是2和5的话，这个数的倒数是不会无限循环的
如2，4，5，8，10
而一个数把质因子中的2和5除去后，得到一个数，我们称之为“基数”吧
这个数和它的基数的倒数循环的长度是相同的
比如说3和6的倒数的循环长度都是1
而怎么计算一个数的循环长度呢
只需要知道它能被多少长度的9整除就行了
3能被9整除，所以它的循环长度是1
7能被999999整除，商正好是循环体142857，所以它的循环长度是6
先求一个数的基数，如果是它本身，则计算它的循环长度
如果不是它自身，那它的循环长度等于基数的循环长度
我们规定1的循环长度是0，这样所以只含2，5为质因子的数的基数都为1，循环长度为0
'''
'''
def No_26_Reciprocal_Cycles():
    length = 0
    n = 0 
    for i in range(2, 1000):
        l = cycle_length(i)
        if l > length:
            length = l
            n = i
    return n

def cycle_length(n):
    i = 1
    if n % 2 == 0: return cycle_length(n / 2)
    if n % 5 == 0: return cycle_length(n / 5)
    while True:
        if (pow(10, i) - 1) % n == 0: return i
        else: i = i + 1
此表达是没问题，但是会报错OverflowError: int too large to convert to float
'''


def No_26_Reciprocal_Cycles():
    ls = [0]
    for d in range(2, 1000):
        ls.append(common_for_euler.cycles(d))
    return "循环节 {}，数字 {}".format(str(max(ls)), max(ls) + 1)  # 1/n循环节最长为（n-1）位


# Project Euler No.27
'''
二次“素数生成”多项式

欧拉发现了这个著名的二次多项式：

n² + n + 41

对于连续的整数n从0到39，这个二次多项式生成了40个素数。然而，当n = 40时，40² + 40 + 41 = 40(40 + 1) + 41能够被41整除，同时显然当n = 41时，41² + 41 + 41也能被41整除。

随后，另一个神奇的多项式n² − 79n + 1601被发现了，对于连续的整数n从0到79，它生成了80个素数。这个多项式的系数-79和1601的乘积为-126479。

考虑以下形式的二次多项式：

    n² + an + b, 满足|a| < 1000且|b| < 1000

    其中|n|指n的模或绝对值
    例如|11| = 11以及|−4| = 4

这其中存在某个二次多项式能够对从0开始尽可能多的连续整数n都生成素数，求其系数a和b的乘积。
'''


def No_27_Quadratic_Primes():
    po = a = b = 0
    for i in range(-1000, 1000):  # 范围在±1000以内
        for j in range(-1000, 1000):
            cha = 0
            res = j  #
            while common_for_euler.isPrime2(res):  # 只要是连续的，cha就会保持计数
                res = cha ** 2 + cha * i + j
                cha += 1
            if po < cha:  # 对以上循环的结果进行赋值回收
                po = cha
                a = i
                b = j
    return po, a, b, a * b


# Project Euler No.28
'''
螺旋数阵对角线

从1开始，按顺时针顺序向右铺开的5 × 5螺旋数阵如下所示：

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
可以验证，该数阵对角线上的数之和是101。

以同样方式构成的1001 × 1001螺旋数阵对角线上的数之和是多少？

右上刚好是1² 3² 5² 7²
第一圈的角=
3²-1*2
3²-2*2
3²-3*2
第二圈的角=
5²-1*4
5²-2*4
5²-3*4
第三圈的角=
7²-1*6
7²-2*6
7²-3*6
每一层的根是 2*层数 中的奇数
'''
'''
def No_28_Number_Spiral_diagonals(num=1001):
    li = [i**2 for i in range(1,2*num) if i%2]
    ls = [li[int(i/2)]-i*j for i in range(2,len(li)*2,2) for j in range(1,4)]
    return sum(li+ls)
'''
'''
从2开始，每隔4次增加2，刚好是奇数-1
'''


def No_28_Number_Spiral_diagonals(num=1001):
    res = iterm = 1
    for i in range(3, num * 2, 2):
        for j in range(1, 5):
            iterm += i - 1
            res += iterm
    return res


# Project Euler No.29
'''
不同的幂

考虑所有满足2 ≤ a ≤ 5和2 ≤ b ≤ 5的整数组合生成的幂ab：

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125

如果把这些幂按照大小排列并去重，我们得到以下由15个不同的项组成的序列：

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
在所有满足2 ≤ a ≤ 100和2 ≤ b ≤ 100的整数组合生成的幂ab排列并去重所得到的序列中，有多少个不同的项？
'''


def No_29_Distinct_Powers(num=100):
    return len(set([i ** j for i in range(2, num + 1) for j in range(2, num + 1)]))


# Project Euler No.30
'''
各位数字的五次幂

令人惊讶的是，只有三个数可以写成它们各位数字的四次幂之和：

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44

由于1 = 14不是一个和，所以这里并没有把它包括进去。

这些数的和是1634 + 8208 + 9474 = 19316。

找出所有可以写成它们各位数字的五次幂之和的数，并求这些数的和。
'''
'''
我们取极限值，假设每一位都是数字9.每一位数的5次方也就是9^5=59049. 只有一位的时候没有问题，因为有1的存在。
我们要找的就是最大的值 两位的时候最大是99肯定也没有问题 三位的时候也没有问题 四位的时候也没有问题。
5位的时候也可以。因为9的5次方就是一个5位数。 6位数也是可以的，我们来看一下，假如说6位都是9.最后的结果就是6*9^5=354294
是一个六位数。 7位的时候，结果最大是7*9^5=413343也是一个6位数，肯定小于七位数。 所以我们通过分析，最大不会超过354294.
'''


def No_30_Digit_Fifth_powers():
    from itertools import count
    li = []
    for n in count(2):
        s = 0
        for i in str(n):
            s += int(i) ** 5
        if s == n:
            li.append(s)
        elif s > 354294:
            return sum(li), li


'''
以下这种方式会更快
# 找出所有能写成各位数字五次方之和的数之和
# 比如 ABCD = A**5 + B**5 + C**5 + D**5
from time import time 
import itertools
def euler030():
    l_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l_result = []
    #粗略算一下，只能是3-6位数之间
    for i in range(3, 7):
        for each in itertools.combinations_with_replacement(l_nums, i):
            n_sum = sum([x ** 5 for x in each])
            t1 = list(each)
            t1.sort()
            t2 = [int(n) for n in list(str(n_sum))]
            t2.sort()
            if t1 == t2:
                l_result.append(n_sum)
    print(sum(l_result))           
if __name__ == '__main__':
    start = time() 
    euler030()
    print('cost %.6f sec' % (time() - start))
'''
# Project Euler No.31
'''
硬币求和

英国的货币单位包括英镑£和便士p，在流通中的硬币一共有八种：

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)

以下是组成£2的其中一种可行方式：

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

不限定使用的硬币数目，组成£2有多少种不同的方式？
'''


def No_31_Coin_Sums():
    num = 0
    for i in range(3):
        for j in range(5):
            if i * 100 + j * 50 > 200:
                break
            for k in range(11):
                if i * 100 + j * 50 + k * 20 > 200:
                    break
                for l in range(21):
                    if i * 100 + j * 50 + k * 20 + l * 10 > 200:
                        break
                    for m in range(41):
                        if i * 100 + j * 50 + k * 20 + l * 10 + m * 5 > 200:
                            break
                        for n in range(101):
                            if i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n * 2 > 200:
                                break
                            for o in range(201):
                                if i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n * 2 + o * 1 == 200:
                                    num += 1
                                    break
                                elif i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n * 2 + o * 1 > 200:
                                    break
    return num + 1


# Project Euler No.32
'''
全数字的乘积

如果一个n位数包含了1至n的所有数字恰好一次，我们称它为全数字的；例如，五位数15234就是1至5全数字的。

7254是一个特殊的乘积，因为在等式39 × 186 = 7254中，被乘数、乘数和乘积恰好是1至9全数字的。

找出所有被乘数、乘数和乘积恰好是1至9全数字的乘法等式，并求出这些等式中乘积的和。

注意：有些乘积可能从多个乘法等式中得到，但在求和的时候只计算一次
'''


def No_32_Pandigital_Products():
    lis = []
    for i in range(1, 100):
        for j in range(100, 10000):
            if len(str(i)) + len(str(j)) + len(str(i * j)) == 9 and sorted(str(i) + str(j) + str(i * j)) == ['1', '2',
                                                                                                             '3', '4',
                                                                                                             '5', '6',
                                                                                                             '7', '8',
                                                                                                             '9']:
                lis.append(i * j)
    return sum(set(lis))


# Project Euler No.33
'''
消去数字的分数

49/98是一个有趣的分数，因为缺乏经验的数学家可能在约简时错误地认为，等式49/98 = 4/8之所以成立，是因为在分数线上下同时抹除了9的缘故。

我们也会想到，存在诸如30/50 = 3/5这样的平凡解。

这类有趣的分数恰好有四个非平凡的例子，它们的分数值小于1，且分子和分母都是两位数。

将这四个分数的乘积写成最简分数，求此时分母的值。
'''


def No_33_Digit_Cancelling_fractions():
    from functools import reduce
    ls = []
    for i in [[i, j] for i in range(11, 100) for j in range(10, i) if j % 10 != 0]:
        if int(str(i[0])[0]) == int(str(i[1])[0]) and i[0] / i[1] == int(str(i[0])[1]) / int(str(i[1])[1]):
            ls.append(i)
        elif int(str(i[0])[1]) == int(str(i[1])[0]) and i[0] / i[1] == int(str(i[0])[0]) / int(str(i[1])[1]):
            ls.append(i)
        elif int(str(i[0])[0]) == int(str(i[1])[1]) and i[0] / i[1] == int(str(i[0])[1]) / int(str(i[1])[0]):
            ls.append(i)
        elif int(str(i[0])[1]) == int(str(i[1])[1]) and i[0] / i[1] == int(str(i[0])[0]) / int(str(i[1])[0]):
            ls.append(i)
    return int(reduce(lambda a, b: a * b, [i[0] for i in ls]) / reduce(lambda a, b: a * b, [i[1] for i in ls]))


# Project Euler No.34
'''
各位数字的阶乘

145是个有趣的数，因为1! + 4! + 5! = 1 + 24 + 120 = 145。

找出所有各位数字的阶乘和等于其本身的数，并求它们的和。

注意：因为1! = 1和2! = 2不是和的形式，所以它们并不在讨论范围内。

因为8*9!<8位，所以范围定在7*9!以内,遍历此范围内所有数，比较"阶乘和"与此数
'''


def No_34_Digit_Factorials():
    from math import factorial
    dirc = {j: factorial(k) for j, k in enumerate(range(10), 0)}
    result = []
    for i in range(11, dirc[9] * 7):
        i_Split = list(str(i))
        i_Sum = sum([dirc[int(k)] for k in i_Split])
        if i == i_Sum:
            result.append(i)
    return result, sum(result)


'''
如果没有重复的数字，可以用次方法
def No_34_Digit_Factorials():
    from math import factorial  # 阶乘
    from itertools import permutations
    ll = []
    lis = [factorial(x) for x in range(0, 10)]
    for i in range(2, 7):
        ls = [k for (k, j) in enumerate(lis) if j < 10**i]
        for each in permutations(ls, i):  # 排列可能
            nstr = ''
            nums = 0
            for j in each:
                nstr += str(j)
                nums += lis[j]
            if nums == int(nstr):
                ll.append(nums)
    return ll
'''

# Project Euler No.35
'''
圆周素数

197被称为圆周素数，因为将它逐位旋转所得到的数：197/971和719都是素数。

小于100的圆周素数有十三个：2、3、5、7、11、13、17、31、37、71、73、79和97。

小于一百万的圆周素数有多少个？
'''
'''
先整理去掉一些数字
[j for i in range(2,num) for j in range(i*i,num,i)]去除此列表内所有数字
用替换的方式
'''


def No_35_Circular_Primes(num=1000000):
    excp_Num_list = [1] * num
    excp_Num_list[0] = excp_Num_list[1] = 0
    for i in range(num):
        if excp_Num_list[i]:
            for j in range(i * i, num, i):  # 清除非质数
                excp_Num_list[j] = 0
    all_num = [k for k, l in enumerate(excp_Num_list) if l]  # 整理
    lss = 0
    for m in all_num:
        str_Num = str(m)
        for n in range(len(str_Num)):
            str_Num = str_Num[1:] + str_Num[0]
            if common_for_euler.isPrime2(int("".join(str_Num))):
                pass
            else:
                lss += 1
                break
    return len(all_num) - lss

'''
比较慢的验证方法
ll = []
for m in all_num:
    lss = 0
    str_Num = str(m)
    for n in range(len(str_Num)):
        str_Num = str_Num[1:] + str_Num[0]
        if int(str_Num) in all_num:
            lss += 1
        else:break
    if lss == len(str_Num):
        ll.append(m)
'''
'''
更快的算法
from time import time
def getPrimes(N=1000000):
    l_result = [True] * N  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, N):
        if l_result[i]:
            for j in range(i * i, N, i):  # 去掉平方，及倍数
                l_result[j] = False
    return l_result  # 返回处理后的列表

def euler034(N=1000000):
    l_primes = getPrimes(N)
    l_k = [k for (k, v) in enumerate(l_primes) if v]  # 把True转成数字
    l_result = []
    for each in l_k:  # 遍历处理后全是数字的列表
        if each in l_result:
            continue  # 去掉在l_result列表的数字
        tmp = str(each)  # 格式化数字以后
        if len(tmp) == 1:  # 满足1位数的，放到l_result里面
            l_result.append(each)
            continue
        else:
            flag = True
            l_tmp = []
            for i in range(1, len(tmp)):
                tmp = tmp[1:] + tmp[0]
                if not l_primes[int(tmp)]:
                    flag = False
                    break
                else:
                    l_tmp.append(int(tmp))
            if flag:
                l_result.append(each)
                l_result.extend(l_tmp)
    l_result = list(set(l_result))
    l_result.sort()
    print(l_result)
    print(len(l_result))
if __name__ == '__main__':
    start = time()
    euler034(1000000)
    print('cost %.6f sec' % (time() - start))
'''
# Project Euler No.36
'''
双进制回文数

十进制数585 = 10010010012（二进制表示），因此它在这两种进制下都是回文数。

找出所有小于一百万，且在十进制和二进制下均回文的数，并求它们的和。

（请注意，无论在哪种进制下，回文数均不考虑前导零。）

2进制可以这么来表示 "{:b}".format(i) 或者 str(bin(i)[2:]
'''


def No_36_Double_Base_palindromes(sour_num=1000000):
    return sum([i for i in range(sour_num) if common_for_euler.is_palindrome(str(bin(i))[2:]) and common_for_euler.is_palindrome(i)])


# Project Euler No.37
'''
可截素数

3797有着奇特的性质。不仅它本身是一个素数，而且如果从左往右逐一截去数字，剩下的仍然都是素数：3797、797、97和7；同样地，如果从右往左逐一截去数字，剩下的也依然都是素数：3797、379、37和3。

只有11个素数，无论从左往右还是从右往左逐一截去数字，剩下的仍然都是素数，求这些数的和。

注意：2、3、5和7不被视为可截素数。

方法是切片[i::]和[:-i:]
'''


def No_37_Truncatable_Primes():
    lis = []
    num = 10
    while len(lis) < 11:
        if sum([1 for i in range(len(str(num))) if common_for_euler.isPrime2(int(str(num)[i::]))]) == len(str(num)):
            if sum([1 for i in range(1, len(str(num))) if common_for_euler.isPrime2(int(str(num)[:-i:]))]) == len(str(num)) - 1:
                lis.append(num)
        num += 1
    return sum(lis), lis


# Project Euler No.38
'''
全数字的倍数

将192分别与1、2、3相乘：

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

连接这些乘积，我们得到一个1至9全数字的数192384576。我们称192384576为192和(1,2,3)的连接乘积。

同样地，将9分别与1、2、3、4、5相乘，得到1至9全数字的数918273645，即是9和(1,2,3,4,5)的连接乘积。

对于n > 1，所有某个整数和(1,2, … ,n)的连接乘积所构成的数中，最大的1至9全数字的数是多少？

解释一下：在所有整数中，与从1到9[n]乘积连续放在一起[不一定要乘到9]，刚好包含1-9并且无重复
求此整数[与n] n 必须大于 1

判断条件需要满足以下
    anth_list = list("123456789")
    result = ""
    len(result) == 9
    sorted(result) == anth_list
最小就是1，[123456789]
思考一下，如果n=1 结果自然是987654321，但是n>1 
就是说至少是2 而且拼接的值要是能*2进位的
所以最大的值不能超过5位，[如果是5位则必须大于5000]
总之可以从100000开始往前找
'''


def No_38_Pandigital_Multiples():
    anth_list = list("123456789")
    for max_num in range(100000, 0, -1):
        str_num = ""
        for i in range(1, 10):
            str_num += str(max_num * i)
            if len(str_num) == 9 and sorted(str_num) == anth_list:
                return max_num, [j for j in range(1, i + 1)]
            elif len(str_num) > 9:
                break


# Project Euler No.39
'''
整数边长直角三角形

若三边长{a,b,c}均为整数的直角三角形周长为p，当p = 120时，恰好存在三个不同的解：

{20,48,52}, {24,45,51}, {30,40,50}
在所有的p ≤ 1000中，p取何值时有解的数目最多？

直角三角形都满足毕达哥拉斯

通过最大的value，找对应的key 这里用到collections里面的Counter
max(dict(Counter([11,22,33,22])), key=dict(Counter([11,22,33,22])).get)
'''


def No_39_Integer_Right_triangles(num=1000):
    from collections import Counter
    lis = []
    for i in range(1, num):
        for j in range(i + 1, num):
            k = (i ** 2 + j ** 2) ** 0.5
            if k % 1 == 0 and k + i + j <= num:
                lis.append(tuple(sorted((i, j, int(k)))))  # Counter只能统计tuple
            elif k + i + j > num:
                break
    set_list = set(tuple(lis))  # 去掉重复的组合
    only_count = dict(Counter([sum([n for n in m]) for m in set_list]))  # 计算各个组合的和
    p = int(max(only_count, key=only_count.get))  # 最多的值
    return p, [m for m in set_list if sum([n for n in m]) == p]


# Project Euler No.40
'''
钱珀瑙恩常数

将所有正整数连接起来构造的一个十进制无理数如下所示：

0.123456789101112131415161718192021…
可以看出小数点后第12位数字是1。

如果dn表示上述无理数小数点后的第n位数字，求下式的值：

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''


def No_40_Champernowne_Constant():
    from itertools import count
    str_num = ""
    for i in count(1):
        str_num += str(i)
        if len(str_num) > 1000000:
            break
    constant = int(str_num[0])
    for j in range(1, 7):
        constant *= int(str_num[10 ** j - 1])
    return constant


# Project Euler No.41
'''
全数字的素数

如果一个n位数恰好使用了1至n每个数字各一次，我们就称其为全数字的。例如，2143就是一个4位全数字数，同时它恰好也是一个素数。

最大的全数字的素数是多少？

遍历小于10**9-1以内的素数，如果各个数字只用了一次
当然不能遍历，不管怎么看都会很大的数字，所以只能用组合

结果相当神奇：9位和8位都没有，但是7位有534个
'''


def No_41_Pandigital_Prime():
    from itertools import permutations
    for ite in range(9, 0, -1):
        lis = "123456789"[:ite:]
        prime_list = [int("".join(i)) for i in permutations(lis) if common_for_euler.isPrime2(int("".join(i)))]
        if len(prime_list) != 0:
            return max(prime_list)


# Project Euler No.42
'''
编码三角形数

三角形数序列的第n项由公式tn[t的n次方] = 1/2 n(n+1)[1/2的n(n+1)次方]给出；因此前十个三角形数是：

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
将一个单词的每个字母分别转化为其在字母表中的顺序并相加，我们可以计算出一个单词的值。例如，单词SKY的值就是 19 + 11 + 25 = 55 = t10。如果一个单词的值是一个三角形数，我们就称这个单词为三角形单词。

在这个16K的文本文件words.txt （右击并选择“目标另存为……”）中包含有将近两千个常用英文单词，这其中有多少个三角形单词？
'''


def No_42_Coded_Triangle_Numbers():
    from itertools import count
    with open(r"p042_words.txt", "r+") as word:
        lis = word.readlines()[0]
    word_list = set(lis.split("\""))
    word_list.remove("")
    word_list.remove(",")
    num_list = []
    larg = max([len(l) for l in word_list])
    for i in count(1):
        num_list.append(int((1 / 2) * i * (i + 1)))
        if num_list[-1] > larg * 26:
            break
    di = {value: num for num, value in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}
    num_form = [sum([di.get(n) for n in word]) for word in word_list]
    return sum([1 for num in num_form if num in num_list])


# Project Euler No.43
'''
子串的可整除性

1406357289是一个0至9全数字数，因为它由0到9这十个数字排列而成；但除此之外，它还有一个有趣的性质：子串的可整除性。

记d1是它的第一个数字，d2是第二个数字，依此类推，我们注意到：

d2d3d4=406能被2整除
d3d4d5=063能被3整除
d4d5d6=635能被5整除
d5d6d7=357能被7整除
d6d7d8=572能被11整除
d7d8d9=728能被13整除
d8d9d10=289能被17整除
找出所有满足同样性质的0至9全数字数，并求它们的和。
'''


def No_43_Sub_String_Divisibility():
    from itertools import permutations
    permutations_list = [per_num for per_num in permutations("0123456789") if per_num[0] != "0"]
    divisor_list = [p for p in range(18) if common_for_euler.isPrime2(p)]
    result_list = []
    for i in permutations_list:
        judge = 0
        for j in range(7):
            if int(i[1 + j] + i[2 + j] + i[3 + j]) % divisor_list[j] == 0:
                pass
            else:
                judge = 1
        if judge == 0: result_list.append(i)
    return sum([int("".join(k)) for k in result_list]), [int("".join(k)) for k in result_list]


# Project Euler No.44
'''
五边形数

五边形数由公式Pn=n(3n−1)/2生成。前十个五边形数是：

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, …
可以看出P4 + P7 = 22 + 70 = 92 = P8。然而，它们的差70 − 22 = 48并不是五边形数。

在所有和差均为五边形数的五边形数对Pj和Pk中，找出使D = |Pk − Pj|最小的一对；此时D的值是多少？

jk越接近，差值越小，找出第一对，就是最小的

先造列表 用set来查询，效率不一般的高！
'''
'''
遍历不是好方法
def isPentagon_Number(x):
    from itertools import count
    for i in count(1):
        if x == i*(3*i-1)/2: return True
        elif i > x: return False
        else: pass

def No_44_Pentagon_Numbers():
    x = 1
    while True:
        x += 1
        for n in range(x, 0, -1):
            dif_num = x*(3*x-1)/2 - n*(3*n-1)/2
            sum_num = x*(3*x-1)/2 + n*(3*n-1)/2
            if isPentagon_Number(dif_num) and isPentagon_Number(sum_num):
                return x*(3*x-1)/2, n*(3*n-1)/2, dif_num
'''


def No_44_Pentagon_Numbers(num=1):
    while True:
        num *= 10  # 不知道上限，就10倍往上找
        nums = [int(i * (3 * i - 1) / 2) for i in range(1, num)]
        pen = set(nums)
        for x in range(1, num - 1):
            for n in range(0, x):
                if nums[x] - nums[n] in pen and nums[x] + nums[n] in pen:
                    return nums[x] - nums[n]


# Project Euler No.45
'''
三角形数、五边形数和六角形数

三角形数、五边形数和六角形数分别由以下公式给出：
 
三角形数	Tn=n(n+1)/2	1, 3, 6, 10, 15, …
五边形数	Pn=n(3n−1)/2	1, 5, 12, 22, 35, …
六边形数	Hn=n(2n−1)	1, 6, 15, 28, 45, …
可以验证，T285 = P165 = H143 = 40755。

找出下一个同时是三角形数、五边形数和六角形数的数。

'''
'''
用二元一次方程直接求解：六角数一定是三角数，第N个六边形数同时是第2N-1个三角形数
n = 144
while True:
    m = n*(2*n-1)
    if ((m*24+1)**0.5+1)%6 == 0:
        print(m)
        break
    n += 1
'''
'''
def No_45_Triangular_Pentagonal_and_Hexagonal():
    from collections import Counter
    num = 100
    while True:
        num *= 10
        Triangular_list = [int(n*(n+1)/2) for n in range(286, num)]
        Pentagonal_list = [int(j*(3*j-1)/2) for j in range(166, num)]
        Hexagonal_list = [k*(2*k-1) for k in range(144, num)]
        dic = Counter(Triangular_list + Pentagonal_list + Hexagonal_list)
        for num_result in Triangular_list:
            if dic.get(num_result) == 3:
                return num_result
        print(num, "范围内还没有")
'''


def No_45_Triangular_Pentagonal_and_Hexagonal():
    from collections import Counter
    num = 100
    while True:
        num *= 10
        Pentagonal_list = [int(j * (3 * j - 1) / 2) for j in range(166, num)]
        Hexagonal_list = [k * (2 * k - 1) for k in range(144, num)]
        dic = Counter(Pentagonal_list + Hexagonal_list)
        if dic.get(max(dic, key=dic.get)) > 1:
            return max(dic, key=dic.get)


# Project Euler No.46
'''
哥德巴赫的另一个猜想

克里斯蒂安·哥德巴赫曾经猜想，每个奇合数可以写成一个素数和一个平方的两倍之和。

9 = 7 + 2×1²
15 = 7 + 2×2²
21 = 3 + 2×3²
25 = 7 + 2×3²
27 = 19 + 2×2²
33 = 31 + 2×1²

最终这个猜想被推翻了。

最小的不能写成一个素数和一个平方的两倍之和的奇合数是多少？
'''


def No_46_Goldbach_other_Conjecture():
    range_num = 10
    while True:
        range_num *= 10
        prime_nums = [i for i in range(2, range_num) if common_for_euler.isPrime2(i)]
        odd_divisible_num = [i for i in range(2, range_num) if not common_for_euler.isPrime2(i) and i % 2 == 1]
        delete_num = []
        for i in odd_divisible_num:
            for j in prime_nums:
                if i > j:
                    if (((i - j) / 2) ** 0.5) % 1 == 0:
                        delete_num.append(i)
                        break
                else:
                    break
        result_set = set(odd_divisible_num) - set(delete_num)
        if len(result_set) != 0:
            return min(result_set)
        else:
            print(range_num, "内无此数")


# Project Euler No.47
'''
不同的质因数

首次出现连续两个数均有两个不同的质因数是在：

14 = 2 × 7
15 = 3 × 5
首次出现连续三个数均有三个不同的质因数是在：

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
首次出现连续四个数均有四个不同的质因数时，其中的第一个数是多少？
'''


def No_47_Distinct_Primes_factors():
    from collections import Counter
    from itertools import count
    for i in count(1):
        li = []
        for j in range(i, i + 4):
            d1 = dict(Counter(common_for_euler.isPrime_factor(j)))
            zu = [k ** d1.get(k) for k in d1]
            li += zu

        if len(set(li)) == 16:
            return "It's", i


# Project Euler No.48
'''
自幂

十项的自幂级数求和为 1¹ + 2² + 3³ + … + 10[10次方] = 10405071317。

求如下一千项的自幂级数求和的最后10位数字：1¹ + 2² + 3³ + … + 1000[1000次方]。

return str(sum([i**i for i in range(1, 1001)]))[-10::]
'''


def No_48_Self_Powers():
    n = 1
    for i in range(2, 1001):
        n += i ** i
    return str(n)[-10::]


# Project Euler No.49
'''
素数重排

公差为3330的三项等差序列1487、4817、8147在两个方面非常特别：其一，每一项都是素数；其二，两两都是重新排列的关系。

一位素数、两位素数和三位素数都无法构成满足这些性质的数列，但存在另一个由四位素数构成的递增序列也满足这些性质。

将这个数列的三项连接起来得到的12位数是多少？
'''


def No_49_Prime_Permutations():
    prime_list = [i for i in range(10 ** 3, 10 ** 4) if common_for_euler.isPrime2(i)]
    lis, result_num = [], ""
    for j in prime_list:
        if j + 3330 in prime_list and j + 6660 in prime_list and sorted(str(j)) == sorted(str(j + 3330)) == sorted(
                str(j + 6660)):
            lis.append([j, j + 3330, j + 6660])
    if len(lis) == 2:
        lis.remove([1487, 4817, 8147])
        for num in lis[0]:
            result_num += str(num)
        return int(result_num)


# Project Euler No.50
'''
连续素数的和

素数41可以写成六个连续素数的和：

41 = 2 + 3 + 5 + 7 + 11 + 13
在小于一百的素数中，41能够被写成最多的连续素数的和。

在小于一千的素数中，953能够被写成最多的连续素数的和，共包含连续21个素数。

在小于一百万的素数中，哪个素数能够被写成最多的连续素数的和？
'''


def No_50_Consecutive_Prime_sum(num=10 ** 6):
    million_list = common_for_euler.Prime_list(num)
    primes_list = [x for x in million_list if x < 10000]  # 只要最小的这部分值，因为连加以后可能超出100W
    primes_set = set(million_list)  # 在set里面查询会快很多

    for length in range(len(primes_list), 0, -1):  # 反过来，先取最大的数字
        for i in range(0, len(primes_list) - length + 1):  # 补位，为下面的截取解决问题[逐渐缩小范围]
            sum_nums = sum(primes_list[i: i + length])  # 截取此段值加总[i 到 length的范围]往最大值靠拢
            if sum_nums > num:  # 如果这个和大于100W，则length个列表里的数相加不成立
                break
            elif sum_nums in primes_set:  # 如果这个数字小于100W，而且在列表中，就是这个数
                return sum_nums, i, i + length
        pass  # 如果这个数字小于100W，但是不在列表内[非质数]，则i+1

'''
def No_50_Consecutive_Prime_sum(num=10**6):
    million_list = Prime_list(num) # 质数列表
    max_len = 1
    prime_max_len = 2
    for inx, prime in enumerate(million_list):  # 从列表调出值和对应的索引
        print("inx, prime", inx, prime)
        primes_ele = million_list[0: max_len]  # 在prime_list截取一段值
        print("截取million_list的0到",max_len)
        primes_sum = sum(primes_ele)  # 求出这段值的和
        print("max_len, inx:",max_len, inx)
        for j in range(max_len, inx):  # 遍历max_len和索引之间的整数
            print("j,million_list[j]", j, million_list[j])
            primes_ele.append(million_list[j])  # 把prime_list[j]的值放到primes_ele
            print("primes_sum", primes_sum)
            primes_sum += million_list[j]  # primes_sum加上prime_list[j]的值
            print("开始循环")
            print("primes_sum, prime", primes_sum, prime)
            while primes_sum > prime:  # 当primes_sum大于当前索引上prime_list的值
                print("len(primes_ele), max_len + 1", len(primes_ele), max_len + 1)
                if len(primes_ele) <= max_len + 1:  # 如果primes_ele里面的数字数量小于等于max_len+1 则打断
                    print("打断")
                    break
                print("primes_sum, primes_ele[0]", primes_sum, primes_ele[0])
                primes_sum -= primes_ele[0]  # 把和减去primes_ele里面第一个数
                primes_ele.pop(0)  # 同时弹出primes_ele第一个数
            print("结束循环")
            print("primes_sum, prime", primes_sum, prime)
            if primes_sum >= prime:  # 循环完毕，如果primes_sum大于等于当前索引上的值 则打断
                print("打断")
                break
        print("primes_sum, prime", primes_sum, prime)    
        if primes_sum == prime:  # 当for循环完毕，如果相等
            print("len(primes_ele), max_len", len(primes_ele), max_len)
            if len(primes_ele) > max_len:  # 则判断数字量哪个大 如果primes_ele的数字多
                max_len = len(primes_ele)  # max_len的值变成len(primes_ele)
                prime_max_len = prime  # prime_max_len变成这个质数
                print("max_len, prime_max_len", max_len, prime_max_len)
    return prime_max_len, max_len
'''

# Project Euler No.51
'''
素数数字替换

将两位数*3的第一个数字代换为任意数字，在九个可能值中有六个是素数：13、23、43、53、73和83。

将五位数56**3的第三和第四位数字代换为相同的任意数字，就得到了十个可能值中有七个是素数的最小例子，这个素数族是：56003、56113、56333、56443、56663、56773和56993。56003作为这一族中最小的成员，也是最小的满足这个性质的素数。

通过将部分数字（不一定相邻）代换为相同的任意数字，有时能够得到八个素数，求满足这一性质的最小素数。

在一个范围内找

'''


def No_51_Prime_Digit_replacements(num=10000):
    while True:
        num *= 10
        bool_list = [True] * num
        bool_list[0], bool_list[1] = False, False
        for i, prime in enumerate(bool_list):
            if prime:
                for j in range(i * i, num, i):
                    bool_list[j] = False

        prime_list = [k for k, prime_num in enumerate(bool_list) if prime_num and len(set(str(k))) < len(str(k))]

        for the_num in prime_list:
            check_dict = common_for_euler.replace_same_digital(the_num, list(range(10)))
            for key in check_dict:
                if len([n for n in check_dict[key] if bool_list[n] and len(str(n)) == len(str(the_num))]) == 8:
                    return the_num

# -- coding = utf-8 --
# python version 3.6
from common_for_euler import *

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

        primeList = [k for k, prime_num in enumerate(bool_list) if prime_num and len(set(str(k))) < len(str(k))]

        for the_num in primeList:
            check_dict = replace_same_digital(the_num, list(range(10)))
            for key in check_dict:
                if len([n for n in check_dict[key] if bool_list[n] and len(str(n)) == len(str(the_num))]) == 8:
                    return the_num


# Project Euler No.52
'''
重排的倍数

可以看出，125874和它的两倍251748拥有同样的数字，只是排列顺序不同。

有些正整数x满足2x、3x、4x、5x和6x都拥有相同的数字，求其中最小的正整数。
'''


def No_52_Permuted_multiples():
    overlay = 0
    while True:
        overlay += 1
        num_set = {0}
        for i in range(1, 7):
            num_set.add("".join(sorted(str(overlay * i))))
        if len(num_set) == 2:
            return overlay


# Project Euler No.53
'''
组合数选择

从五个数12345中选择三个恰好有十种方式，分别是：

123、124、125、134、135、145、234、235、245和345
在组合数学中，我们记作：5C3 = 10。

一般来说，

nCr=n!/(r!(n−r)!)
 
，其中r ≤ n，n! = n×(n−1)×…×3×2×1，且0! = 1。

直到n = 23时，才出现了超出一百万的组合数：23C10 = 1144066。

若数值相等形式不同也视为不同，对于1 ≤ n ≤ 100，有多少个组合数nCr超过一百万？
'''


def No_53_Combinatoric_selections():
    from math import factorial
    num = 0
    for i in range(1, 101):
        for j in range(i, 0, -1):
            if factorial(i) / (factorial(j) * factorial(i - j)) > 1000000:
                num += 1
    return num


# Project Euler No.54
'''
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
'''
'''
此题思路判断太多

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

# 字典结构
point_dict = {j:i for i,j in enumerate("23456789abcdeSHDC",2)}
# 需要的模块
from collections import Counter
# 字符串排序，变成列表
lis = sorted("") # 牌面
lip = sorted("") # 花色
# 统计
Counter(lis)
# 顺子判断顺序

if 同花:
    if 大顺：
    elif 顺：
    else：散牌
else：
    if 顺子：
    else：散牌

if len(set(lip)) == 1:
    if point_dict.get(lis[-1])-point_dict.get(lis[0])==4 and sum([point_dict.get(i) for i in lis])==point_dict.get(lis[2]) and lis[-1]=="A":
        soccer = point_dict.get(lip[0])*10**9
    elif point_dict.get(lis[-1])-point_dict.get(lis[0])==4 and sum([point_dict.get(i) for i in lis])==point_dict.get(lis[2]):
        soccer = point_dict.get(lis[-1])*10**8 + point_dict.get(lip[0])
    else:
        soccer = point_dict.get(lis[-1])*10**5
elif len(set(lip)) > 1:
    if point_dict.get(lis[-1])-point_dict.get(lis[0])==4 and sum([point_dict.get(i) for i in lis])==point_dict.get(lis[2]):
        soccer = point_dict.get(lis[-1])*10**4
    else:
        soccer = point_dict.get(lis[-1])

# 条子判断顺序

try:
    four = 查看4个相同的
    soccer = int(four)*10**7
except ValueError: # 如果没有四个相同的
    try:
        three = 查看3个相同的
            try:
                three_two = 查看3个相同的 剩余两个相同的
                soccer = int(three)*10**6 # 如果有
            except ValueError: # 如果只有三个相同
                soccer = int(three)*10**3
    except ValueError: # 如果没有三个相同的
        two = 查看2个相同的
        if 还有另外2个相同: 则加上最后那张单牌
            soccer = int(two)*10**2
        else: 没有另外2个相同: 如果两边都相同，则加上最大的单牌
            soccer = int(two)*10**1 + int(max([i for i in poker_num_count if poker_num_count.get(i) == 1]))

try:
    four = max([i for i in Counter(lis) if Counter(lis).get(i)==4])
    soccer = point_dict.get(four)*10**7
except ValueError:
    try:
        three = max([i for i in Counter(lis) if Counter(lis).get(i)==3])
        try:
            three_two = max([i for i in Counter(lis) if Counter(lis).get(i)==2])
            soccer = point_dict.get(three)*10**6
        except ValueError: 
            soccer = point_dict.get(three)*10**3
    except ValueError:
        two = max([i for i in Counter(lis) if Counter(lis).get(i)==2])
        one = max([i for i in Counter(lis) if Counter(lis).get(i)==1])
        if min([i for i in Counter(lis) if Counter(lis).get(i)==2]) != two:
            soccer = point_dict.get(two)*10**2 + Counter(lis).get(one)
        else:
            soccer = point_dict.get(two)*10**1 + Counter(lis).get(one)

'''


def No_54_Poker_hands():
    win = 0
    with open(r"C:\\Users\lo\Documents\GitHub\Project Euler\p054_poker.txt", "r") as rr:
        for i in range(1000):
            ll = rr.readline()
            p1_poker_num = ll[0] + ll[3] + ll[6] + ll[9] + ll[12]
            p1_poker_fol = ll[1] + ll[4] + ll[7] + ll[10] + ll[13]
            p2_poker_num = ll[15] + ll[18] + ll[21] + ll[24] + ll[27]
            p2_poker_fol = ll[16] + ll[19] + ll[22] + ll[25] + ll[28]
            if poker_soccer(p1_poker_num, p1_poker_fol) > poker_soccer(p2_poker_num, p2_poker_fol):
                win += 1
    return win


# Project Euler No.55
'''
利克瑞尔数

将47倒序并相加得到47 + 74 = 121，是一个回文数。

不是所有的数都能像这样迅速地变成回文数。例如，

349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337

也就是说，349需要迭代三次才能变成回文数。

尽管尚未被证实，但有些数，例如196，被认为永远不可能变成回文数。如果一个数永远不可能通过倒序并相加变成回文数，就被称为利
克瑞尔数。出于理论的限制和问题的要求，在未被证否之前，我们姑且就认为这些数确实是利克瑞尔数。除此之外，已知对于任意一个小
于一万的数，它要么在迭代50次以内变成回文数，要么就是没有人能够利用现今所有的计算能力将其迭代变成回文数。事实上，10677是
第一个需要超过50次迭代变成回文数的数，这个回文数是4668731596684224866951378664（53次迭代，28位数）。

令人惊讶的是，有些回文数本身也是利克瑞尔数数；第一个例子是4994。

小于一万的数中有多少利克瑞尔数？

注意：2007年4月24日，题目略作修改，以强调目前利克瑞尔数理论的限制。
'''


def No_55_Lychrel_numbers():
    count = 0
    for i in range(1, 10000):
        yes_or_no = i
        for j in range(50):
            yes_or_no += int(str(yes_or_no)[::-1])
            if is_palindrome(yes_or_no):
                count += 1
                break
    return count


# Project Euler No.56
'''
幂的数字和

一古戈尔（10的100次方）是一个巨大的数字：一后面跟着一百个零。100的100次方则更是无法想像地巨大：一后面跟着两百个零。然而，
尽管这两个数如此巨大，各位数字和却都只有1。

若a, b < 100，所有能表示为a的b次方的自然数中，最大的各位数字和是多少？
'''


def No_56_Powerful_Digit_Sum():
    num = 0
    for a in range(100):
        for b in range(100):
            n = 0
            for i in str(a ** b):
                n += int(i)
            if num < n:
                num = n
    return num


# Project Euler No.57
'''
平方根逼近
2的平方根可以用一个无限连分数表示：

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + … ))) = 1.414213…
将连分数计算取前四次迭代展开式分别是：

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666…
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379…

接下来的三个迭代展开式分别是99/70、239/169和577/408，但是直到第八个迭代展开式1393/985，分子的位数第一次超过分母的位数。

在前一千个迭代展开式中，有多少个分数分子的位数多于分母的位数？
'''


def No_57_Square_root_convergents():
    li = [3, 2]
    count = 0
    for i in range(999):
        li[0], li[1] = li[0] + li[1] * 2, li[0] + li[1]
        if len(str(li[0])) > len(str(li[1])):
            count += 1
    return count


# Project Euler No.58
'''
螺旋素数
从1开始逆时针螺旋着摆放自然数，我们可以构造出一个边长为7的螺旋数阵。

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
可以发现，所有的奇数平方都在这个螺旋方针的右下对角线上，更有趣的是，在所有对角线上一共有8个素数，比例达到8/13 ≈ 62%。

在这个方阵外面完整地再加上一层，就能构造出一个边长为9的螺旋方阵。如果不断重复这个过程，当对角线上素数的比例第一次低于10%时，螺旋数阵的边长是多少？
'''


def No_58_Spiral_primes():
    side_large = 1
    interval = 2
    count_prime = 0
    count_spiral = 1
    while True:
        side_large += 2
        count_spiral += 4
        for j in range(1, 4):
            if isPrime2(side_large ** 2 - interval * j):
                count_prime += 1
        if count_prime / count_spiral < 0.1:
            return side_large
        interval += 2


# Project Euler No.59
'''
异或解密

计算机上的每个字符都被指定了一个独特的代码，其中被广泛使用的一种是ASCII码（美国信息交换标准代码）。例如，大写字母A = 65，
星号（*） = 42，小写字母k = 107。

一种现代加密方法是将一个文本文档中的符号先转化为ASCII码，然后将每个字节异或一个根据密钥确定的值。使用异或进行加密的好处
在于，只需对密文使用相同的密钥再加密一次就能得到明文，例如，65 XOR 42 = 107，而107 XOR 42 = 65。

为了使加密难以破解，密钥要和明文一样长，由随机的字节构成。用户会把加密过的信息和密钥放置在不同的地方，解密时二者缺一不可。

不幸的是，这种方法对大多数人来说并不实用，因此一个略有改进的方法是使用一个密码作为密钥。密码的长度很有可能比信息要短，这
时候就循环重复使用这个密码进行加密。这种方法需要达到一种平衡，一方面密码要足够长才能保证安全，另一方面需要充分短以方便记
忆。

你的破解任务要简单得多，因为密钥只由三个小写字母构成。文本文档cipher.txt（右击并选择“目标另存为……”）中包含了加密后的
ASCII码，并且已知明文包含的一定是常见的英文单词，解密这条消息并求出原文的ASCII码之和。
'''

'''
因为是三个小写字母构成，所以密码是以三个字母为一组对整个密文进行对应匹配【三个字母是有序的】
所以需要把整个密文拆成3份，第147...个字符为1组  第258...个字符为一组  第369...个字符为一组
猜测整个字符表中最多的是空格，所以用空格的asc异或最多的asc码，得到三个key字母的asc
重复排列key到和密文一样长，并且一一对应，然后用key去异或密文，得到的字母拼接起来
'''


def No_59_XOR_decryption(guess=32):
    with open(r"C:\\Users\lo\Documents\GitHub\Project Euler\p059_cipher.txt", "r") as rr:
        ll = rr.readline()
    ll = [int(i) for i in ll.split(",")]  # 调整数据为列表
    key = []
    for i in range(3):  # 3是因为只有三个字母
        depart = [x for x in ll[i::3]]  # 按3字节一循环分组
        key.append(max(depart, key=depart.count))  # 把最多的重复的加入列表

    key = [x ^ guess for x in key]  # 反转出key，32为猜测值（空格）
    key_asc = key * int(len(ll) / 3)  # 复制密码循环和密文一样长
    letter = [chr(x ^ y) for x, y in zip(ll, key_asc)]  # 一一匹配后 异或处理，用asc转为字母
    cipher = "".join(letter)  # 拼接结果
    asc_sum = sum([ord(x) for x in cipher])
    return cipher, asc_sum


# Project Euler No.60
'''
素数对的集合

3、7、109和673是非常特别的一组素数。任取其中的两个并且以任意顺序连接起来，其结果仍然是个素数。例如，选择7和109，我们得到
7109和1097均为素数。这四个素数的和是792，这是满足这个性质的一组四个素数的最小和。

若有一组五个素数，任取其中的两个并且以任意顺序连接起来，其结果仍然是个素数，求这样一组素数的最小和。
'''


def No_60_Prime_pair_sets():
    from itertools import combinations  # 不重复的组合
    lis = prime_list(10000)
    ll = []
    for i in combinations(lis, 5):
        flag = True
        for o in combinations(i, 2):
            num1 = int(str(o[0]) + str(o[1]))
            num2 = int(str(o[1]) + str(o[0]))
            if not isPrime2(num1) or not isPrime2(num2):
                flag = False
                break
        if flag:
            ll.append(sum(i))
    return min(ll)


'''
from time import time
from math import sqrt
def getPrimes(N):
    primes = [True] * N
    primes[0], primes[1] = False, False
    for i, prime in enumerate(primes):
        if prime:
            for j in range(i * i, N, i):
                primes[j] = False
    return [k for k, p in enumerate(primes) if p ]

def isPrime(n, l_pr):
    # 不考虑1
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    t = int(sqrt(n))
    for i in l_pr:
        if i > t:
            return True
        if n % i == 0:
            return False
    return True
def findNums(l_pr, l_primes, N, l_result):
    if N == 1 and len(l_result) < 1:
        l_result.append(min(l_primes)) 
    else:
        if len(l_result) < N:
            findNums(l_pr, l_primes, N - 1, l_result)
            for i in [x for x in l_primes if x > max(l_result)]:
                flag = True
                for j in l_result:
                    if not (isPrime(int(str(j) + str(i)), l_pr)  
                            and isPrime(int(str(i) + str(j)), l_pr)):
                        flag = False
                        break
                if flag:
                    l_result.append(i) 
                    return          
def euler060(N=10000):
    l_primes = getPrimes(N)
    l_result = [3]
    l_pr = [x for x in l_primes]
    findNums(l_pr, l_primes, 5, l_result)
    while len(l_result) < 5:
        l_primes = [i for i in l_pr if i > max(l_result)]
        l_result.remove(max(l_result))
        findNums(l_pr, l_primes, 5, l_result)
    print(l_result)
if __name__ == '__main__':
    start = time() 
    euler060()
    print('cost %.6f sec' % (time() - start))
'''

# Project Euler No.61
'''
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
存在唯一一个包含六个4位数的有序循环集，每种多边形数——三角形数、正方形数、五边形数、六边形数、七边形数和八边形数——在其中各有一个代表。求这个集合的元素和。

'''


def No_61_Cyclical_figurate_numbers(min_num=1000, max_num=10000):
    p3 = x_shape_list(lambda n: n * (n + 1) // 2, max_num, min_num)
    p4 = x_shape_list(lambda n: n * n, max_num, min_num)
    p5 = x_shape_list(lambda n: n * (3 * n - 1) // 2, max_num, min_num)
    p6 = x_shape_list(lambda n: n * (2 * n - 1), max_num, min_num)
    p7 = x_shape_list(lambda n: n * (5 * n - 3) // 2, max_num, min_num)
    p8 = x_shape_list(lambda n: n * (3 * n - 2), max_num, min_num)
    p_list = [p3, p4, p5, p6, p7, p8]
    flag = [False] * 6

    flag[-1] = True
    for i in p8:
        No_61_recursion([i], p_list, flag)


def No_61_recursion(numbers, p_list, flag):
    if len(numbers) == 6 and numbers[-1] % 100 == numbers[0] // 100:
        return print(numbers, sum(numbers))

    for i in range(6):
        if flag[i]: continue  # 如果为真则跳过
        flag[i] = True  # 标记此条列表已用，递归的时候也带进去
        for j in p_list[i]:
            if j // 100 == numbers[-1] % 100:
                No_61_recursion(numbers + [j], p_list, flag)
        flag[i] = False  # 如果在i里面没找到，重新标记为待用


# Project Euler No.62
'''
立方数重排

立方数41063625（345的3次方）可以重排为另外两个立方数：56623104（384的3次方）和66430125（405的3次方）。实际上，41063625是重排中恰好有三个立方数的最小立方数。

求重排中恰好有五个立方数的最小立方数。
'''


def No_62_Cubic_permutations():
    aa = 1
    while True:
        aa *= 10
        print(aa)
        ll = ["".join(sorted(str(i ** 3))) for i in range(1, aa)]
        cc = max(ll, key=ll.count)
        if ll.count(cc) == 5:
            return (ll.index(cc) + 1) ** 3


# Project Euler No.63
'''
幂次与位数

五位数16807=7的5次方 同时也是一个五次幂。同样的，九位数134217728=8的9次方 同时也是九次幂。

有多少个n位正整数同时也是n次幂？

范围会在10的10次方以内
a = 1
while True:
    a += 1
    if len(str(a**a)) > a:
        break
'''


def No_63_Powerful_digit_counts():
    count = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if len(str(i ** j)) == j:
                count += 1
    return count


# Project Euler No.64
'''
奇周期平方根

所有的平方根写成如下连分数表示时都是周期性重复的：

N−−√=a0+1a1+1a2+1a3+…
N=a0+1a1+1a2+1a3+…
例如，让我们考虑√23：

23−−√=4+23−−√−4=4+1123√−4=4+11+23√−37
23=4+23−4=4+1123−4=4+11+23−37
如果我们继续这个过程，我们会得到如下的展开：

N−−√=4+11+13+11+18+…
N=4+11+13+11+18+…
这个过程可以总结如下：

a0=4, 123−−√−4=23−−√+47=1+23−−√−37
a0=4, 123−4=23+47=1+23−37

a1=1, 723−−√−3=7(23−−√+3)14=3+23−−√−32
a1=1, 723−3=7(23+3)14=3+23−32

a2=2, 223−−√−3=2(23−−√+3)14=1+23−−√−47
a2=2, 223−3=2(23+3)14=1+23−47

a3=1, 723−−√−4=7(23−−√+4)7=8+23−−√−4
a3=1, 723−4=7(23+4)7=8+23−4

a4=8, 123−−√−4=23−−√+47=1+23−−√−37
a4=8, 123−4=23+47=1+23−37

a5=1, 723−−√−3=7(23−−√+3)14=3+23−−√−32
a5=1, 723−3=7(23+3)14=3+23−32

a6=3, 223−−√−3=2(23−−√+3)14=1+23−−√−47
a6=3, 223−3=2(23+3)14=1+23−47

a7=1, 723−−√−4=7(23−−√+4)7=8+23−−√−4
a7=1, 723−4=7(23+4)7=8+23−4
可以看出序列正在重复。我们将其简记为√23 = [4;(1,3,1,8)]，表示在此之后(1,3,1,8)无限循环。

前10个（无理数）平方根的连分数表示是：

√2=[1;(2)]，周期=1
√3=[1;(1,2)]，周期=2
√5=[2;(4)]，周期=1
√6=[2;(2,4)]，周期=2
√7=[2;(1,1,1,4)]，周期=4
√8=[2;(1,4)]，周期=2
√10=[3;(6)]，周期=1
√11=[3;(3,6)]，周期=2
√12= [3;(2,6)]，周期=2
√13=[3;(1,1,1,1,6)]，周期=5

在N ≤ 13中，恰好有4个连分数表示的周期是奇数。

在N ≤ 10000中，有多少个连分数表示的周期是奇数？
'''


def No_64_Odd_period_square_roots():  # 诸多不理解的地方，以后研究
    import math
    ans = 0
    for i in range(1, 10001):

        m = int(math.sqrt(i))
        if m * m == i:
            continue

        dic = {}
        a = i
        b = -m
        c = 1
        count = 0
        while True:
            nc = a - b * b
            nc /= c
            nd = int((math.sqrt(a) - b) / nc)
            nb = -b - nd * nc
            t = (nb, nc, nd)
            b = nb
            c = nc
            if t not in dic:
                count += 1
                dic[t] = 1
            else:
                break

        if count % 2 != 0:
            ans += 1
    return ans


'''
暴力破解
import decimal as dc
dc.getcontext().prec = 250
def root(n):
    blist = []
    n0 = dc.Decimal(i).sqrt()
    a0 = int(n0)
    b0 = n0 - a0
    n1 = 1/b0
    a1 = int(n1)
    b1 = n1 - a1
    while str(b1)[:11] not in blist:
        blist.append(str(b1)[:11])
        n1 = 1/b1
        a1 = int(n1)
        b1 = n1 - a1
    return len(blist)

count = 0
for i in range(2,10000):
    if i**0.5 != int(i**0.5):
        if root(i) % 2 == 1:
            count += 1
print (count)
'''

# Project Euler No.65
'''
e的有理逼近
2的算术平方根可以写成无限连分数的形式。

2–√=1+12+12+12+12+…
2=1+12+12+12+12+…
这个无限连分数可以简记为√2 = [1;(2)]，其中(2)表示2无限重复。同样的，我们可以记√23 = [4;(1,3,1,8)]。

可以证明，截取算术平方根连分数表示的一部分所组成的序列，给出了一系列最佳有理逼近值。让我们来考虑√2的逼近值：

1+12=32
1+12=32

1+12+12=75
1+12+12=75

1+12+12+12=1712
1+12+12+12=1712

1+12+12+12+12=4129
1+12+12+12+12=4129
因此√2的前十个逼近值为：

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, …

最令人惊讶的莫过于重要的数学常数e有如下连分数表示
e = [2; 1,2,1, 1,4,1, 1,6,1 , … , 1,2k,1, …]。

e的前十个逼近值为：

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, …

第10个逼近值的分子各位数字之和为1+4+5+7=17。

求e的第100个逼近值的分子各位数字之和。
'''


def No_65_Convergents_of_e():
    k = []
    for i in range(int(100 / 3) + 1):
        k.append(1)
        k.append(2 * i + 2)
        k.append(1)

    e_value = [2, 3]
    for j in range(2, 100):
        e_value.append(e_value[j - 1] * k[j - 1] + e_value[j - 2])

    return sum([int(i) for i in str(e_value[99])])


# Project Euler No.66
'''
丢番图方程
考虑如下形式的二次丢番图方程：

x² – Dy² = 1
举例而言，当D=13时，x的最小值出现在649² – 13×180² = 1。

可以断定，当D是平方数时，这个方程不存在正整数解。

对于D= {2, 3, 5, 6, 7}分别求出x取最小值的解，我们得到：

3² – 2×2² = 1
2² – 3×1² = 1
9² – 5×4² = 1
5² – 6×2² = 1
8² – 7×3² = 1

因此，对于所有D ≤ 7，当D=5时x的最小值最大。

对于D ≤ 1000，求使得x的最小值最大的D值。
'''


def No_66_Diophantine_equation():  # 估计会遍历几天吧
    lis = [n for n in range(1001) if not n ** 0.5 % 1 == 0]
    count = {0}
    for i in lis:
        y = 0
        while True:
            y += 1
            x = (y ** 2 * i + 1) ** 0.5
            if x % 1 == 0:
                count.add(x)
                break
    return max(count)


'''
觉得速度太慢，就用线程池来high了  结果 x = 2178548422
from multiprocessing.dummy import Pool

p = Pool(100)

lis = [d for d in range(1001) if not d**0.5 % 1 == 0]
count = []

def ss(i):
    y = 0
    while True:
        y += 1
        x = (y**2*i+1)**0.5
        if x % 1 == 0:
            print(i)
            count.append(x)
            break

for i in lis:
    p.apply_async(ss, args=(i,))

p.close()
p.join()
'''

'''
用数学的方法 瞬间出结果
x_max = 0
D_res = 0

for D in range(2, 1001):
    root = int(pow(D, 0.5))
    if root * root == D:
        continue

    m = 0
    d = 1
    a = root

    x_m1 = 1
    x = a

    y_m1 = 0
    y = 1

    while x ** 2 - D * y ** 2 != 1:
        m -= d * a - m
        d //= (D - m * m)
        a //= (root + m)

        x_m2 = x_m1
        x_m1 = x
        y_m2 = y_m1
        y_m1 = y

        x = a * x_m1 + x_m2
        y = a * y_m1 + y_m2

    if x > x_max:
        x_max = x
        D_res = D
        
print(D_res)
'''

# Project Euler No.67
'''
最大路径和 II

从下面展示的三角形的顶端出发，不断移动到在下一行与其相邻的元素，能够得到的最大路径和是23。

3
7 4
2 4 6
8 5 9 3
如上图，最大路径和为 3 + 7 + 4 + 9 = 23。

在这个15K的文本文件triangle.txt（右击并选择“目标另存为……”）中包含了一个一百行的三角形，求从其顶端出发到达底部，所能够得到的最大路径和。

注意：这是第18题的强化版。由于总路径一共有299条，穷举每条路经来解决这个问题是不可能的！即使你每秒钟能够检查一万亿（1012）条路径，全部检查完也需要两千万年。存在一个非常高效的算法能解决这个问题。;o)
'''


def No_67_Maximum_path_sum_II():
    with open("P067_triangle.txt", "r") as rr:
        li = rr.readlines()
    tri = [i.replace("\n", "").split() for i in li]

    for i in range(1, len(tri)):
        count_last_line = len(tri[-(i + 1)])
        tri[-(i + 1)] = [max(int(tri[-i][j]) + int(tri[-(i + 1)][j]), int(tri[-i][j + 1]) + int(tri[-(i + 1)][j])) for j
                         in range(count_last_line)]
    return print(tri[0][0])


# Project Euler No.68
'''
魔力五边形环

考虑下面这个“魔力”三角形环，在其中填入1至6这6个数，每条线上的三个数加起来都是9。


从最外侧结点所填的数最小的线（在这个例子中是4,3,2）开始，按顺时针方向，每个解都能被唯一表述。例如，上面这个解可以记作解集：4,3,2; 6,2,1; 5,1,3。

将环填满后，每条线上的总和一共有四种可能：9、10、11和12。总共有8种填法：

总和	解集
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
把解集中的数字连接起来，可以构造一个9位数字串；对于三角形环来说，最大的数字串是432621513。

在如下的“魔力”五边形环中，在其中填入1至10这10个数，根据不同的填写方式，可以组成16位或17位数字串。在“魔力”五边形环中，最大的16位数字串是多少？
'''


def No_68_Magic_5_gon_ring():
    from itertools import permutations
    num = 0
    for i in permutations(range(1, 11)):
        if i[0] == 6 and not {10, 9, 8, 7, 6} & set(i[5:]):
            x = list(i)
            if sum(x[:1] + x[5:7]) == sum(x[1:2] + x[6:8]) == sum(x[2:3] + x[7:9]) == sum(x[3:4] + x[8:]) == sum(
                    x[4:5] + x[9:] + x[5:6]):
                y = x[:1] + x[5:7] + x[1:2] + x[6:8] + x[2:3] + x[7:9] + x[3:4] + x[8:] + x[4:5] + x[9:] + x[5:6]
                num = max(num, int("".join([str(k) for k in y])))
    return num


# Project Euler No.69
'''
欧拉总计函数与最大值

在小于n的数中，与n互质的数的数目记为欧拉总计函数φ(n)（有时也称为φ函数）。例如，因为1、2、4、5、7和8均小于9且与9互质，故φ(9)=6。

n	互质的数	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666…
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
可以看出，对于n ≤ 10，当n=6时n/φ(n)取得最大值。

当n ≤ 1,000,000时，求使得n/φ(n)取得最大值的n。

1、不能为质数
2、因子越多，结果越大
结果：100W内，因子(除自己和1外)最多的合数

再分析，如果分解质因子的集合越多，说明欧拉总计函数越小[集合中包含相同的数，即为不互质]
所以直接从第一个质数开始往上乘[2x3x5x7x9x....]，在规定范围内，组成的最大的数就是 使得n/φ(n)取得最大值的n
如果在此范围内，数值过小，可以用这个数再从头开始乘以这些质数，试试会不会超过范围
'''


def No_69_Totient_maximum(max_range=10 ** 6):
    num_list = prime_list(int(max_range ** (1 / 2)))
    num = 1
    pri_list = []
    for i in num_list:
        num *= i
        pri_list.append(i)
        if num > max_range:
            num /= i
            pri_list.pop()
            break
    # 校验最大数 比如在100以内是90[2,3,5,3]
    while True:
        if num * pri_list[-1] > max_range:
            pri_list.pop()
        else:
            num *= pri_list[-1]
        if len(pri_list) == 0: return int(num)


'''
欧拉函数就是指：对于一个正整数n，小于n且和n互质的正整数（包括1）的个数，记作φ(n) 。
欧拉函数的通式：φ(n)=n*(1-1/p1)*(1-1/p2)*(1-1/p3)*(1-1/p4)…..(1-1/pn),其中p1, p2……pn为n的所有质因数，n是不为0的整数。
φ(1)=1（唯一和1互质的数就是1本身）。
用遍历的方法[遍历始终是最慢的]
y = 0
num = 0
for i in range(1,10**6+1):
    x = i
    for j in set(isPrime_factor(i)):
        x *= 1-1/j
    if y < i/x:
        y = i/x
        num = i
'''

# Project Euler No.70
'''
欧拉总计函数与重排

在小于n的数中，与n互质的数的数目记为欧拉总计函数φ(n)（有时也称为φ函数）。例如，因为1、2、4、5、7和8均小于9且与9互质，故φ(9)=6。

1被认为和任意正整数互质，所以φ(1)=1。

有趣的是，φ(87109)=79180，而79180恰好是87109的一个重排。

在1 < n < 10的7次方中，有些n满足φ(n)是n的一个重排，求这些取值中使n/φ(n)最小的一个。

8319823 跑了好久，终于出来了

用69题的思路，本题的分解质因子的集合越少，最好是n=2个质因子相乘[因为肯定不是质数]
'''


def No_70_Totient_permutation(max_range=10 ** 7):
    lis = prime_list(int(max_range / 2), 2)  # 要保证2*最大质数 刚好在范围内
    num = 0
    cha = 10

    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            if lis[i] * lis[j] < max_range:
                x = y = lis[i] * lis[j]
                x *= 1 - 1 / lis[i]
                x *= 1 - 1 / lis[j]
                if sorted(str(y)) == sorted(str(int(x))):
                    if cha > y / x:
                        cha = y / x
                        num = y
            else:
                break
    return num


# Project Euler No.71
'''
有序分数

考虑形如n/d的分数，其中n和d均为正整数。如果n < d且其最大公约数为1，则该分数称为最简真分数。

如果我们将d ≤ 8的最简真分数构成的集合按大小升序列出，我们得到：

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
可以看出2/5是3/7直接左邻的分数。

将所有d ≤ 1,000,000的最简真分数按大小升序排列，求此时3/7直接左邻的分数的分子。

分母小于等于100W，无限接近 3/7 的真分数的分子[小于3/7]

分子和分母 互质

猜测 范围固定在 40w/100w < x < 50w/100w 所以就10w个数字

从大到小的递减
分子分母增加或者减少1 并且检测是否是互质[最大公约数为1]，低于3/7的加入列表
比较最大数

'''


def No_71_Ordered_ractions(num=10 ** 6):
    x = d = num
    f = {}
    while d > 0:
        while x / d >= 3 / 7:
            x -= 1

        while x / d < 3 / 7:
            if gys(x, d) == 1:
                f[x, d] = x / d
            d -= 1
            if not d:
                break
    return max(f, key=f.get)[0]


# Project Euler No.72
'''
分数计数

考虑形如n/d的分数，其中n和d均为正整数。如果n < d且其最大公约数为1，则该分数称为最简真分数。

如果我们将d ≤ 8的最简真分数构成的集合按大小升序列出，我们得到：

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
可以看出该集合中共有21个元素。

d ≤ 1,000,000的最简真分数构成的集合中共有多少个元素？

其实本题是求 1~100W 每个数的互质数的个数的和
'''
'''
def No_72_Counting_fractions(num=10**6):
    f = 0
    for i in range(1, num+1):
        for j in range(i+1, num+1):
            if gys(i, j) == 1:
                f += 1
    return f
'''


def No_72_Counting_fractions(num=10 ** 6):  # 欧拉公式来标记列表
    p_list = prime_list(num)  # 建立num以内的素数列表
    h_list = [0] * (num + 1)  # 建立一个有num+1个0的列表

    for i in p_list:  # 先处理所有素数
        h_list[i] = i - 1  # 素数的互质数为[素数-1]

    for index, value in enumerate(p_list):  # 用素数来处理倍数[一层一层的覆盖]

        for n in range(value * value, num + 1, value):  # 处理素数的倍数
            h_list[n] = h_list[int(n / value)] * (value - 1)

        for m in range(value * value, num + 1, value * value):  # 处理素数倍数的倍数
            h_list[m] = h_list[int(m / value)] * value

    return sum(h_list)


# Project Euler No.73
'''
分数有范围计数

考虑形如n/d的分数，其中n和d均为正整数。如果n < d且其最大公约数为1，则该分数称为最简真分数。

如果我们将d ≤ 8的最简真分数构成的集合按大小升序列出，我们得到：

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
可以看出在1/3和1/2之间有3个分数。

将d ≤ 12,000的最简真分数构成的集合排序后，在1/3和1/2之间有多少个分数？
'''


def No_73_Counting_fractions_in_a_range(max_range=12000):
    f = {}
    for i in range(1, max_range):
        for j in range(i + 1, max_range):
            if 1 / 3 < i / j < 1 / 2 and gys(i, j) == 1:
                f[i, j] = i / j


'''
更科学的方法
count = {}  # 削去重复项
for i in range(3, 12001):
        for j in range (int(i / 3),int(i / 2 + 1)):  # 把范围缩小,而且过滤了非互质数
                if 1 / 2 > j / i > 1 / 3:
                        count[(j / i)] = j / i
'''

# Project Euler No.74
'''
数字阶乘链

145之所以广为人知，是因为它的各位数字的阶乘之和恰好等于本身：

1! + 4! + 5! = 1 + 24 + 120 = 145

而169则可能不太为人所知，尽管从169开始不断地取各位数字的阶乘之和构成了最长的循环回到169；事实上，只存在三个这样的循环：

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

不难证明，从任意数字出发最终都会陷入循环。例如，

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

从69开始可以得到一个拥有五个不重复项的链，但是从一个小于一百万的数出发能够得到的最长的无重复项链包含有60项。

从小于一百万的数出发，有多少条链恰好包含有60个不重复项？
'''


def No_74_Digit_factorial_chains(max_range=10 ** 6):  # 12821
    from math import factorial
    count = 0
    for num in range(2, max_range):
        num_set = {num}
        flag = True

        while flag:
            tmp = 0
            for i in str(num):
                tmp += factorial(int(i))

            if tmp in num_set:
                if len(num_set) == 60:
                    count += 1
                flag = False

            num_set.add(tmp)
            num = tmp

    return count


# Project Euler No.75
'''
唯一的整数边直角三角形

只能唯一地弯折成整数边直角三角形的电线最短长度是12厘米；当然，还有很多长度的电线都只能唯一地弯折成整数边直角三角形，例如：

12厘米: (3,4,5)
24厘米: (6,8,10)
30厘米: (5,12,13)
36厘米: (9,12,15)
40厘米: (8,15,17)
48厘米: (12,16,20)

相反地，有些长度的电线，比如20厘米，不可能弯折成任何整数边直角三角形，而另一些长度则有多个解；例如，120厘米的电线可以弯折成三个不同的整数边直角三角形。

120厘米: (30,40,50), (20,48,52), (24,45,51)

记电线长度为L，对于L ≤ 1,500,000，有多少种取值只能唯一地弯折成整数边直角三角形？

a=m^2-n^2,b=2mn,c=m^2+n^2 (m大于n mn为正整数） 可以得证a²+b²=c² 就是一组直角三角形
所以max_range< (150W/2)**0.5 [c为最大范围]
'''


def No_75_Singular_integer_right_triangles(num=1500000):
    max_range = int((num / 2) ** 0.5)
    point_list = [0] * (num + 1)
    count = 0

    for m in range(2, max_range):
        for n in range(1, m):
            if ((m + n) % 2) == 1 and gys(m, n) == 1:  # 因为后面倍数打点，所以把有公约数的去掉
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                s = a + b + c

                while s <= num:
                    point_list[s] = point_list[s] + 1
                    if point_list[c] == 1:
                        count = count + 1
                    if point_list[s] == 2:  # 有大于2的就不做处理了[已经计算过]
                        count = count - 1
                    s = s + a + b + c  # 再到倍数上去打点
    return count


'''
def No_75_Singular_integer_right_triangles(num=1500000):
    max_range = int((num / 2)**0.5)
    lis = []
    count = 0
    for m in range(1, max_range+1):
        for n in range(1, m):
            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if not k % 1 and k + i + j <= num:
                lis.append(int(k + i + j))  # 最后统计相同数
            elif k + i + j > num:
                break

    set_list = set(tuple(lis))  # 去掉重复的组合
    for i in set_list:
        if lis.count(i) == 1:
            count += 1
    return count
'''

# Project Euler No.76
'''
加和计数

将5写成整数的和有6种不同的方式：

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

将100写成整数的和有多少种不同的方式？

有多少总方式100=1+99、100=2+98、100=1+1+98......
'''


def No_76_Counting_summations(num=100):
    tmp_dict = {}
    count = 0
    for m in range(2, num + 1):
        count += divide_count(num, m, tmp_dict)
    return count


# Project Euler No.77
'''
素数加和

将10写成素数的和有5种不同的方式：

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

写成素数的和有超过五千种不同的方式的数最小是多少？
'''


def No_76_Prime_summations(num=100, min_range=5000):
    primes = [True] * num
    prime = prime_list(num)
    P = len(prime)

    # R = [[0] * P] * num  # 等价，但是结果不同
    R = []
    for i in range(100):
        R.append([0] * P)

    for k in range(P):
        R[0][k] = 1
    for n in range(0, num, 2):
        R[n][0] = 1
    for n in range(2, num):
        for k in range(1, P):
            R[n][k] = R[n][k - 1]
            if prime[k] <= n:
                R[n][k] += R[n - prime[k]][k]
        if R[n][-1] >= min_range and not primes[n] or R[n][-1] >= min_range + 1:
            return n


# Project Euler No.78
'''
硬币分拆

记p(n)是将n枚硬币分拆成堆的不同方式数。例如，五枚硬币有7种分拆成堆的不同方式，因此p(5)=7。

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

找出使p(n)能被一百万整除的最小n值。 

开始还理解错了...被100W整除的就是2   100W是被除数就是以下...
维基百科的公式
p(k) = p(k-(3*n*n-n)/2) + p(k-(3*n*n+n)/2) - p(k-(3*n*n+5*n+2)/2) - p(k-(3*n*n+7*n+4)/2) +... (n from 1 to ...) while p(0) = 1 and p(1) = 1
'''


def No_78_Coin_partitions():
    from itertools import count
    tmpDict = {0: 1, 1: 1}
    for k in count():
        s = 0
        if k == 0 or k == 1:
            continue
        for n in range(1, int(k ** 0.5 + 1), 2):
            a = k - (3 * n * n - n) / 2
            b = k - (3 * n * n + n) / 2
            c = k - (3 * n * n + 5 * n + 2) / 2
            d = k - (3 * n * n + 7 * n + 4) / 2
            if a >= 0:
                s += tmpDict[a]
            else:
                break
            if b >= 0:
                s += tmpDict[b]
            else:
                break
            if c >= 0:
                s -= tmpDict[c]
            else:
                break
            if d >= 0:
                s -= tmpDict[d]
            else:
                break
        tmpDict[k] = s

        if not s % 1000000:
            return k


# Project Euler No.79
'''
密码推断

网上银行常用的一种密保手段是向用户询问密码中的随机三位字符。例如，如果密码是531278，询问第2、3、5位字符，正确的回复应当是317。

在文本文件keylog.txt中包含了50次成功登陆的正确回复。

假设三个字符总是按顺序询问的，分析这个文本文件，给出这个未知长度的密码最短的一种可能。

先考虑没有重复数字的可能
筛选出所有出现过的数字
用冒泡排序做出来
'''


def No_79_Passcode_derivation():
    with open("p079_keylog.txt", "r") as rr:
        ss = rr.readlines()

    sr = list({i[j] for i in ss for j in range(3)})
    auth_set = {i[:3] for i in ss}

    for i in auth_set:
        a, b, c = [sr.index(j) for j in i]
        sr[a], sr[b], sr[c] = [sr[j] for j in sorted([a, b, c])]
    return "".join(sr)


# Project Euler No.80
'''
平方根数字展开

众所周知，如果一个自然数的平方根不是整数，那么就一定是无理数。这样的平方根的小数部分是无限不循环的。

2的平方根为1.41421356237309504880…，它的小数点后一百位数字的和是475。

对于前一百个自然数，求所有无理数平方根小数点后一百位数字的总和。

这里用到decimal库，计算高精度小数
'''


def No_80_Square_root_digital_expansion():
    import decimal
    decimal.getcontext().prec = 102
    sum_count = 0

    for i in range(1, 100):
        r = decimal.Decimal(i).sqrt()
        if i not in [x ** 2 for x in range(1, 11)]:
            d = str(r)[0] + str(r)[2:101]
            t = 0
            for j in d:
                t += int(j)
            sum_count += t

    return sum_count


# Project Euler No.81
'''
路径和：两个方向

在如下的5乘5矩阵中，从左上方到右下方始终只向右或向下移动的最小路径和为2427，由标注红色的路径给出。

 	 	 	 	 
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
在这个31K的文本文件matrix.txt（右击并选择“目标另存为……”）中包含了一个80乘80的矩阵，求出从该矩阵的左上方到右下方始终
只向右和向下移动的最小路径和。
'''


def No_81_Path_sum_two_ways():
    path_list = []
    with open("p081_matrix.txt", "r") as rr:
        for i in range(80):
            str_num = rr.readline().replace("\n", "").split(",")
            path_list.append([int(i) for i in str_num])

    side = len(path_list)
    for i in range(side):
        for j in range(side):
            if i == 0 and j == 0:
                pass
            elif i == 0:
                path_list[i][j] += path_list[i][j - 1]
            elif j == 0:
                path_list[i][j] += path_list[i - 1][j]
            else:
                if path_list[i][j - 1] < path_list[i - 1][j]:
                    path_list[i][j] += path_list[i][j - 1]
                else:
                    path_list[i][j] += path_list[i - 1][j]
    return path_list[side - 1][side - 1]


# Project Euler No.82
'''
路径和：三个方向

注意：这是第81题的一个更具挑战性的版本。

在如下的5乘5矩阵中，从最左栏任意一格出发，始终只向右、向上或向下移动，到最右栏任意一格结束的最小路径和为994，由标注红色的路径给出。

 	 	 	 	 
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
在这个31K的文本文件matrix.txt（右击并选择“目标另存为……”）中包含了一个80乘80的矩阵，求出从最左栏到最右栏的最小路径和。
'''


def No_82_Path_sum_three_ways():
    path_list = []
    with open("p081_matrix.txt", "r") as rr:
        for i in range(80):
            str_num = rr.readline().replace("\n", "").split(",")
            path_list.append([int(i) for i in str_num])

    targ_list = [path_list[i][79] for i in range(80)]
    for i in range(78, -1, -1):
        targ_list[0] = targ_list[0] + path_list[0][i]

        for j in range(1, 80):
            targ_list[j] = min(targ_list[j] + path_list[j][i], targ_list[j - 1] + path_list[j][i])

        for k in range(78, -1, -1):
            targ_list[k] = min(targ_list[k], targ_list[k + 1] + path_list[k][i])

    return min(targ_list)


# Project Euler No.83
'''
路径和：四个方向

注意：这是第81题的一个极具挑战性的版本。

在如下的5乘5矩阵中，从左上角到右下角任意地向上、向下、向左或向右移动的最小路径和为2297，由标注红色的路径给出。

 	 	 	 	 
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
在这个31K的文本文件matrix.txt（右击并选择“目标另存为……”）中包含了一个80乘80的矩阵，求出从左上角到右下角任意地向上、向下、向左或向右移动的最小路径和。
'''


def No_83_Path_sum_four_ways():
    path_list = []
    with open("E:\\GitHub\Project-Euler\p081_matrix.txt", "r") as rr:
        for i in range(80):
            str_num = rr.readline().replace("\n", "").split(",")
            path_list.append([int(i) for i in str_num])

    # side = 79
    # x, y = 0, 0
    # while x != side:
    #     dic = {}
    #
    #     if left < 0:
    #         pass
    #     else:
    #         dic[path_list[x - 1][y]] = (left, y)
    #
    #     if right > side:
    #         pass
    #     else:
    #         dic[path_list[x + 1][y]] = (right, y)
    #
    #     if down < 0:
    #         pass
    #     else:
    #         dic[path_list[x][y - 1]] = (x, down)
    #
    #     if up > side:
    #         pass
    #     else:
    #         dic[path_list[x][y + 1]] = (x, up)
    #
    #     cache_num = path_list[x][y]
    #     path_list[x][y] = 9999999
    #     x, y = dic.get(min(dic))
    #     ss[x][y] = 1
    #     path_list[x][y] += cache_num


'''
能出结果
file=open('E:\\GitHub\Project-Euler\p081_matrix.txt')
f=file.read()
file.close()
s=f.split('\n')
matrix = [[]*80 for i in range(80)]
for i in range(80):
    matrix[i]=s[i].split(',')
for i in range(80):
    for j in range(80):
        matrix[i][j]=int(matrix[i][j])

visited = [[False]*80 for i in range(80)]
dp = [[999999]*80 for i in range(80)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
checklist = [(0,0)]
dp[0][0] = 4445

#define the method for searching the best way:
def findway(x,y):
        if not visited[x][y]:
                visited[x][y] = True
                for m in move:
                        nx,ny = x+m[0],y+m[1]
                        if 0<=nx<80 and 0<=ny<80:
                                dp[nx][ny] = min(dp[x][y]+matrix[nx][ny],dp[nx][ny])
                                checklist.append((nx,ny))

#min7979 is the min price to go:
min7979 = 999999

#repeat again and again until the min is stable, that's the answer.
while True:
        for i in range(len(checklist)):
                findway(checklist[i][0],checklist[i][1])
        if len([(j,k) for j in range(80) for k in range(80) if not visited[j][k]]) == 0:
                visited = [[False]*80 for i in range(80)]
                checklist = [(0,0)]
                if min7979 > dp[79][79]:
                        min7979 = dp[79][79]
                else:
                        print (min7979)
                        break
'''

# Project Euler No.84
'''
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
'''


def No_84_Monopoly_odds():
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


# Project Euler No.85
'''
数长方形

如果数得足够仔细，能看出在一个3乘2的长方形网格中包含有18个不同大小的长方形，如下图所示：

尽管没有一个长方形网格中包含有恰好两百万个长方形，但有许多长方形网格中包含的长方形数目接近两百万，求其中最接近这一数目的
长方形网格的面积。

以1为单位，划分网格，长=3个格子，宽=2个格子  所以就是（3+2+1）*（2+1）= 6 * 3 = 18
三角形公式 （1+3）* 3 / 2 = 6   （1+2）* 2 * 2 = 3
(（1 + large）* large / 2） * (( 1 + wide) * wide / 2) < 200W

【先求范围】确定范围 wide, large = 100, 100 上面公式会达到25502500，所以可以把遍历范围放到100以内
'''


def No_85_Counting_rectangles(n=2000000):
    max_range, value = 1, 0
    while value < n:
        max_range *= 10
        value = ((1 + max_range) * max_range / 2) ** 2

    x, y, z = 0, 0, n
    for large in range(1, max_range):
        for wide in range(large, max_range):
            total = ((1 + large) * large / 2) * ((1 + wide) * wide / 2)
            if z > abs(n - total):
                x, y, z = large, wide, abs(n - total)
            if total > n:
                break
    return x, y, z


# Project Euler No.86
'''
长方体路径

蜘蛛S位于一个6乘5乘3大小的长方体屋子的一角，而苍蝇F则恰好位于其对角。沿着屋子的表面，从S到F的最短“直线”距离是10，路径如下图所示：


然而，对于任意长方体，“最短”路径实际上一共有三种可能；而且，最短路径的长度也并不一定为整数。

当M=100时，若不考虑旋转，所有长、宽、高均不超过M且为整数的长方体中，对角的最短距离是整数的恰好有2060个；这是使得该数目超过两千的最小M值；当M=99时，该数目为1975。

找出使得该数目超过一百万的最小M值。


把长方体想想成一个纸盒子，把盒子打开，这条线就是对角线，就是求直角三角形的组合
当直角三角形，最短两条边均不大于100的情况下，有2060种情况可以满足
'''


def No_86_Cuboid_route(maxrange=1000000):
    countKind = large = 0
    while True:
        large += 1
        for sortSide in range(2, 2 * large + 1):
            n = large ** 2 + sortSide ** 2
            if n ** 0.5 % 1 == 0:
                countKind += (sortSide // 2 - max(1, sortSide - large) + 1)
            if countKind > maxrange:
                return large


# Project Euler No.87
'''
素数幂三元组

最小的可以表示为一个素数的平方，加上一个素数的立方，再加上一个素数的四次方的数是28。实际上，在小于50的数中，一共有4个数满足这一性质：

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

有多少个小于五千万的数，可以表示为一个素数的平方，加上一个素数的立方，再加上一个素数的四次方？
'''


def No_87_Prime_power_triples(n=50000000):
    log2 = int(n ** (1 / 2)) + 1
    log3 = int(n ** (1 / 3)) + 1
    log4 = int(n ** (1 / 4)) + 1
    n2 = [i ** 2 for i in prime_list(log2)]
    n3 = [i ** 3 for i in prime_list(log3)]
    n4 = [i ** 4 for i in prime_list(log4)]
    count = set()
    for two in n2:
        for three in n3:
            for four in n4:
                if two + three + four < n:
                    count.add(two + three + four)
                else:
                    break
    return len(count)


# Project Euler No.88

'''
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

# 需要一个字典 先出现的进去，后出现如果N相同，则加不进去（求最小）
# 分解质因子，连续相乘，或者某两个或多个相乘后，用1补位
    # 因子相加，用1补位，直到等于num
    # 因子列表后面往前面乘，用1补位，直到等于num
# 当set(list(range(2, 12001))) == set(字典.keys()) 则停止搜寻
# 返回sum(字典.values())
'''
'''↑
用此递归的方式遇到因子组合极大的，会计算很久，比如256，在120以内，还行
def product_sum_more(num, divisor_list, count_num={}):  # 用递归收集所有组合
    from itertools import combinations
    import copy
    if len(divisor_list) == 2:
        return count_num
    for i in range(2, len(divisor_list)):
        for j in combinations(divisor_list, i):
            tmp_list = copy.deepcopy(divisor_list)
            pro = 1
            for k in j:
                tmp_list.remove(k)
                pro *= k

            tmp_list.append(pro)
            count = num - sum(tmp_list) + len(tmp_list)
            count_num[count] = num
            product_sum_more(num, tmp_list, count_num)

def product_sum_one_and_more(num, divisor_list, count_num={}):
    count = num - sum(divisor_list) + len(divisor_list)
    count_num[count] = num
    product_sum_more(num, divisor_list, count_num)
    return count_num
    
def No_88_Product_sum_numbers(n=12000):
    from itertools import count
    count_dict = {}
    JUDGE = {i for i in range(2, n + 1)}
    for num in count(2):
        if 1 == len(isPrime_factor(num)):
            continue
        primeList = isPrime_factor(num)
        pp = product_sum_one_and_more(num, primeList)
        for key, value in pp.items():
            if key in count_dict: continue
            else: count_dict[key] = value
        if 0 == len(JUDGE - set(count_dict.keys())):
            return sum({value for key, value in count_dict.items() if key <= n})
'''
'''
n[k]表示minimal product-sum numbers for size=k

n[k]的上界为2*k，因为2*k总是能分解成2*k，然后2*k=k+2+(1)*(k-2)

显然n[k]的下界为k

对于一个数num   因式分解后因子个数为product   这些因子的和为sump

则需要添加的1的个数为num-sump，所以size k=num-sump+product

def No_88_Product_sum_numbers(k=12000):  # 此种方法不会取2，因此偏向于上一种方法
    n = [2 * k for i in range(k)]
    getpsn(1, 1, 1, 2, k, n)
    result = sum(set(n[2:]))
    return result

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
            
[60, 1, 4, 6, 8, 8, 12, 12, 12, 15, 16, 16, 16, 18, 20, 24, 24, 24, 24, 24, 28, 27, 32, 30, 48, 32, 32, 42, 36, 36]
30以内的列表为此，求的不是最小N值
'''
'''
用筛选标记的方式，分解因子，因子个数是标记起点，num 减去 因子的和 则为补位区间
比如 16 因子为[2,2,2,2] 因子和为8 个数为4 则为从4开始，往后16-8= 8个位可以补
'''


def No_88_Product_sum_numbers(k=12000):
    from itertools import count
    group_list = [0] * (k + 1)
    pointer_shadow = 0

    for num in count(2):
        divisor_list = isPrime_factor(num)
        pointer = len(divisor_list)  # 起点，因子个数，[所有因子相加+1 = 所有因子相乘+1]

        if 1 == pointer:  # 去除质数
            continue

        max_range = num - sum(divisor_list) + pointer

        if max_range > k:  # 防止超出边界
            max_range = k

        if pointer_shadow < pointer:  # 优化一下，不用从头开始打标
            pointer_shadow = pointer

        for i in range(pointer_shadow, max_range + 1):
            if not group_list[i]:
                group_list[i] = num
        pointer_shadow = max_range + 1

        if group_list[-1]:
            divide_set = set(group_list[2:])
            return sum(divide_set)


# Project Euler No.89
'''
罗马数字

要正确地用罗马数字表达一个数，必须遵循一些基本规则。尽管符合规则的写法有时会多于一种，但对每个数来说总是存在一种“最好的”写法。

例如，数16就至少有六种写法：

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

然而，根据规则，只有XIIIIII和XVI是合理的写法，而后一种因为使用了最少的数字而被认为是最有效的写法。

在这个11K的文本文件roman.txt （右击并选择“目标另存为……”）中包含了一千个合理的罗马数字写法，但并不都是最有效的写法；有关罗马数字的明确规则，可以参考关于罗马数字。

求出将这些数都写成最有效的写法所节省的字符数。

注意：你可以假定文件中的所有罗马数字写法都不包含连续超过四个相同字符。

    I = 1 
    V = 5 
    X = 10 
    L = 50 
    C = 100 
    D = 500 
    M = 1000

    数字必须按大小的顺序排列
    M，C和X不能等同或超过较小的面值
    D，L和V每个只能出现一次

    减法原则：
    只有一个I，X和C可以用作减法对的一部分的主要数字。
    I只能放在V和X之前。
    X只能放在L和C之前。
    C只能放在D和M之前。
'''


def No_89_Roman_numerals():
    text = "C:\\Users\lo\Documents\GitHub\Project_Euler\p089_roman.txt"
    with open(text, "r") as rr:
        ss = rr.readlines()

    ss = "".join(ss)
    X = (("IIII", 2), ("XXXX", 2), ("CCCC", 2), ("VIIII", 1), ("LXXXX", 1), ("DCCCC", 1))  # 规定一个统计方式
    return sum([ss.count(num) * x for num, x in X])


# Project Euler No.90
'''
立方体数字对

在一个立方体的六个面上分别标上不同的数字（从0到9），对另一个立方体也如法炮制。将这两个立方体按不同的方向并排摆放，我们可以得到各种各样的两位数。

例如，平方数64可以通过这样摆放获得：


事实上，通过仔细地选择两个立方体上的数字，我们可以摆放出所有小于100的平方数：01、04、09、16、25、36、49、64和81。

例如，其中一种方式就是在一个立方体上标上{0, 5, 6, 7, 8, 9}，在另一个立方体上标上{1, 2, 3, 4, 8, 9}。

在这个问题中，我们允许将标有6或9的面颠倒过来互相表示，只有这样，如{0, 5, 6, 7, 8, 9}和{1, 2, 3, 4, 6, 7}这样本来无法表示09的标法，才能够摆放出全部九个平方数。

在考虑什么是不同的标法时，我们关注的是立方体上有哪些数字，而不关心它们的顺序。

{1, 2, 3, 4, 5, 6}等价于{3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6}不同于{1, 2, 3, 4, 5, 9}

但因为我们允许在摆放两位数时将6和9颠倒过来互相表示，这个例子中的两个不同的集合都可以代表拓展集{1, 2, 3, 4, 5, 6, 9}。

对这两个立方体有多少中不同的标法可以摆放出所有的平方数？
'''


@time_pay
def No_90_Cube_digit_pairs():

    from itertools import combinations

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    con = set()

    for i in combinations(nums, 6):
        for j in combinations(nums, 6):
            if j + i not in con:
                if (0 in i and 1 in j) or (1 in i and 0 in j):
                    if (0 in i and 4 in j) or (4 in i and 0 in j):
                        if (0 in i and (9 in j or 6 in j)) or ((9 in i or 6 in i) and 0 in j):
                            if (1 in i and (6 in j or 9 in j)) or ((6 in i or 9 in i) and 1 in j):
                                if (2 in i and 5 in j) or (5 in i and 2 in j):
                                    if (3 in i and (6 in j or 9 in j)) or ((6 in i or 9 in i) and 3 in j):
                                        if (4 in i and (9 in j or 6 in j)) or ((9 in i and 6 in i) and 4 in j):
                                            if ((6 in i or 9 in i) and 4 in j) or (4 in i and (6 in j or 9 in j)):
                                                if (8 in i and 1 in j) or (1 in i and 8 in j):
                                                    con.add(i + j)

    print(len(con))


# Project Euler No.91
"""
格点直角三角形

点P(x1, y1)和点Q(x2, y2)都是格点，并与原点O(0,0)构成ΔOPQ。


当点P和点Q的所有坐标都在0到2之间，也就是说0 ≤ x1, y1, x2, y2 ≤ 2时，恰好能构造出14个直角三角形。


如果0 ≤ x1, y1, x2, y2 ≤ 50，能构造出多少个直角三角形？
"""

@time_pay
def No_91_Right_triangles_with_integer_coordinates():
    """
    直角三角形公式：两短边长平方相加等于长边平方
    除去重复的
    :return:
    """
    count = 0
    for x1 in range(51):
        for y1 in range(51):
            for x2 in range(51):
                for y2 in range(51):
                    aa = x1**2 + y1**2
                    bb = x2**2 + y2**2
                    cc = (x1-x2)**2 + (y1-y2)**2
                    if (aa == bb + cc or bb == aa + cc or cc == aa + bb) and aa != 0 and bb != 0 and cc != 0:
                        count += 1
    print(count/2)


# Project Euler No.92
"""
平方数字链

将一个数的所有数字的平方相加得到一个新的数，不断重复直到新的数已经出现过为止，这构成了一条数字链。

例如，

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

可见，任何一个到达1或89的数字链都会陷入无尽的循环。更令人惊奇的是，从任意数开始，最终都会到达1或89。

有多少个小于一千万的数最终会到达89？
"""

@time_pay
def No_92_Square_digit_chains():
    """
    10000000以下平方和最大的数是9999999，其平方和为81*7=567。所以，可以先建立一个600以下的字典，
    其他数在运行过程中一旦碰到字典中的数，马上将1或89作为结果反馈。这样，可以加速运算过程。
    :return:
    """
    dict_600 = {}
    for x in range(1, 600):
        d = x
        while x != 1 and x != 89:
            # x = sum([int(i) ** 2 for i in list(str(x))])
            x = No_92_get_sum(x)
        dict_600[d] = x

    count = 0
    for num in range(1, 10**7):
        # ss = sum([int(i) ** 2 for i in list(str(num))])
        ss = No_92_get_sum(num)
        if dict_600[ss] == 89:
            count += 1

    print(count)


if __name__ == '__main__':
    No_92_Square_digit_chains()


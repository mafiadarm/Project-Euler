# -- coding = utf-8 --
# python version 3.6
import common_for_euler

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
            if common_for_euler.poker_soccer(p1_poker_num, p1_poker_fol) > common_for_euler.poker_soccer(p2_poker_num,
                                                                                                         p2_poker_fol):
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
            if common_for_euler.is_palindrome(yes_or_no):
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
            if common_for_euler.isPrime2(side_large ** 2 - interval * j):
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
    from itertools import combinations
    lis = common_for_euler.prime_list(10000)
    ll = []
    for i in combinations(lis, 5):
        flag = True
        for o in combinations(i, 2):
            num1 = int(str(o[0]) + str(o[1]))
            num2 = int(str(o[1]) + str(o[0]))
            if not common_for_euler.isPrime2(num1) or not common_for_euler.isPrime2(num2):
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
    p3 = common_for_euler.x_shape_list(lambda n: n * (n + 1) // 2, max_num, min_num)
    p4 = common_for_euler.x_shape_list(lambda n: n * n, max_num, min_num)
    p5 = common_for_euler.x_shape_list(lambda n: n * (3 * n - 1) // 2, max_num, min_num)
    p6 = common_for_euler.x_shape_list(lambda n: n * (2 * n - 1), max_num, min_num)
    p7 = common_for_euler.x_shape_list(lambda n: n * (5 * n - 3) // 2, max_num, min_num)
    p8 = common_for_euler.x_shape_list(lambda n: n * (3 * n - 2), max_num, min_num)
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

# Project Euler No.63
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


# Project Euler No.63
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
    for i in range(int(100/3)+1):
        k.append(1)
        k.append(2 * i + 2)
        k.append(1)

    e_value = [2, 3]
    for j in range(2, 100):
        e_value.append(e_value[j - 1] * k[j - 1] + e_value[j - 2])

    return sum([int(i) for i in str(e_value[99])])

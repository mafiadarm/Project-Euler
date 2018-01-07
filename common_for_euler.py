""" encode=utf-8 """

''' 以下为常用函数 '''


def __init__():
    pass


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


def common_Divisor(x, y, z, li):  # 求公约数
    while y:
        x, y = y, x % y
    return li.append(z / x * li[-1] / x * x)


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


def Prime_list(n, f=0):  # 返回N以内所有的素数
    l_result = [True] * n  # 占位 预留True
    l_result[0], l_result[1] = False, False  # 去掉1,0
    for i in range(0, n):
        if l_result[i]:
            for j in range(i * i, n, i):  # 去掉平方，及倍数
                l_result[j] = False
    return [k for k, v in enumerate(l_result) if v and k >= f]  # 返回处理后的列表


def Not_Prime_list(n, f=0):  # 返回N以内所有的非素数
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
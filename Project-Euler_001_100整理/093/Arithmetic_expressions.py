#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
算术表达式
通过使用集合 {1, 2, 3, 4} 中每个数字一次（用且只用一次），以及四种算术运算 (+, -, *, /) 和括号，我们可以得到不同的目标正整数。
例如：
8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)
但是将相连接是不允许的，如 12 + 34。
使用集合 {1, 2, 3, 4} 可以得到 31 个目标数，其中最大的是 36。而且 1 到 28 中的每个数字都可以被表示，但是 29 不能被表示。
找出四个不同的 1位数 的集合，a < b < c < d，能够形成最长的 1 到 n 的连续正整数集合。以 abcd 的形式给出你的答案。
"""
def number_tuple(m):
    for i in range(1, m - 2):
        for j in range(i + 1, m - 1):
            for k in range(j + 1, m):
                for l in range(k + 1, m + 1):
                    yield (i, j, k, l)

def operations(t):
    if len(t) == 1:
        yield t[0]
        return

    for i, e in enumerate(t):
        for result in operations(t[:i] + t[i + 1:]):
            yield e * result
            yield e + result
            yield e - result
            yield result - e
            if result != 0:
                yield e / float(result)

def consecutive_digits(digits):
    from itertools import count
    for i in count(1):
        if i not in digits:
            return i - 1

def xxx():
    max_digits = (0, None)
    for t in number_tuple(9):
        results = set(int(n) for n in operations(t) if int(n) == n and n > 0)
        max_digits = max(max_digits, (consecutive_digits(results), t))
    return ''.join(map(str, max_digits[1]))

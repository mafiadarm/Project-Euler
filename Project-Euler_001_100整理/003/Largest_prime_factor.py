#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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

"""

def big_prime(ask):
    f = 2
    while f * f <= ask:
        while not ask % f:  # 只要能整除就去除掉
            ask //= f  # 一步一步把能除掉的全除掉，剩下最大的就是最大质因数
        f += 1

    if ask == 1:
        return f - 1
    else:
        return ask

if __name__ == '__main__':
    print(big_prime(600851475143))
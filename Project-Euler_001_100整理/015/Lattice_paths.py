#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
用排列组合即可解决：C(n,m) = n!/(m!(n-m)!)
20*20的方格中，从左上角到右下角，不论怎么走，都是20步向左和20步向右，
即：在40步中，20个“向右”和20个“向下”共有几种排法？并且是不重复排列
C(40,20)=40!/20!/（40-20）!
"""
ask_length = 20
ask_width = 20
from math import factorial as fac

result = fac(ask_length + ask_width)/fac(ask_length)/fac(ask_length + ask_width - ask_length)

print(result)

# 或者直接调用工具
from scipy.special import comb

print(comb(ask_length + ask_width, ask_length))

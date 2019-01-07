#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 遍历去重

ask = range(2, 101)
result = set()

for a in ask:
    for b in ask:
        result.add(a**b)

print(len(result))
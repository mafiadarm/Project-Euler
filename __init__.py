# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_17_2018  14:42
   File Name:      /GitHub/__init__
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
==============================
"""
import os
import sys

__author__ = 'Loffew'

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    if path not in sys.path:
        sys.path.append(path)
    for p in sys.path:
        print(p)


if __name__ == '__main__':
    main()
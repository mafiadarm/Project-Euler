# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_01_2018  12:21
   File Name:      /GitHub/time_pay
   Creat From:     PyCharm
   Python version:   
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

import logging
import time
from .Project_Euler_050_to_100 import *


__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

nt = time.time()
pp_dbg(No_86_Cuboid_route(100))
nn = time.time() - nt
pp_dbg(nn)



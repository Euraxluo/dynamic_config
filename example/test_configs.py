# -*- coding: utf-8 -*- 
# Time: 2021-10-20 16:35
# Copyright (c) 2021
# author: Euraxluo

from unittest import TestCase
from example.configs import *


class Test(TestCase):
    def test_case1(self):
        import time
        i = 0
        while True:
            Config.xxx = f"test xxx sas a {i}"
            print("Config.xxx", Config.xxx)
            print("Config.yyy", Config.yyy)
            print("Config.zzz", Config.zzz)
            print("Config.mmm", Config.mmm)

            print("Config2.xxx", Config2.xxx)
            print("Config2.yyy", Config2.yyy)

            print("Config3.xxx", Config3.xxx)
            print("Config3.yyy", Config3.yyy)

            print("Config4.xxx", Config4.xxx)
            print("Config4.yyy", Config4.yyy)
            i += 1
            time.sleep(5)

# -*- coding: utf-8 -*-
# Time: 2022-02-25 14:32
# Copyright (c) 2022
# author: Euraxluo
from example.configs import *
from dynamic_config.dynamic_config import Field


class ConfigTest(DynamicConfig):
    __prefix__ = "test_config"
    __enable__ = True
    x: str = None
    y: str = Field(None)


if __name__ == '__main__':
    import time

    i = 0
    ConfigTest.y = "dsadasfsa"
    while True:
        print(f"================{i}=======================")
        print(ConfigTest.x)
        print(ConfigTest.y)
        ConfigTest.x = i
        ConfigTest.y = [i] * 2
        i += 1
        time.sleep(1)

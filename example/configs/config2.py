# -*- coding: utf-8 -*- 
# Time: 2021-10-20 16:35
# Copyright (c) 2021
# author: Euraxluo


from dynamic_config.dynamic_config import DynamicConfig, Filed


class Config3(DynamicConfig):
    __prefix__ = "config3"
    xxx: str = "1"  # 以变量为准
    yyy: str = Filed("1")  # AutoRefresh(None) 支持动态刷新


class Config4(DynamicConfig):
    xxx: int = None  # 以变量为准
    yyy: int = Filed(None)  # AutoRefresh(None) 支持动态刷新

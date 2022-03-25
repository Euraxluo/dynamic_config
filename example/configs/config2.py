# -*- coding: utf-8 -*- 
# Time: 2021-10-20 16:35
# Copyright (c) 2021
# author: Euraxluo

from dynamic_config.dynamic_config import DynamicConfig, Field


class Config3(DynamicConfig):
    __prefix__ = "config3"
    xxx: str = "1"  # 以变量为准
    yyy: str = Field("1")  # AutoRefresh 支持动态刷新


class Config4(DynamicConfig):
    xxx: int = None  # 以变量为准
    yyy: int = Field(None)  # AutoRefresh 支持动态刷新

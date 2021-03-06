# -*- coding: utf-8 -*- 
# Time: 2021-10-20 16:35
# Copyright (c) 2021
# author: Euraxluo

from dynamic_config.dynamic_config import DynamicConfig, Field


class Config(DynamicConfig):
    __prefix__ = "config"
    xxx: str = None
    yyy: str = Field(None)
    zzz: str = Field("2312321321")
    mmm: bytes = bytes("mmm", encoding="utf8")
    lll: list = [1, 2, 3, 4]


class Config2(DynamicConfig):
    xxx: int = None  # 以变量为准
    yyy: int = Field(None)  # AutoRefresh(None) 支持动态刷新

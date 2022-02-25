# -*- coding: utf-8 -*- 
# Time: 2022-02-25 14:29
# Copyright (c) 2022
# author: Euraxluo

from dynamic_config.dynamic_config import DynamicConfig
from example.conftest import rdb
from loguru import logger

DynamicConfig.register(rdb,logger=logger)
from .config import Config, Config2
from .config2 import Config3, Config4

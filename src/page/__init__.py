# -*- coding:utf-8 -*-
#@Time : 2020/6/28 16:52
#@Author: fyl
#@File : __init__.py.py
from config.global_var import g
from src.utils.driver_util import get_config

g.config = get_config()
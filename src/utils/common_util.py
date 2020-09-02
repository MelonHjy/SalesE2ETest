#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File       :   common_util.py
@Time       :   2020/7/31 18:13
@Author     :   Huang Jiayi
@Version    :   1.0
@Contact    :   huangjiayi@sinosoft.com.cn
@Desc       :   None
'''
import platform
from enum import Enum
from functools import wraps

import pytest
import selenium

from config.global_var import g
from src.utils.driver_util import get_config


class BusinessType(Enum):
    '''
        枚举业务类型：新增、变更、注销
    '''
    create = 1
    change = 2
    logout = 3


class DecoratorType(Enum):
    '''
        枚举传入测试数据的装饰器
    '''
    parametrize = 1
    fixture = 2


def tuple_to_dict(tp):
    return {'v' + str(i): tp[i] for i in range(tp.__len__())}


def tuple_to_dict_by_keys(tp, keys):
    '''

    :param tp: (1,'aa')
    :param keys: ('v0','v1')
    :return: {'v0':1,'v1':'aa'}
    '''
    return {keys[i]: tp[i] for i in range(tp.__len__())}


def return_dict(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return list(map(tuple_to_dict, data))
        # return list(map(tuple_to_dict_by_keys, data, [('code', 'name')] * data.__len__()))

    return wapper


def write_properties(file_name):
    systemVersion = "systemVersion={}".format(platform.platform())
    pythonVersion = "pythonVersion={}".format(platform.python_version())
    seleniumVersion = "seleniumVersion={}".format(selenium.__version__)
    pytestVersion = ("pytestVersion={}".format(pytest.__version__))
    g.config = get_config()
    testEnv = "testEnv={}".format(g.config['DEFAULT']['url'])
    browser = "browser={}".format(g.config['DEFAULT']['browser'])
    str = systemVersion + "\n" + pythonVersion+"\n"+seleniumVersion+"\n"+pytestVersion+"\n"+testEnv+"\n"+browser
    with open(file_name, 'w') as f:
        f.write(str)

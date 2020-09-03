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
import os
from enum import Enum
from functools import wraps

import win32api

from src.utils.log import info


def set_windows_resolution(height, width):
    dm = win32api.EnumDisplaySettings(None, 0)
    dm.PelsHeight = height
    dm.PelsWidth = width
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 0
    win32api.ChangeDisplaySettings(dm, 0)


def close_ie():
    task_kill("IEDriverServer.exe")
    task_kill("iexplore.exe")
    info("关闭ie相关进程")


def task_kill(name):
    if os.system("tasklist |findstr {}".format(name)) == 0:
        os.system("taskkill /f /im {}".format(name))


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

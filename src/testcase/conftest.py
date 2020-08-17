# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:42
# @Author: fyl
# @File : conftest.py
import os

import allure
import pytest
import win32api

from config.global_var import g
from src.page.base_page import info
from src.utils.db_util import DBUtils
from src.utils.driver_util import get_config


@pytest.fixture(scope='session', autouse=True)
def db_conn():
    g.config = get_config()
    # 获取数据库连接
    db = g.config['DEFAULT']['db']
    url = g.config[db]['url']
    user = g.config[db]['user']
    password = g.config[db]['password']
    g.db = DBUtils(url, user, password)

    # width = win32api.GetSystemMetrics(0)
    # height = win32api.GetSystemMetrics(1)
    # print('before-size:%s-%s' % (width, height))
    # set_windows_resolution(768, 1366)
    yield
    # set_windows_resolution(1080, 1920)
    info("关闭数据库连接")
    g.db.close_connection()


def set_windows_resolution(height, width):
    dm = win32api.EnumDisplaySettings(None, 0)
    dm.PelsHeight = height
    dm.PelsWidth = width
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 0
    win32api.ChangeDisplaySettings(dm, 0)


@pytest.fixture(scope='class', autouse=True)
def restore_data():
    current = os.environ.get('PYTEST_CURRENT_TEST').split('/')
    test_dir = current[2]
    test_name = current[3].split('.')[0]
    sql_path = g.root_path + '/data/' + test_dir + '/' + test_name + '.sql'
    if os.path.exists(sql_path):
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql = f.read()
            restore_log('CURRENT_TEST:%s/%s 正在恢复数据' % (test_dir, test_name))
            try:
                data = g.db.execute(sql)
                restore_log('CURRENT_TEST:%s/%s 恢复数据成功' % (test_dir, test_name))
            except Exception:
                restore_log('CURRENT_TEST:%s/%s 恢复数据失败' % (test_dir, test_name))
    else:
        restore_log('CURRENT_TEST:%s/%s 没有恢复数据sql脚本文件' % (test_dir, test_name))
    yield


@allure.step("{log}")
def restore_log(log):
    info(log)

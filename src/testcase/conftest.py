# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:42
# @Author: fyl
# @File : conftest.py
import os

import allure
import pytest
import win32api
import win32con
from selenium.webdriver.support.wait import WebDriverWait

from config.global_var import g
from src.page.base_page import BasePage, info
from src.testcase.base_step.commonsteps import CommonSteps
from src.utils.db_util import DBUtils
from src.utils.driver_util import get_config, get_browser





@pytest.fixture(scope='session', autouse=True)
def db_conn():
    g.config = get_config()
    # 获取数据库连接
    db = g.config['DEFAULT']['db']
    url = g.config[db]['url']
    user = g.config[db]['user']
    password = g.config[db]['password']
    g.db = DBUtils(url, user, password)

    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    print('before-size:%s-%s' % (width, height))
    set_windows_resolution(768, 1366)
    yield
    set_windows_resolution(1080, 1920)
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
    sql_path = g.root_path+'/data/'+current[2]+'/'+current[3].split('.')[0]+'.sql'
    if os.path.exists(sql_path):
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql = f.read()
            data = g.db.execute(sql)
    yield

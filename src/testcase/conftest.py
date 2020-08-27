# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:42
# @Author: fyl
# @File : conftest.py
import os
import re

import allure
import pytest
import win32api

from config.global_var import g
from src.page.base_page import info
from src.utils.common_util import DecoratorType
from src.utils.csv_util import data_reader
from src.utils.db_util import get_conn


@pytest.fixture(scope='session', autouse=True)
def setup():
    # 获取数据库连接
    get_conn()
    # 调整分辨率
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    print('before-size:%s-%s' % (width, height))
    if width == 1536 and height == 864:
        set_windows_resolution(768, 1366)
    yield
    if width == 1536 and height == 864:
        set_windows_resolution(1080, 1920)
    g.db.close_connection()
    info("关闭数据库连接")
    task_kill("IEDriverServer.exe")
    task_kill("iexplore.exe")
    info("关闭ie相关进程")


def set_windows_resolution(height, width):
    dm = win32api.EnumDisplaySettings(None, 0)
    dm.PelsHeight = height
    dm.PelsWidth = width
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 0
    win32api.ChangeDisplaySettings(dm, 0)


def task_kill(name):
    if os.system("tasklist |findstr {}".format(name)) == 0:
        os.system("taskkill /f /im {}".format(name))


@pytest.fixture(scope='class', autouse=True)
def restore_data():
    current = os.environ.get('PYTEST_CURRENT_TEST').split('/')
    test_dir = current[2]
    test_name = current[3].split('.')[0]
    sql_path = g.root_path + '/data/' + test_dir + '/' + test_name + '.sql'
    csv_path = test_dir + '/' + test_name + '.csv'
    g.db.test_name = test_name

    if os.path.exists(sql_path):
        restore_log('CURRENT_TEST:%s/%s 正在准备数据' % (test_dir, test_name))
        sql = get_sql(csv_path, sql_path)
        try:
            data = g.db.execute(sql)
            restore_log('CURRENT_TEST:%s/%s 准备数据成功' % (test_dir, test_name))
        except Exception as e:
            restore_log('CURRENT_TEST:%s/%s 准备数据失败。详细信息:%s' % (test_dir, test_name, e))
        # success = True
        # for sql in get_sql(csv_path, sql_path):
        #     try:
        #         data = g.db.execute(sql)
        #     except Exception as e:
        #         restore_log('CURRENT_TEST:%s/%s 准备数据失败。详细信息:%s' % (test_dir, test_name, e))
        #         success = False
        # if success:
        #     restore_log('CURRENT_TEST:%s/%s 准备数据成功' % (test_dir, test_name))
    else:
        restore_log('CURRENT_TEST:%s/%s 没有准备数据sql脚本文件' % (test_dir, test_name))
    yield


@allure.step("{log}")
def restore_log(log):
    info(log)


def get_sql(csv_path, sql_path):

    sql = ""
    with open(sql_path, 'r', encoding='utf-8') as f:
        if os.path.exists(csv_path):
            datas = data_reader(csv_path, DecoratorType.fixture)
            for line in f:
                if line.__contains__('{'):
                    params = re.findall(r"{(.*?)}", line)
                    for data in datas:
                        format_data = ""
                        for param in params:
                            format_data += "{0}='{1}',".format(param, data[param])
                        format_data = format_data[:-1]
                        sql += eval("line.format({})".format(format_data))
                        # yield eval("sql.format({})".format(format_data))
                # elif not sql.startswith('--') and sql.strip():  # 如果此行不以--开头，或不为空行
                #     yield sql
                else:
                    sql += line
        else:
            sql = f.read()
    return sql

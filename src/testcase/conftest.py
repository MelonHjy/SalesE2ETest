# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:42
# @Author: fyl
# @File : conftest.py
import os
import re
import traceback

import allure
import pytest
import win32api

from config.global_var import g
from src.page.base_page import info
from src.utils.common_util import DecoratorType, task_kill, set_windows_resolution, close_ie, write_properties
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
    write_properties(g.root_path + '/report/allure-results/environment.properties')
    info("生成环境配置信息文件")
    yield
    if width == 1536 and height == 864:
        set_windows_resolution(1080, 1920)
    g.db.close_connection()
    close_ie()


@pytest.fixture(scope='function')
def restore_data():
    current = os.environ.get('PYTEST_CURRENT_TEST').split('/')
    test_dir = current[2]
    test_name = current[3].split('.')[0]
    sql_path = '{}/data/{}/{}/{}.sql'.format(g.root_path, g.config['DEFAULT']['datafile'], test_dir, test_name)
    csv_path = '{}/data/{}/{}/{}.csv'.format(g.root_path, g.config['DEFAULT']['datafile'], test_dir, test_name)
    g.db.test_name = test_name

    if os.path.exists(sql_path):
        restore_log('CURRENT_TEST:%s/%s 正在准备数据' % (test_dir, test_name))
        # sql = get_sql(csv_path, sql_path)
        # data = g.db.execute(sql)
        # restore_log('CURRENT_TEST:%s/%s 准备数据成功' % (test_dir, test_name))
        for sql in get_sql(csv_path, sql_path):
            try:
                data = g.db.execute(sql)
            except Exception as e:
                restore_log('CURRENT_TEST:%s/%s 准备数据失败。详细信息:%s \n sql:%s' % (test_dir, test_name, e, sql))
        restore_log('CURRENT_TEST:%s/%s 准备数据完毕' % (test_dir, test_name))
    else:
        restore_log('CURRENT_TEST:%s/%s 没有准备数据sql脚本文件' % (test_dir, test_name))
    yield


@allure.step("{log}")
def restore_log(log):
    info(log)


def get_sql(csv_path, sql_path):
    # sql = ""
    with open(sql_path, 'r', encoding='utf-8') as f:
        if os.path.exists(csv_path):
            datas = data_reader(csv_path, DecoratorType.fixture)
            for line in f:
                if not is_valid_sql(line):
                    continue
                elif line.__contains__('{'):
                    yield format_sql(line, datas)
                    # sql += eval("line.format({})".format(format_data))
                else:
                    yield line
    #             else:
    #                 sql += line
    #     else:
    #         sql = f.read()
    # return sql


# def pytest_addoption(parser):
#     parser.addoption(
#         "--datafile", action="store", default="default", help="my option: default or haerbin"
#     )

# @pytest.fixture()
# def cmdopt(request):
#     g.dataFile = request.config.getoption("--datafile")

def is_valid_sql(sql):
    sql = sql.strip().lower()
    return sql and not (sql.startswith('--') or sql.startswith('/*')) and (sql.__contains__(
        'insert') or sql.__contains__('delete') or sql.__contains__('update') or sql.__contains__(
        'select'))


def format_sql(sql, datas):
    params = re.findall(r"{(.*?)}", sql)
    for data in datas:
        format_data = ""
        for param in params:
            format_data += "{0}='{1}',".format(param, data[param])
        format_data = format_data[:-1]
        return eval("sql.format({})".format(format_data))

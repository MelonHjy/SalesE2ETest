# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:42
# @Author: fyl
# @File : conftest.py
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from config.global_var import g
from src.page.base_page import BasePage, info
from src.testcase.base_step.commonsteps import CommonSteps
from src.utils.db_util import DBUtils
from src.utils.driver_util import get_config, get_browser

# g.config = get_config()
# # 获取数据库连接
# db = g.config['DEFAULT']['db']
# url = g.config[db]['url']
# user = g.config[db]['user']
# password = g.config[db]['password']
# g.db = DBUtils(url, user, password)
#
#
#
# @pytest.fixture(scope='session', autouse=True)
# def db_conn():
#     print('qwe123123qwe')
#     yield
#     print('qweqwe')
#     # g.db.close_connection()

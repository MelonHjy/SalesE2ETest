# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:42
# @Author: fyl
# @File : conftest.py
import os
import random

import allure
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from config.global_var import g
from src.page.base_page import BasePage, info
from src.testcase.base_step.commonsteps import CommonSteps
from src.testcase.conftest import task_kill
from src.utils import csv_util
from src.utils.create_identity import IdNumber
from src.utils.driver_util import get_config, get_browser


@pytest.fixture(scope="class", autouse=False)
@allure.severity('blocker')
def login_jiangsu_p():
    get_config_content()
    CommonSteps().login_p()
    yield
    BasePage().close_browser()


@pytest.fixture(scope="function", autouse=False)
@allure.severity('blocker')
def login_jiangsu_p_fun():
    get_config_content()
    CommonSteps().login_p()
    yield
    BasePage().close_browser()

# @pytest.fixture(scope="function",autouse=False)
# def flash_idcard():
#     current = os.environ.get('PYTEST_CURRENT_TEST').split('/')
#     test_dir = current[2]
#     test_name = current[3].split('.')[0]
#     csv_path = g.root_path + '/data/' + test_dir + '/' + test_name + '.csv'
#     data = csv_util.data_reader(csv_path,ignore_heads=False)
#     random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
#     new_id = IdNumber.generate_id(random_sex)  # 随机生成身份证号
#     account_no = new_id[0:13]
#     edit_data_dict = [("idCard", new_id),("accountno",account_no)]
#     csv_util.data_edit(data, csv_path, edit_data_dict)
#     info("刷新{0}的身份证{1}，银行账号{2}".format(test_name,new_id,account_no))
#     yield


def get_config_content():
    # g.config = get_config()
    url = g.config['DEFAULT']['url']
    browser = g.config['DEFAULT']['browser']
    g.driver = get_browser(browser)
    g.wait = WebDriverWait(g.driver, 60)
    BasePage().maximize_window()
    info("进入%s", url)
    BasePage().open_url(url)

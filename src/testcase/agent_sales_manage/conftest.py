# -*- coding:utf-8 -*-
#@Time : 2020/6/30 13:42
#@Author: fyl
#@File : conftest.py
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from config.global_var import g
from src.page.base_page import BasePage, info
from src.testcase.base_step.commonsteps import CommonSteps
from src.utils.driver_util import get_config, get_browser


@pytest.fixture(scope="function", autouse=False)
@allure.severity('blocker')
def login_jiangsu_p():
    g.config = get_config()
    url = g.config['DEFAULT']['url']
    browser = g.config['DEFAULT']['browser']
    g.driver = get_browser(browser)
    g.wait = WebDriverWait(g.driver, 120)
    BasePage().maximize_window()
    info("进入%s", url)
    BasePage().open_url(url)
    CommonSteps().login_p()
    yield
    BasePage().close_browser()
# -*- coding: utf-8 -*-#
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.utils.high_light_element import high_light
from config.global_var import *
import random
from src.utils.log import *
from src.utils.driver_util import set_wait
from src.utils.except_util import catch_except
from selenium import webdriver
from os import path, remove


class BasePage:
    # ------------------------  菜单 ------------------------#

    # 三农模块
    snmk = "//li[@class='m1_4']/a[text()='三农模块']"
    # 经营机构模块
    jyjg = "//li[@class='m1_4']/a[text()='经营机构']"
    # 直销渠道模块
    zxqd = "//li[@class='m1_4']/a[text()='直销渠道']"
    # 个代渠道模块
    gdqd = "//li[@class='m1_4']/a[text()='个代渠道']"
    # 农村保险事业部模块
    ncbxsyb = "//li[@class='m1_7']/a[text()='农村保险事业部']"
    # 登录日志查询模块
    dlrzcx = "//li[@class='m1_6']/a[text()='登录日志查询']"
    # 经代渠道模块
    jdqd = "//li[@class='m1_4']/a[text()='经代渠道']"
    # 银保渠道模块
    ybqd = "//li[@class='m1_4']/a[text()='银保渠道']"
    # 车商渠道模块
    csqd = "//li[@class='m1_4']/a[text()='车商渠道']"
    # 综合管理模块
    zhgl = "//li[@class='m1_4']/a[text()='综合管理']"
    #--------------展开------------#
    #销售团队展开
    xstdzk = "//td[@id='ygtvt356']"
    #销售人员展开
    xsryzk = "//td[@id='ygtvt362']"
    #--------------子菜单----------#
    #代理制销售人员代码管理
    dlzxsrydmgl = "//a[@id='ygtvlabelel363']"

    # ------------------------  页面元素 ------------------------#





    # ------------------------  常用操作封装 ------------------------#

    #页面切换
    # 进入第一层iFrame
    def switch_to_first_iFrame(self, first_iFrame_id):
        self.switch_to_default_content()
        self.select_frame_id(first_iFrame_id)

    # ------------------------  同名api ------------------------#

    @catch_except
    def click(self, el):
        sleep(0.5)
        el.click()

    @catch_except
    def wait_until_el_xpath(self, xpath):
        el = g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        sleep(0.5)
        high_light(element=el)
        return el

    @catch_except
    def wait_until_els_xpath(self, xpath):
        return g.wait.until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))


    @catch_except
    def close_browser(self):
        sleep(0.5)
        g.driver.quit()

    @catch_except
    def choose_ok_on_alert(self):
        sleep(3)
        alter = g.driver.switch_to.alert
        sleep(3)
        alter.accept()
        sleep(1)

    @catch_except
    def clear(self, el):
        el.clear()

    @catch_except
    def send_keys(self, el, value):
        el.send_keys(value)

    @set_wait(1)
    def is_element_exist(self, xpath):
        try:
            el = g.wait.until(
                expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
            high_light(element=el)
            return True
        except BaseException:
            return False

    @catch_except
    def get_text(self, el):
        return el.text

    @catch_except
    def get_element_xpath(self, xpath):
        el = g.driver.find_element_by_xpath(xpath)
        high_light(element=el)
        return el

    @catch_except
    def right_click(self, xpath):
        right_click = g.driver.find_element_by_xpath(xpath)
        high_light(element=right_click)
        ActionChains(g.driver).context_click(right_click).perform()

    @catch_except
    def is_selected(self, xpath):
        el = g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))).is_selected()
        high_light(element=el)
        return el

    @catch_except
    def open_url(self, url):
        g.driver.get(url)
        handles = g.driver.window_handles
        g.driver.switch_to.window(handles[-1])

    @catch_except
    def double_click(self, double_click_el):
        ActionChains(g.driver).double_click(double_click_el).perform()

    @catch_except
    def move_to_el(self, el):
        webdriver.ActionChains(g.driver).move_to_element(el).perform()

    @catch_except
    def active_el(self):
        return g.driver.switch_to.active_element

    @catch_except
    def switch_to_default_content(self):
        g.driver.switch_to.default_content()

    @catch_except
    def select_frame_id(self, id):
        g.driver.switch_to.frame(id)

    @catch_except
    def maximize_window(self):
        g.driver.maximize_window()

    # ------------------------  assert api ------------------------#

    # 断言方法
    def assertEqual(self, message, actual, expect):
        pytest.assume(actual == expect)
        info('message-->{0},actual-->{1},expect-->{2}'.format(message, actual, expect))

    def assertResult(self, message, result):
        pytest.assume(result)
        info('message-->{0},result-->{1}'.format(message, result))

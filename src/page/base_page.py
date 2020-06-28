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


    # ------------------------  页面元素 ------------------------#

    username_path = "//input[@id='username1']"
    pwd_xpath = "//input[@id='password1']"
    login = "//input[@id='button']"
    #经营机构模块
    jyjg_xpath = "//li[@class='m1_4']/a[text()='经营机构']"
    #销售人员前的加号
    xsry_xpath = "//td[@id='ygtvt9']"

    # ------------------------  常用操作封装 ------------------------#



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
            g.wait.until(
                expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
            return True
        except BaseException:
            return False

    @catch_except
    def get_text(self, el):
        return el.text

    @catch_except
    def get_element_xpath(self, xpath):
        return g.driver.find_element_by_xpath(xpath)

    @catch_except
    def right_click(self, xpath):
        right_click = g.driver.find_element_by_xpath(xpath)
        ActionChains(g.driver).context_click(right_click).perform()

    @catch_except
    def is_selected(self, xpath):
        return g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))).is_selected()

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

    # ------------------------  assert api ------------------------#

    # 断言方法
    def assertEqual(self, message, actual, expect):
        pytest.assume(actual == expect)
        info('message-->{0},actual-->{1},expect-->{2}'.format(message, actual, expect))

    def assertResult(self, message, result):
        pytest.assume(result)
        info('message-->{0},result-->{1}'.format(message, result))

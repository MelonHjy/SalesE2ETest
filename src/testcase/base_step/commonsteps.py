# -*- coding:utf-8 -*-
#@Time : 2020/6/30 13:57
#@Author: fyl
#@File : commonsteps.py
from config.constants import Constants
from src.page.base_page import BasePage
from src.utils.log import info


class CommonSteps():

    #登录名输入框
    username = "//input[@id='username1']"
    #密码输入框
    pwd = "//input[@id='password1']"
    #登录按钮
    login_btn = "//input[@id='button']"

    base_page = BasePage()
    cons = Constants()

    def login_p(self):
        username = self.base_page.wait_until_el_xpath(self.username)
        self.base_page.send_keys(username, self.cons.JIANGSU_PROVINCE_USERNAME)
        password = self.base_page.wait_until_el_xpath(self.pwd)
        self.base_page.send_keys(password, self.cons.JIANGSU_PROVINCE_PASSWORD)
        login_b = self.base_page.wait_until_el_xpath(self.login_btn)
        info("登录账号：{0}，密码：{1}".format(self.cons.JIANGSU_PROVINCE_USERNAME, self.cons.JIANGSU_PROVINCE_PASSWORD))
        self.base_page.click(login_b)

    def login_c(self):
        username = self.base_page.wait_until_el_xpath(self.username)
        self.base_page.send_keys(username, self.cons.NANJING_CITY_USERNAME)
        password = self.base_page.wait_until_el_xpath(self.pwd)
        self.base_page.send_keys(password, self.cons.NANJING_CITY_PASSWORD)
        login_b = self.base_page.wait_until_el_xpath(self.login_btn)
        info("登录账号：{0}，密码：{1}".format(self.cons.NANJING_CITY_USERNAME, self.cons.NANJING_CITY_PASSWORD))
        self.base_page.click(login_b)

    def login(self):
        username = self.base_page.wait_until_el_xpath(self.username)
        self.base_page.send_keys(username, self.cons.NANJING_USERNAME)
        password = self.base_page.wait_until_el_xpath(self.pwd)
        self.base_page.send_keys(password, self.cons.NANJING_PASSWORD)
        login_b = self.base_page.wait_until_el_xpath(self.login_btn)
        info("登录账号：{0}，密码：{1}".format(self.cons.NANJING_USERNAME, self.cons.NANJING_PASSWORD))
        self.base_page.click(login_b)
# -*- coding:utf-8 -*-
# @Time : 2020/6/30 13:57
# @Author: fyl
# @File : commonsteps.py
import sys
from time import sleep

from config.constants import Constants
from src.page.base_page import BasePage
from src.utils import csv_util
from src.utils.driver_util import set_wait
from src.utils.log import info


# class base_test():
#     data = None
#
#     @classmethod
#     def get_data(cls):
#         a= cls.__class__
#         b=a.__name__
#         c=cls.__name__
#         cls.data = csv_util.data_reader(b)
#         return cls.data

class CommonSteps:
    # 登录名输入框
    username = "//input[@id='username1']"
    # 密码输入框
    pwd = "//input[@id='password1']"
    # 登录按钮
    login_btn = "//input[@id='button']"

    base_page = BasePage()
    cons = Constants()

    def login_p(self):
        self.login_base(self.cons.JIANGSU_PROVINCE_USERNAME, self.cons.JIANGSU_PROVINCE_PASSWORD)

    def login_c(self):
        self.login_base(self.cons.NANJING_CITY_USERNAME, self.cons.NANJING_CITY_PASSWORD)

    def login(self):
        self.login_base(self.cons.NANJING_USERNAME, self.cons.NANJING_PASSWORD)

    @set_wait(60)
    def login_base(self, user_name, pwd):
        username = self.base_page.wait_until_el_xpath(self.username)
        self.base_page.send_keys(username, user_name)
        password = self.base_page.wait_until_el_xpath(self.pwd)
        self.base_page.send_keys(password, pwd)
        login_b = self.base_page.wait_until_el_xpath(self.login_btn)
        info("登录账号：{0}，密码：{1}".format(user_name, pwd))
        self.base_page.click(login_b)

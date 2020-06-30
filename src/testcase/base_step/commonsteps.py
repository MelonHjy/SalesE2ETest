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
    login = "//input[@id='button']"

    def login_p(self):
        base_page = BasePage()
        cons = Constants()
        username = base_page.wait_until_el_xpath(self.username)
        base_page.send_keys(username, cons.JIANGSU_PROVINCE_USERNAME)
        password = base_page.wait_until_el_xpath(self.pwd)
        base_page.send_keys(password, cons.JIANGSU_PROVINCE_PASSWORD)
        login = base_page.wait_until_el_xpath(self.login)
        info("登录账号：{0}，密码：{1}".format(cons.JIANGSU_PROVINCE_USERNAME,cons.JIANGSU_PROVINCE_PASSWORD))
        base_page.click(login)

#  -*- coding:utf-8 -*-
# @Time : 2020/7/30 14:03
# @Author: fyl
# @File : sales_query.py
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class SalesQuery(TablePage):
    user_code = "//input[@id='userCode']"
    query_btn = "//input[@value='查询']"

    def into_page(self):
        self.to_main_page("个代渠道", "销售人员", "销售人员查询")

    def query(self, user_code1):
        self.click(self.wait_until_el_xpath(self.user_code))
        self.send_keys(self.wait_until_el_xpath(self.user_code), user_code1)
        self.click(self.wait_until_el_xpath(self.query_btn))
        sleep(3)

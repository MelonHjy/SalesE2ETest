#  -*- coding:utf-8 -*-
# @Time : 2020/7/29 15:25
# @Author: fyl
# @File : main_group_query.py   综合管理->销售团队->团队查询
import allure

from src.page.table_page import TablePage


class GroupQuery(TablePage):
    group_name = "//input[@id='groupName']"
    query_btn = "//input[@value='查询']"


    @allure.step("综合管理->销售团队->团队查询")
    def into_page(self):
        self.to_main_page("综合管理", "销售团队", "团队查询")

    def query(self, group_name):
        self.click(self.wait_until_el_xpath(self.group_name))
        self.send_keys(self.wait_until_el_xpath(self.group_name), group_name)
        self.click(self.wait_until_el_xpath(self.query_btn))



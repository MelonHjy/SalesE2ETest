#  -*- coding:utf-8 -*-
# @Time : 2020/7/29 15:25
# @Author: fyl
# @File : main_group_query.py   综合管理->销售团队->团队查询
import allure

from src.page.table_page import TablePage


class GroupQuery(TablePage):
    group_name = "//input[@id='groupName']"
    query_btn = "//input[@value='查询']"

    def into_page(self):
        self.to_main_page("综合管理", "销售团队", "团队查询")
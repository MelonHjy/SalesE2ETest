#  -*- coding:utf-8 -*-
# @Time : 2020/8/27 15:52
# @Author: fyl
# @File : main_commission_edit.py
from src.page.agency_module.common_main_page import CommonMainPage


class MainCommisson_edit(CommonMainPage):
    rule_no = "//*[@id='ruleno']"

    def into_page(self,module_menu):
        self.to_main_page(module_menu,"中介机构","佣金比例上限标准查询修改")

    def query(self,rule_no):
        self.send_keys(self.get_element_xpath(self.rule_no), rule_no)
        self.click_btn("查询")
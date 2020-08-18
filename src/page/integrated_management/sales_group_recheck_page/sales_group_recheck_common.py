#  -*- coding:utf-8 -*-
# @Time : 2020/8/17 15:44
# @Author: fyl
# @File : sales_group_recheck_common.py
from src.page.process_page import ProcessPage


class SalesGroupRecheckCommon(ProcessPage):

    case = "//*[@class='case']"
    recheck_btn = "//*[@id='toHRFarm']"

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))
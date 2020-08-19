#  -*- coding:utf-8 -*-
# @Time : 2020/8/18 11:55
# @Author: fyl
# @File : zt_group_approval.py  综拓审批页
from src.page.process_page import ProcessPage


class ZtGroupApproval(ProcessPage):

    case = "//*[@class='case']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    approval_btn = "//*[@id='addFarm']"

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))
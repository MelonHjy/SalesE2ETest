#  -*- coding:utf-8 -*-
# @Time : 2020/8/17 13:40
# @Author: fyl
# @File : group_issue_manage_common.py
import allure

from src.page.process_page import ProcessPage


class GroupIssueManageCommon(ProcessPage):

    case = "//*[@class='case']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def get_head_text(self):
        return self.get_text(self.get_element_xpath(self.case))


#  -*- coding:utf-8 -*-
# @Time : 2020/8/6 14:03
# @Author: fyl
# @File : group_issue_recheck.py   团队成员出单权赋予复核页面
import allure

from config.global_var import sleep
from src.page.base_page import BasePage
from src.page.process_page import ProcessPage


class GroupIssueRecheck(ProcessPage):
    case = "//*[@class='case']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    success = "//*[@id='success']"  #复核按钮
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功
    submit_close = "//*[@class='button_ty_over']"

    # ---------------------人员基础信息填写项------------------------------ #
    user_tab = "//*[@id='folder-label-userTab']"

    # 双击选择框


    # ---------------------合同信息填写项------------------------------ #
    contract_tab = "//*[@id='folder-label-contractTab']"

    # 增加资质信息中的各项

    # 合同基本信息中的各项

    # 账户信息中的各项

    def get_head_text(self):
        return self.get_text(self.get_element_xpath(self.case))

    def recheck_ope(self, check_state="", textarea=""):
        """
        点击复核的后续操作
        """
        self.click(self.wait_until_el_xpath(self.success))
        self.submit_interaction(iframe_xpath=self.submit_iframe, check_state=check_state, textarea=textarea)


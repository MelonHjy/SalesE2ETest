#  -*- coding:utf-8 -*-
# @Time : 2020/8/6 15:59
# @Author: fyl
# @File : appointment_manager_recheck.py    营销团队经理聘任与解聘复核
import allure

from src.page.process_page import ProcessPage


class DismissalManagerRecheck(ProcessPage):
    case = "//*[@class='case']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    success = "//*[@id='success']"  # 复核按钮
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))

    def recheck_ope(self, check_state="", textarea=""):
        """
        点击复核的后续操作
        """
        self.click(self.wait_until_el_xpath(self.success))
        self.submit_interaction(iframe_xpath=self.submit_iframe, check_state=check_state, textarea=textarea)

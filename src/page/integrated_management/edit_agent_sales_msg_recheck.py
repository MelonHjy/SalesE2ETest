#  -*- coding:utf-8 -*-
# @Time : 2020/8/4 14:27
# @Author: fyl
# @File : edit_agent_sales_msg_recheck.py
import allure
from selenium.webdriver.common.keys import Keys

from config.global_var import sleep
from src.page.process_page import ProcessPage


class EditAgentSaleMsgRecheck(ProcessPage):
    case = "//*[@class='case']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    success = "//*[@id='success']"  # 复核按钮
    save_success = "//body/table/tbody/tr/td[2]"  # 保存成功

    # ---------------------人员基础信息填写项------------------------------ #
    user_tab = "//*[@id='folder-label-userTab']"


    # ---------------------合同信息填写项------------------------------ #
    contract_tab = "//*[@id='folder-label-contractTab']"

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))

    @allure.step("切换到合同信息")
    def switch_contract_tab(self):
        self.click(self.wait_until_el_xpath(self.contract_tab))

    @allure.step("切换到人员基础信息")
    def switch_user_tab(self):
        self.click(self.wait_until_el_xpath(self.user_tab))

    def recheck_ope(self, check_state="", textarea=""):
        """
        点击复核的后续操作
        """
        self.click(self.wait_until_el_xpath(self.success))
        self.submit_interaction(iframe_xpath=self.submit_iframe, check_state=check_state, textarea=textarea)
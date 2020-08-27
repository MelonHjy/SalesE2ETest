#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:06
# @Author: fyl
# @File : main_channel_type_code_approval.py  渠道类型码审批
import allure

from config.global_var import sleep
from src.page.agency_module.common_main_page import CommonMainPage


class MainChannelTypeCodeApproval(CommonMainPage):
    agent_type = "//*[@id='condition.agentType']"  # 渠道类型码
    agent_type_name = "//*[@id='condition.agentTypeName']"  # 渠道类型码名称
    status = "//*[@id='state{}1']"  # 状态

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "渠道类型码审核")

    @allure.step("查询")
    def query(self, agent_type=None, agent_type_name=None, status="100"):
        """
        contract_no:合同编号
        status：任务状态
        """
        if agent_type:
            self.send_keys(self.wait_until_el_xpath(self.agent_type), agent_type)
        if agent_type_name:
            self.send_keys(self.wait_until_el_xpath(self.agent_type_name), agent_type_name)
        j = 1
        for i in status:
            el = self.wait_until_el_xpath(self.status.format(j))
            if (el.is_selected() == False and i == "1") or (el.is_selected() and i == "0"):
                self.click(el)
            j = j + 1
        self.click_btn("查询")
        sleep(2)

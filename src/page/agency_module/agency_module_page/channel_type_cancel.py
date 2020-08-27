#  -*- coding:utf-8 -*-
# @Time : 2020/8/25 2:43
# @Author: fyl
# @File : channel_type_cancel.py    渠道类型码作废
from src.page.agency_module.common_main_page import CommonMainPage


class ChannelTypeCancel(CommonMainPage):
    agent_type = "//*[@id='condition.agentType']"
    agent_type_name = "//*[@id='condition.agentTypeName']"
    new_agent_type = "//*[@id='condition.newAgentType']"
    cancel_agent_type = "//*[@id='cancelAgentType']"    # 作废
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "渠道类型码作废")

    def query(self,agent_type=None,agent_type_name=None,new_agent_type=None):
        if agent_type:
            self.send_keys(self.wait_until_el_xpath(self.agent_type),agent_type)
        if agent_type_name:
            self.send_keys(self.wait_until_el_xpath(self.agent_type_name),agent_type_name)
        if new_agent_type:
            self.send_keys(self.wait_until_el_xpath(self.new_agent_type),new_agent_type)
        self.click_btn("查询")

    def close_button_ty(self):
        self.click(self.wait_until_el_xpath("//input[@class='button_ty']"))
#  -*- coding:utf-8 -*-
# @Time : 2020/8/26 15:50
# @Author: fyl
# @File : main_channel_type_code_edit.py    渠道类型码修改
from src.page.agency_module.common_main_page import CommonMainPage


class MainChannelTypeCodeEdit(CommonMainPage):

    agent_type = "//*[@id='condition.agentType']"   # 渠道类型码
    agent_type_name = "//*[@id='condition.agentTypeName']"    #   渠道类型码名称

    def query(self,agent_type=None, agent_type_name=None):
        if agent_type:
            self.send_keys(self.wait_until_el_xpath(self.agent_type),agent_type)
        if agent_type_name:
            self.send_keys(self.wait_until_el_xpath(self.agent_type_name),agent_type_name)
        self.click_btn("查询")

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "渠道类型码修改")
#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 20:27
# @Author: fyl
# @File : main_channel_type_code_query.py   渠道类型码查询
from src.page.agency_module.common_main_page import CommonMainPage


class MainChannelTypeCodeQuery(CommonMainPage):
    query_data = "//*[@id='yui-dt-table0']/tbody[1]/tr/td"
    agent_type = "//*[@id='condition.agentType']"   # 渠道类型码
    agent_type_name = "//*[@id='condition.agentTypeName']"  # 渠道类型码名称

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "渠道类型码查询")


    def table_cell_text(self, head, text):
        list = self.get_cell_text_by_head(head)
        for i in list:
            if i != text:
                return False
        return True


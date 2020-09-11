#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 13:44
# @Author: fyl
# @File : main_agency_org_query.py  中介机构查询
import allure

from config.global_var import sleep
from src.page.agency_module.common_main_page import CommonMainPage
from src.page.table_page import TablePage


class MainAgencyOrgQuery(CommonMainPage):
    query_btn = "//input[@id='qubtn']"  # 按钮
    contract_no = "//*[@id='condition.contractNo']" # 合同号
    query_data = "//*[@id='yui-dt-table0']/tbody[1]/tr/td"

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "中介机构查询")





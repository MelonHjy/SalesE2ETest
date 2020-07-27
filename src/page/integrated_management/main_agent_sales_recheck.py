#  -*- coding:utf-8 -*-
# @Time : 2020/7/23 17:43
# @Author: fyl
# @File : main_agent_sales_recheck.py #代理制销售人员代码复核
import allure

from config.global_var import sleep
from src.page.process_page import ProcessPage
from src.page.table_page import TablePage


class AgentSalesRecheck(TablePage, ProcessPage):
    user_code = "//input[@id='userCode']"  # 人员代码
    status = "//label[contains(text(),'{}')]"
    query_btn = "//input[@value='查询']"
    manage_flag_select = "//select[@id='manageFlag']"
    identify_number_input = "//input[@id='identifyNumber']"

    @allure.step("综合管理->销售人员->代理制销售人员代码复核")
    def into_page(self):
        self.to_main_page("综合管理", "销售人员", "代理制销售人员代码复核")

    @allure.step("查询")
    def query(self, user_code1, status="未提交", manage_flag='', identify_number=''):
        """
        user_code1:人员代码
        status：任务状态
        manage_flag：审核状态
        identify_number:身份证号
        """
        self.click(self.wait_until_el_xpath(self.user_code))
        self.send_keys(self.wait_until_el_xpath(self.user_code), user_code1)
        self.click(self.wait_until_el_xpath(self.status.format(status)))
        if identify_number != '':
            self.send_keys(self.identify_number_input, identify_number)
        if manage_flag != '':
            self.select(self.manage_flag_select, manage_flag)
        self.click(self.wait_until_el_xpath(self.query_btn))
        sleep(3)

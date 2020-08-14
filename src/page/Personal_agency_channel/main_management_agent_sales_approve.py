#  -*- coding:utf-8 -*-
# @Time : 2020/7/30 10:36
# @Author: fyl
# @File : main_management_agent_sales_approve.py    综合管理->销售团队->团队查询
import allure

from src.page.process_page import ProcessPage
from src.page.table_page import TablePage


class ManagementAgentSalesApprove(TablePage, ProcessPage):
    user_code = "//input[@id='userCode']"  # 人员代码
    query_btn = "//input[@value='查询']"  # 查询
    status = "//label[contains(text(),'{}')]"  # 状态
    success_btn = "//input[@id='success']"  # 审核
    submit_iframe = "//iframe[@name='submitFrame']"

    def into_page(self):
        self.to_main_page("个代渠道", "销售人员", "代理制销售人员代码审批")

    @allure.step("根据人员代码：{user_code1}->进行查询")
    def query(self, user_code1, status='未提交'):
        self.click(self.wait_until_el_xpath(self.user_code))
        self.send_keys(self.wait_until_el_xpath(self.user_code), user_code1)
        self.click(self.wait_until_el_xpath(self.status.format(status)))
        self.click(self.wait_until_el_xpath(self.query_btn))

    def select_data(self, status_text):
        """
        根据查询的数据状态选择该条数据（前提：查询是通过人员代码查询数据）
        status_text：需要选择的审核状态
        """
        status_list = self.get_cell_text_by_head('审核状态')
        index = status_list.index(status_text)
        self.click(self.get_a_by_head(index, '操作'))

    def approve(self):
        """
        点击审核
        """
        self.click(self.wait_until_el_xpath(self.success_btn))

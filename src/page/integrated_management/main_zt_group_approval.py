#  -*- coding:utf-8 -*-
# @Time : 2020/8/18 11:40
# @Author: fyl
# @File : main_zt_group_approval.py   综拓团队审批
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class MainZtGroupApproval(TablePage):
    group_name = "//*[@id='groupName']"
    status = "//label[contains(text(),'{}')]"  # 状态
    query_btn = "//input[@value='查询']"  # 查询

    def into_page(self):
        self.to_main_page("综合管理", "综拓团队管理", "综拓团队审批")

    @allure.step("查询")
    def query(self, group_name, status="未提交", manage_flag=None, identify_number=None):
        """
        user_code1:人员代码
        status：任务状态
        manage_flag：审核状态
        identify_number:身份证号
        """
        self.click(self.wait_until_el_xpath(self.group_name))
        self.send_keys(self.wait_until_el_xpath(self.group_name), group_name)
        self.click(self.wait_until_el_xpath(self.status.format(status)))
        self.click(self.wait_until_el_xpath(self.query_btn))
        sleep(3)

    def select_data(self, status_text):
        """
        根据查询的数据状态选择该条数据
        status_text：需要选择的审核状态
        """
        status_list = self.get_cell_text_by_head('审核状态')
        index = status_list.index(status_text)
        self.click(self.get_a_by_head(index, '操作'))

    def switch_max_window(self):
        self.switch_to_window()
        self.maximize_window()
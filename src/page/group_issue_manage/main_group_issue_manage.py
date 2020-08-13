#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:54
# @Author: fyl
# @File : main_group_issue_manage.py    团队出单权管理
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class MainGroupIssueManage(TablePage):

    input_btn = "//input[@value='{}']"  # 按钮

    def into_page(self):
        self.to_main_page("经营机构", "销售团队", "团队出单权管理")

    @allure.step("点击{btn_text}")
    def click_btn(self, btn_text):
        self.click(self.wait_until_el_xpath(self.input_btn.format(btn_text)))
        sleep(2)

    def switch_max_window(self):
        self.switch_to_window()
        self.maximize_window()

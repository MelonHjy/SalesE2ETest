#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 20:10
# @Author: fyl
# @File : common_main_page.py
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class CommonMainPage(TablePage):
    case = "//*[@class='case']"
    input_btn = "//input[@value='{}']"  # 按钮

    @allure.step("点击{btn_text}")
    def click_btn(self, btn_text):
        self.click(self.wait_until_el_xpath(self.input_btn.format(btn_text)))
        sleep(2)

    def switch_max_window(self):
        self.switch_to_window()
        self.maximize_window()

    def select_data(self, column_name, column_value, row_ope, num=1):
        """
        根据指定列中指定的值获取该行数据，并对该行数据进行操作
        column_name：列名
        column_value：该列所指定的值
        row_ope：对该行进行点击的列名
        """
        status_list = self.get_cell_text_by_head(column_name)
        index = status_list.index(column_value)
        self.click(self.get_a_by_head(index, row_ope, num))

    def get_head_text(self):
        return self.get_text(
            self.wait_until_el_xpath(self.case))

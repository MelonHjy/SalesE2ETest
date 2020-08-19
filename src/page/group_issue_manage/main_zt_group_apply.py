#  -*- coding:utf-8 -*-
# @Time : 2020/8/18 1:42
# @Author: fyl
# @File : main_zt_group_apply.py    综拓团队申请
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class MainZtGroupApply(TablePage):

    case = "//*[@class='case']"
    com_code = "//*[@id='comCode']" #上级机构
    pk_deptdoc = "//*[@id='pk_deptdoc']"    # 团队代码
    group_name = "//*[@id='groupName']" # 团队名称
    status = "//input[@id='state1{}']"  # 任务状态
    input_btn = "//input[@value='{}']"  # 按钮

    def into_page(self):
        self.to_main_page("经营机构", "销售团队", "综拓团队申请")

    @allure.step("根据团队->查询")
    def query(self, group_name=None, pk_deptdoc=None, status="100"):
        """
        group_name:团队名称
        status：任务提交：0->未选定）,1->被选定，未提交，已提交，被打回
        """
        if group_name:
            self.click(self.wait_until_el_xpath(self.group_name))
            self.send_keys(self.wait_until_el_xpath(self.group_name), group_name)
        if pk_deptdoc:
            self.click(self.wait_until_el_xpath(self.pk_deptdoc))
            self.send_keys(self.wait_until_el_xpath(self.pk_deptdoc), pk_deptdoc)
        j = 0
        for i in status:
            el = self.wait_until_el_xpath(self.status.format(j))
            if (el.is_selected() == False and i == "1") or (el.is_selected() and i == "0"):
                self.click(el)
            j = j + 1
        self.click(self.wait_until_el_xpath(self.input_btn.format("查询")))
        sleep(2)

    def select_data(self, column_name, column_value, row_ope):
        """
        根据指定列中指定的值获取该行数据，并对该行数据进行操作
        column_name：列名
        column_value：该列所指定的值
        row_ope：对该行进行点击的列名
        """
        status_list = self.get_cell_text_by_head(column_name)
        index = status_list.index(column_value)
        self.click(self.get_a_by_head(index, row_ope))

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))
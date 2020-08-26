#  -*- coding:utf-8 -*-
# @Time : 2020/8/19 15:49
# @Author: fyl
# @File : main_agency_org_manage.py   中介机构新增和变更申报
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class MainAgencyOrgManage(TablePage):
    case = "//*[@class='case']"
    contractType = "//*[@id='condition.contractType']"
    status = "//input[@id='state{}']"  # 任务状态
    input_btn = "//input[@value='{}']"  # 按钮
    contract_no = "//*[@id='condition.contractNo']"
    # 部门类型
    apartment_type = "//*[contains(text(), '部门类型')]/../td[2]/div[contains(@style,'DISPLAY: inline')]/div[contains(@style,'DISPLAY: inline')]/input"
    query_data = "//*[@id='yui-dt-table0']/tbody[1]/tr/td"

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "中介机构新增和变更申报")
        self.assertEqual("验证页面标题", self.get_text(self.wait_until_el_xpath(self.case)), "中介机构新增和变更申报")

    @allure.step("点击{btn_text}")
    def click_btn(self, btn_text):
        self.click(self.wait_until_el_xpath(self.input_btn.format(btn_text)))
        sleep(2)

    @allure.step("查询")
    def query(self, contract_no, contractType=None, apartment_type='0', status="100"):
        """
        contractType:合同/协议类型
        status：任务提交：0->未选定）,1->被选定，未提交，已提交，被打回
        """
        self.select(self.contractType, contractType)
        if apartment_type == '1':
            self.click(self.wait_until_el_xpath(self.apartment_type))
        if contract_no:
            self.send_keys(self.wait_until_el_xpath(self.contract_no), contract_no)
        j = 0
        for i in status:
            if j == 2:
                j = j + 1
            el = self.wait_until_el_xpath(self.status.format(j))
            if (el.is_selected() == False and i == "1") or (el.is_selected() and i == "0"):
                self.click(el)
            j = j + 1
        self.click_btn("查询")
        sleep(5)

    def table_cell_text(self, head, text):
        list = self.get_cell_text_by_head(head)
        for i in list:
            if i != text:
                return False
        return True

    def switch_max_window(self):
        self.switch_to_window()
        self.maximize_window()

    def get_head_text(self):
        return self.get_text(
            self.wait_until_el_xpath(self.case))

    def is_selected(self, status):
        return self.get_element_xpath(self.status.format(status)).is_selected()

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

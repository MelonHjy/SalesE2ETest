#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 16:06
# @Author: fyl
# @File : main_agency_org_approval.py     中介机构审批
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class MainAgencyOrgApproval(TablePage):
    case = "//*[@class='case']"
    input_btn = "//input[@value='{}']"  # 按钮
    status = "//*[contains(text(),'未提交')]/input[@value='{}']"  # 状态
    contract_no = "//*[@id='condition.contractNo']"  # 合同编号
    contractType = "//*[@id='condition.contractType']"  # 合同类型
    # 部门类型
    apartment_type = "//*[contains(text(), '部门类型')]/../td[2]/div[contains(@style,'DISPLAY: inline')]/div[contains(@style,'DISPLAY: inline')]/input"

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "中介机构审批")
        self.assertEqual("验证页面标题", self.get_text(self.wait_until_el_xpath(self.case)), "中介机构审批")

    @allure.step("点击{btn_text}")
    def click_btn(self, btn_text):
        self.click(self.wait_until_el_xpath(self.input_btn.format(btn_text)))
        sleep(2)

    @allure.step("查询")
    def query(self, contract_no, contractType=None, status="未提交"):
        """
        contract_no:合同编号
        status：任务状态

        """
        if contractType:
            self.select(self.contractType, contractType)
            self.click(self.get_element_xpath(self.apartment_type))
        status_list = {"未提交": "1", "已提交": "2", "被打回": "3"}
        self.send_keys(self.wait_until_el_xpath(self.contract_no), contract_no)
        self.click(self.wait_until_el_xpath(self.status.format(status_list[status])))
        self.click_btn("查询")
        sleep(3)

    @allure.step("选择数据")
    def select_data(self, status_text):
        """
        根据查询的数据状态选择该条数据（前提：查询是通过人员代码查询数据）
        status_text：需要选择的审核状态
        """
        status_list = self.get_cell_text_by_head('审核状态')
        index = status_list.index(status_text)
        self.click(self.get_a_by_head(index, '操作'))

    def switch_max_window(self):
        self.switch_to_window()
        self.maximize_window()

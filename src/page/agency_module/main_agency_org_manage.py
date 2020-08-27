#  -*- coding:utf-8 -*-
# @Time : 2020/8/19 15:49
# @Author: fyl
# @File : main_agency_org_manage.py   中介机构新增和变更申报
import allure

from config.global_var import sleep
from src.page.agency_module.common_main_page import CommonMainPage
from src.page.table_page import TablePage


class MainAgencyOrgManage(CommonMainPage):
    contractType = "//*[@id='condition.contractType']"
    status = "//input[@id='state{}']"  # 任务状态
    input_btn = "//input[@value='{}']"  # 按钮
    contract_no = "//*[@id='condition.contractNo']"
    # 部门类型
    apartment_type = "//*[contains(text(), '部门类型')]/../td[2]/div[contains(@style,'DISPLAY: inline')]/div[contains(@style,'DISPLAY: inline')]/input"
    query_data = "//*[@id='yui-dt-table0']/tbody[1]/tr/td"

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "中介机构新增和变更申报")

    @allure.step("查询")
    def query(self,contract_no, contractType=None, apartment_type='0', status="100"):
        """
        contractType:合同/协议类型
        status：任务提交：0->未选定）,1->被选定，未提交，已提交，被打回
        """
        self.select(self.contractType, contractType)
        if apartment_type == '1':
            self.click(self.wait_until_el_xpath(self.apartment_type))
        if contract_no:
            self.send_keys(self.wait_until_el_xpath(self.contract_no),contract_no)
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

    def is_selected(self,status):
        return self.get_element_xpath(self.status.format(status)).is_selected()



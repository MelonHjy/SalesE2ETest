#  -*- coding:utf-8 -*-
# @Time : 2020/8/27 16:11
# @Author: fyl
# @File : main_commission_approval.py
from config.global_var import sleep
from src.page.agency_module.common_main_page import CommonMainPage


class MainCommissionApproval(CommonMainPage):
    rule_no = "//*[@id='ruleno']"  # 佣金单号
    s_com_code = "//*[@id='sComCode']"  # 归属机构代码
    status = "//*[@id='state{}1']"  # 状态

    def into_page(self, module_menu):
        self.to_main_page(module_menu, "中介机构", "佣金标准审核")

    def query(self, s_com_code=None, rule_no=None, status="10"):
        if s_com_code:
            self.send_keys(self.wait_until_el_xpath(self.s_com_code), s_com_code)
        if rule_no:
            self.send_keys(self.wait_until_el_xpath(self.rule_no), rule_no)
        j = 1
        for i in status:
            el = self.wait_until_el_xpath(self.status.format(j))
            if (el.is_selected() == False and i == "1") or (el.is_selected() and i == "0"):
                self.click(el)
            j = j + 1
        self.click_btn("查询")
        sleep(2)

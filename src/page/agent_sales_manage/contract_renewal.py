#  -*- coding:utf-8 -*-
# @Time : 2020/8/5 10:12
# @Author: fyl
# @File : contract_renewal.py   合同续签页
from src.page.process_page import ProcessPage


class ContractRenewal(ProcessPage):
    case = "//*[@class='case']"
    contract_start_date = "//*[@id='contractstartdate']"  # 合同起始日期
    contract_end_date = "//*[@id='contractenddate']"  # 合同结束日期
    renew = "//*[@id='renew']"  #保存并提交
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe

    def get_head_text(self):
        return self.get_text(self.get_element_xpath(self.case))

    def get_value(self, xpath):
        return self.get_attribute(self.get_element_xpath(xpath),'value')
#  -*- coding:utf-8 -*-
# @Time : 2020/8/5 10:49
# @Author: fyl
# @File : contract_renewal_recheck.py   合同续签复核页
from src.page.process_page import ProcessPage


class ContractRenewalRecheck(ProcessPage):
    case = "//*[@class='case']"
    contract_start_date = "//*[@id='fm1']/div/table/tbody/tr[1]/td[4]"    # 合同起始日期
    contract_end_date = "//*[@id='fm1']/div/table/tbody/tr[1]/td[6]"    # 合同结束日期
    success = "//*[@id='success']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe

    def get_head_text(self):
        return self.get_text(self.get_element_xpath(self.case))




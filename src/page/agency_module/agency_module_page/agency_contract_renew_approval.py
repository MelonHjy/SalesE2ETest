#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 17:03
# @Author: fyl
# @File : new_agency_contract_approval.py   中介合同续签审批
from src.page.process_page import ProcessPage


class AgencyContractRenewApproval(ProcessPage):

    case = "//*[@class='case']"
    pass_check = "//*[@id='passCheck']"
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))

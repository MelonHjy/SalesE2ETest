#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 17:03
# @Author: fyl
# @File : new_agency_contract_approval.py   中介合同修改审批
from src.page.process_page import ProcessPage


class AgencyContractModifyApproval(ProcessPage):

    case = "//*[@class='case']"
    pass_check = "//*[@id='passCheck']"
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))
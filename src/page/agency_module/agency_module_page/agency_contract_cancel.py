#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 15:58
# @Author: fyl
# @File : agency_contract_cancel.py
from src.page.process_page import ProcessPage


class AgencyContractCancel(ProcessPage):
    case = "//*[@class='case']"
    contract_cancel = "//*[@id='contractcancel']"
    submit_frame = "//iframe[@name='submitFrame']"  # 提示聘任的提示框iframe
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def get_head_text(self):
        return self.get_text(self.wait_until_el_xpath(self.case))

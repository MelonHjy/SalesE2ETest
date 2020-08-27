#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 14:16
# @Author: fyl
# @File : new_agency_org.py  中介机构合同续签
from config.global_var import sleep
from src.page.process_page import ProcessPage


class AgencyContractRenew(ProcessPage):
    case = "//*[@class='case']"

    imgBtn1 = "//*[@id='imgBtn{}']"  # 合同日期控件

    renew_submit = "//*[@id='renewSubmit']"  # 保存并提交
    save_success = "//body/table/tbody/tr/td[2]"  # 保存成功
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe

    name = "//*[@id='Name']"  # 账号名

    def get_head_text(self):
        return self.get_text(self.wait_until_el_xpath(self.case))


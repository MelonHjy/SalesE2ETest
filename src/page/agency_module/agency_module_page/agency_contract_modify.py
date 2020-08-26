#  -*- coding:utf-8 -*-
# @Time : 2020/8/25 14:16
# @Author: hjy
# @File : new_agency_org.py  中介机构合同修改
from config.global_var import sleep
from src.page.process_page import ProcessPage


class AgencyContractModify(ProcessPage):
    case = "//*[@class='case']"
    imgBtn1 = "//*[@id='imgBtn{}']"  # 合同日期控件
    add_account = "//*[@id='addAccount[{}]']"  # 编辑银行账号
    # -----银行账号编辑-----#
    sa_Account_bankName = "//*[@id='saDAccount.bankName']"  # 银行代码
    bank_area = "//*[@id='saDAccount.bankareaname']"  # 银行区域
    bank_Name = "//*[@id='bankName']"  # 联行号
    save_account = "//*[contains(@value,'保 存')]"

    contractUpdate_submit = "//*[@id='contractUpdateSubmit']"  # 保存并提交
    save_success = "//body/table/tbody/tr/td[2]"  # 保存成功
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe

    name = "//*[@id='Name']"  # 账号名

    def get_head_text(self):
        return self.get_text(self.wait_until_el_xpath(self.case))

    def send_keys_(self, xpath, param):
        el = self.get_element_xpath(xpath)
        self.execute_script("arguments[0].focus();", el)
        self.send_keys(el, param)
        sleep(2)
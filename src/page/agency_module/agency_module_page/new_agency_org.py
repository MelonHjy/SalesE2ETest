#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 14:16
# @Author: fyl
# @File : new_agency_org.py  新增中介机构
from config.global_var import sleep
from src.page.process_page import ProcessPage


class NewAgencyOrg(ProcessPage):
    case = "//*[@class='case']"
    contract_type = "//*[@id='saAContract.contractType']"  # 合同/协议类型
    com_code = "//*[@id='comCode']"  # 我司机构代码
    agent_name = "//*[@id='saAContract.agentName']"  # 签约中介机构全称
    imgBtn1 = "//*[@id='imgBtn{}']"  # 合同日期控件
    # 部门类型
    apartment_type = "//*[contains(text(), '部门类型')]/../td[2]/div[contains(@style,'DISPLAY: inline')]/div[contains(@style,'DISPLAY: inline')]/input"
    add_agent_contract_button = "//*[@id='addAgentContractButton']"  # 增加按钮
    sa_agent_code = "//*[@id='saAAgentContractList[{}].agentCode']"  # 渠道码
    sa_comCode = "//*[@id='saAAgentContractList[{}].comCode']"  # 我司专营机构/团队
    fee_rule_No = "//*[@id='feeruleNo']/../input[1]"  # 配置单号
    add_account = "//*[@id='addAccount[{}]']"  # 编辑银行账号
    # -----银行账号编辑-----#
    his_payee_name = "//*[@id='hispayeename']"  # 收款人姓名
    his_account_no = "//*[@id='hisaccountno']"  # 收款人账号/卡号
    sa_Account_bankName = "//*[@id='saDAccount.bankName']"  # 银行代码
    bank_area = "//*[@id='saDAccount.bankareaname']"  # 银行区域
    bank_Name = "//*[@id='bankName']"  # 联行号
    save_account = "//*[contains(@value,'保 存')]"

    contract_submit = "//*[@id='contractSubmit']"  # 保存并提交
    save_success = "//body/table/tbody/tr/td[2]"  # 保存成功
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe

    name = "//*[@id='Name']"  # 账号名

    def get_head_text(self):
        return self.get_text(self.wait_until_el_xpath(self.case))

    def select_type(self, contract_type):
        """
        选择合同/协议类型、部门类型
        """
        self.select(self.contract_type, contract_type)
        self.click(self.get_element_xpath(self.apartment_type))

    def contract_date(self, start_date, end_date):
        """
        合同起始日期、终止日期
        """
        self.pick_date_old(self.imgBtn1.format("1"), start_date)
        self.pick_date_old(self.imgBtn1.format("2"), end_date)

    def double_click_org(self, xpath, code):
        com_code_el = self.get_element_xpath(xpath)
        self.send_keys(com_code_el, code)
        self.double_click(com_code_el)
        sleep(3)
        self.switch_to_window()
        confirm = self.wait_until_el_xpath("//input[@value='确定']")
        self.click(confirm)
        sleep(2)
        self.switch_to_window()

    def send_keys_(self, xpath, param):
        el = self.get_element_xpath(xpath)
        self.execute_script("arguments[0].focus();", el)
        self.send_keys(el, param)
        sleep(2)

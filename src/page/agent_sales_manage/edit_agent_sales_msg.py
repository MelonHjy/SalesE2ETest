#  -*- coding:utf-8 -*-
# @Time : 2020/8/4 14:27
# @Author: fyl
# @File : edit_agent_sales_msg.py
import allure
from selenium.webdriver.common.keys import Keys

from config.global_var import sleep
from src.page.process_page import ProcessPage


class EditAgentSaleMsg(ProcessPage):
    case = "//*[@class='case']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    close_over = "//input[@class='button_ty_over']"
    close_btn = "//input[@class='button_ty']"
    manage_account_btn = "//input[@id='manageAccount']"  # 修改账号
    # ---------------------人员基础信息填写项------------------------------ #
    user_tab = "//*[@id='folder-label-userTab']"
    username = "//input[@id='userName']"
    id_cards = "//input[@id='idCards']"
    make_com = "//*[@id='makeCom']"
    mobile = "//*[@id='mobile']"
    usertype = "//*[@id='usertype']"
    birthday = "//*[@id='birthday']"
    # 双击选择框
    com_code = "//*[@id='comCode']"
    group_code = "//input[@id='groupcode']"
    # 下拉选项
    sex = "//*[@id='sex']"
    rolecode = "//*[@id='rolecode']"  # 团队职务选择
    nation = "//*[@id='nation']"  # 民族
    visage = "//*[@id='visage']"  # 政治面貌
    culture = "//*[@id='culture']"  # 学历
    # 保存
    save_button = "//input[@id='preparesavedeputy2']"
    # 保存并提交
    save_commit_btn = "//input[@id='savedeputy2']"

    # ---------------------合同信息填写项------------------------------ #
    contract_tab = "//*[@id='folder-label-contractTab']"

    addUserButton = "//*[@id='addUserButton']"  # 增加资质信息
    # 增加资质信息中的各项
    qualifytype = "//*[@id='qualifytype[{0}]']"  # 证件类型
    qualifyno = "//*[@id='qualifyno[{0}]']"  # 证件号码
    qualifystartdate = "//*[@id='qualifystartdate{0}']"  # 发证日期
    agentType = "//*[@id='agentType[{0}]']"  # 证件类型
    # 合同基本信息中的各项
    agentno0 = "//*[@id='agentno0']"  # 资格证号码
    credentialno0 = "//*[@id='credentialno0']"  # 执业证号码
    contractstartdate0 = "//*[@id='contractstartdate0']"  # 合同起始日期
    imgBtncon1 = "//*[@id='imgBtncon1[0]']"  # 合同起始日期按钮
    contractenddate0 = "//*[@id='contractenddate0']"  # 合同终止日期
    imgBtncon2 = "//*[@id='imgBtncon2[0]']"  # 合同终止日期按钮
    ruleNo = "//*[@id='ruleNo']/following-sibling::input[1]"  # 佣金配置
    # 账户信息中的各项
    accountno = "//*[@id='accountno']"  # 收款人账号
    cardtype = "//*[@id='cardtype']"  # 卡折标志
    saDAccount_bankName = "//*[@id='saDAccount.bankName']"  # 银行名称
    saDAccount_bankareaname = "//*[@id='saDAccount.bankareaname']"  # 银行区域名称
    bankName = "//*[@id='bankName']"  # 联行号

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))

    @allure.step("切换到合同信息")
    def switch_contract_tab(self):
        self.click(self.wait_until_el_xpath(self.contract_tab))

    @allure.step("切换到人员基础信息")
    def switch_user_tab(self):
        self.click(self.wait_until_el_xpath(self.user_tab))

    @allure.step("选择民族")
    def select_nation(self, text):
        self.select(self.nation, text)

    @allure.step("选择政治面貌")
    def select_visage(self, text):
        self.select(self.visage, text)

    @allure.step("选择学历")
    def select_culture(self, text):
        self.select(self.culture, text)

    @allure.step("填写资质信息,第{num}条（证件类型:{qualifytype},证件号码：{qualifyno},发证日期：{qualifystartdate},证件类型：{agentType}")
    def input_qualify(self, num, qualifytype, qualifyno, qualifystartdate, agentType=None):
        self.select(self.qualifytype.format(num), qualifytype)
        ele = self.wait_until_el_xpath(self.qualifyno.format(num))
        self.execute_script("arguments[0].focus();", ele)
        self.send_keys(ele, qualifyno)
        # 日期组件
        self.pick_date_new(self.qualifystartdate.format(num), qualifystartdate)
        if agentType:
            self.select(self.agentType.format(num), agentType)

    @allure.step(
        "填写合同基本信息（资格证号码:{agentno0},执业证号码：{credentialno0},合同起始日期：{contractstartdate0},合同终止日期：{contractenddate0}")
    def input_contract(self, agentno0, credentialno0, contractstartdate0, contractenddate0):
        self.select(self.agentno0, agentno0)
        self.select(self.credentialno0, credentialno0)
        # 日期组件
        self.pick_date_old(self.imgBtncon1, contractstartdate0)
        self.pick_date_old(self.imgBtncon2, contractenddate0)

    @allure.step("聘任保存")
    def prepare_save(self):
        self.click(self.wait_until_el_xpath(self.save_button))

    @allure.step("聘任保存并提交")
    def save_commit(self):
        self.click(self.wait_until_el_xpath(self.save_commit_btn))

    def submit_process(self, textarea=""):
        self.submit_interaction(iframe_xpath=self.submit_iframe, textarea=textarea)
        sleep(2)
        self.click(self.wait_until_el_xpath(self.close_over))

    @allure.step(
        "填写账户信息（收款人账号:{accountno},卡折标志:{cardtype},银行名称：{saDAccount_bankName},银行区域名称：{saDAccount_bankareaname},联行号：{bankName}）")
    def input_account(self, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        self.send_keys(self.wait_until_el_xpath(self.saDAccount_bankName), saDAccount_bankName)
        sleep(1)
        self.send_keys(self.wait_until_el_xpath(self.saDAccount_bankareaname), saDAccount_bankareaname)
        sleep(1)
        self.send_keys(self.wait_until_el_xpath(self.bankName), bankName)
        sleep(1)
        self.send_keys(self.wait_until_el_xpath(self.accountno), accountno)
        self.select(self.cardtype, cardtype)

    @allure.step("修改账号")
    def manage_account(self):
        self.click(self.wait_until_el_xpath(self.manage_account_btn))

    def get_cardtype(self):
        value = self.get_element_xpath(self.cardtype).get_attribute('value')
        cardtype = {'1': '卡', '2': '折', '3': '对公账号'}
        return cardtype[value]

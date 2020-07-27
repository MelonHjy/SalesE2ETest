#  -*- coding:utf-8 -*-
# @Time : 2020/7/27 11:14
# @Author: fyl
# @File : group_issue.py   团队成员出单权赋予
import allure

from config.global_var import sleep
from src.page.base_page import BasePage


class GroupIssue(BasePage):

    case = "//*[@class='case']"
    save_button = "//input[@id='prepareadddeputy']"  # 保存
    save_commit = "//input[@id='adddeputy']"  # 保存并提交
    close = "//input[@class='button_ty']"
    submit_dlg = "//div[@id='submitDlg_c']"
    submit_iframe = "submitFrame"

    # ---------------------人员基础信息填写项------------------------------ #
    user_tab = "//*[@id='folder-label-userTab']"
    username = "//input[@id='userName']"
    id_cards = "//input[@id='idCards']"
    make_com = "//*[@id='makeCom']"  # 出单归属机构
    mobile = "//*[@id='mobile']"
    # usertype = "//*[@id='usertype']"  # 人员属性
    birthday = "//*[@id='birthday']"
    # 双击选择框
    com_code = "//*[@id='comCode']"
    group_code = "//input[@id='groupcode']"
    # 下拉选项
    sex = "//*[@id='sex']"
    # rolecode = "//*[@id='rolecode']"  # 团队职务选择
    nation = "//*[@id='nation']"  # 民族
    visage = "//*[@id='visage']"  # 政治面貌
    culture = "//*[@id='culture']"  # 学历

    # ---------------------合同信息填写项------------------------------ #
    contract_tab = "//*[@id='folder-label-contractTab']"

    addUserButton = "//*[@id='addUserButton']"  # 增加资质信息
    # 增加资质信息中的各项
    qualifytype = "//*[@id='saUQualifys[{0}].qualifytype']"  # 证件类型
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
    usercodeAndContract = "//td[@colSpan='2']"  # 人员代码，合同号

    @allure.step("填入姓名:{username},身份证号：{id_cards},手机号码：{mobile}")
    def user_tab_input(self, username, id_cards, mobile):
        """
        username:姓名
        id_cards：身份证号
        mobile:手机号码
        """
        self.send_keys(self.wait_until_el_xpath(self.username), username)
        self.send_keys(self.wait_until_el_xpath(self.id_cards), id_cards)
        self.send_keys(self.wait_until_el_xpath(self.mobile), mobile)

    @allure.step("选择上级机构:{com_code}，归属机构:{group_code}")
    def select_org(self, com_code, group_code):
        """
        com_code:上级机构
        group_code：归属机构
        """
        self.code_select(self.com_code, com_code)
        self.code_select(self.group_code, group_code)
        sleep(2)

    @allure.step("民族:{nation}->政治面貌:{visage}->学历:{culture}")
    def select_base(self, nation, visage, culture):
        """
        nation_text:民族选项值
        visage_text：政治面貌选项值
        culture_text：学历选项值
        """
        self.select(self.nation, nation)
        self.select(self.visage, visage)
        self.select(self.culture, culture)

    @allure.step("切换到合同信息")
    def switch_contract_tab(self):
        self.click(self.wait_until_el_xpath(self.contract_tab))

    @allure.step("切换到人员基础信息")
    def switch_user_tab(self):
        self.click(self.wait_until_el_xpath(self.user_tab))

    def get_head_text(self):
        return self.get_text(self.get_element_xpath(self.case))

    def add_user_button(self):
        self.click(self.wait_until_el_xpath(self.addUserButton))

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
        "填写合同基本信息（资格证号码:{agentno0},执业证号码：{credentialno0},合同起始日期：{contractstartdate0},合同终止日期：{contractenddate0},佣金配置：{ruleNo}）")
    def input_contract(self, agentno0, credentialno0, contractstartdate0, contractenddate0, ruleNo):
        self.select(self.agentno0, agentno0)
        self.select(self.credentialno0, credentialno0)
        # 日期组件
        self.pick_date_old(self.imgBtncon1, contractstartdate0)
        self.pick_date_old(self.imgBtncon2, contractenddate0)
        self.code_select(self.ruleNo, ruleNo)

    @allure.step(
        "填写账户信息（收款人账号:{accountno},卡折标志:{cardtype},银行名称：{saDAccount_bankName},银行区域名称：{saDAccount_bankareaname},联行号：{bankName}）")
    def input_account(self, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        self.send_keys(self.wait_until_el_xpath(self.accountno), accountno)
        self.select(self.cardtype, cardtype)
        self.send_keys(self.wait_until_el_xpath(self.saDAccount_bankName), saDAccount_bankName)
        sleep(1)
        self.send_keys(self.wait_until_el_xpath(self.saDAccount_bankareaname), saDAccount_bankareaname)
        sleep(1)
        self.send_keys(self.wait_until_el_xpath(self.bankName), bankName)
        sleep(1)

    def prepare_add_deputy(self):
        self.click(self.wait_until_el_xpath(self.save_button))

    @allure.step("生成人员代码，合同号")
    def get_msg(self):
        text = self.get_text(self.wait_until_el_xpath(self.usercodeAndContract))
        a = text.split(' ')
        msg = {'usercode': a[0].split('：')[1], "contract": a[1].split('：')[1]}
        return msg

# -*- coding:utf-8 -*-
# @Time : 2020/6/30 15:01
# @Author: fyl
# @File : appointment_and_dismissal.py 营销团队经理聘任与解聘
import allure

from config.global_var import sleep
from src.page.base_page import BasePage


class AppointmentAndDismissal(BasePage):
    # frame
    frame_id = 'main'
    # 销售团队经理聘任与解聘
    xstdjlpryjp = "//input[@value='营销团队经理聘任与解聘']"
    # iframe->营销团队经理聘任与解聘
    iframe = "//iframe[@name='page']"
    # 营销团队经理聘任
    case = "//*[@class='case']"
    close_icon = "//div[@class='container-close']"  # 提交后提示选择审核人对话框的关闭图标

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
    # 聘任保存
    save_button = "//input[@id='prepareadddeputy']"
    # 聘任保存并提交
    save_commit = "//input[@id='adddeputy']"

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
    close = "//input[@class='button_ty']"
    submit_dlg = "//div[@id='submitDlg_c']"
    submit_iframe = "submitFrame"
    submit_btn = "//*[@id='save1']"
    close_over = "//input[@class='button_ty_over']"

    @allure.step("增加资质信息两条（资格证、执业证）")
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
        self.send_keys(self.wait_until_el_xpath(self.saDAccount_bankareaname), saDAccount_bankareaname)
        self.send_keys(self.wait_until_el_xpath(self.bankName), bankName)

    @allure.step("填入姓名:{username},身份证号：{id_cards},手机号码：{mobile}")
    def user_tab_input(self, username, id_cards, mobile):
        self.send_keys(self.wait_until_el_xpath(self.username), username)
        self.send_keys(self.wait_until_el_xpath(self.id_cards), id_cards)
        self.send_keys(self.wait_until_el_xpath(self.mobile), mobile)

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))

    def get_com_code_text(self):
        return self.get_element_xpath(self.com_code).get_attribute('value')

    def get_make_com_text(self):
        return self.get_element_xpath(self.make_com).get_attribute('value')

    def get_sex(self, text):
        value = self.get_element_xpath(self.sex).get_attribute('value')
        sex = {'': '请选择', '1': '男', '2': '女'}
        self.assertEqual("验证性别是否与身份证匹配", sex[value], text)

    def get_birthday(self):
        value = self.get_element_xpath(self.birthday).get_attribute('value')
        return ''.join(value.split('-'))

    def get_make_com(self):
        return self.get_text(
            self.get_element_xpath(self.make_com))

    @allure.step("双击选择上级机构")
    def select_com(self):
        self.code_select(self.com_code, "32000000--中国人民财产保险股份有限公司江苏省分公司")

    @allure.step("双击选择归属团队")
    def select_group(self, text):
        self.code_select(self.group_code, text)

    @allure.step("选择团队职务")
    def select_rolecode(self, text):
        self.select(self.rolecode, text)

    @allure.step("选择民族")
    def select_nation(self, text):
        self.select(self.nation, text)

    @allure.step("选择政治面貌")
    def select_visage(self, text):
        self.select(self.visage, text)

    @allure.step("选择学历")
    def select_culture(self, text):
        self.select(self.culture, text)

    @allure.step("填入姓名:{username},身份证号：{id_cards},手机号码：{mobile}")
    def contract_tab_input(self, username, id_cards, mobile):
        self.send_keys(self.wait_until_el_xpath(self.username), username)
        self.send_keys(self.wait_until_el_xpath(self.id_cards), id_cards)
        self.send_keys(self.wait_until_el_xpath(self.mobile), mobile)

    @allure.step("切换到合同信息")
    def switch_contract_tab(self):
        self.click(self.wait_until_el_xpath(self.contract_tab))

    @allure.step("切换到人员基础信息")
    def switch_user_tab(self):
        self.click(self.wait_until_el_xpath(self.user_tab))

    @allure.step("聘任保存")
    def prepare_save(self):
        self.click(self.wait_until_el_xpath(self.save_button))

    @allure.step("聘任保存并提交")
    def prepare_save_commit(self):
        self.click(self.wait_until_el_xpath(self.save_commit))

    @allure.step("获取人员代码，合同号")
    def get_msg(self):
        text = self.get_text(self.wait_until_el_xpath(self.usercodeAndContract))
        a = text.split(' ')
        msg = {'usercode': a[0].split('：')[1], "contract": a[1].split('：')[1]}
        return msg

    def close_btn(self):
        self.click(self.wait_until_el_xpath(self.close))
        sleep(3)

    def submit_(self):
        self.switch_to_first_iFrame(self.submit_iframe)
        self.click(self.wait_until_el_xpath(self.submit_btn))
        sleep(2)

    def close_over_btn(self):
        self.click(self.wait_until_el_xpath(self.close_over))
        sleep(2)

    # ---------------------以下输入信息验证相关------------------------------ #

    @allure.step("输入合同起始日期、终止日期")
    def input_contract_date(self, start_date, end_date):
        self.pick_date_old(self.imgBtncon1, start_date)
        self.pick_date_old(self.imgBtncon2, end_date)

    # 资格证、职业证输入
    @allure.step("输入资格证、职业证的发证日期")
    def input_qualify_date(self, qualifystartdate0, qualifystartdate1):
        self.pick_date_new(self.qualifystartdate.format(0), qualifystartdate0)
        self.pick_date_new(self.qualifystartdate.format(1), qualifystartdate1)

    # 关闭提交对话框
    def close_submit(self):
        self.click(self.wait_until_el_xpath(self.close_icon))

    # 获取title属性的属性值
    def get_title_att(self, xpath):
        return self.get_attribute(self.wait_until_el_xpath(xpath),
                                  'title')

    # 保存提交->弹出提示—>关闭提示
    def submit_step(self, expect):
        self.switch_user_tab()
        self.prepare_save_commit()
        if expect:
            self.close_submit()
        else:
            self.choose_ok_on_alert()
        self.switch_contract_tab()
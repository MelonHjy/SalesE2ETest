# -*- coding:utf-8 -*-
# @Time : 2020/6/30 15:01
# @Author: fyl
# @File : appointment_and_dismissal.py
import allure

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

    # ---------------------人员基础信息填写项------------------------------ #
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

    # ---------------------人员基础信息填写项------------------------------ #
    contract_tab = "//*[@id='folder-label-contractTab']"

    @allure.step("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
    def into_page(self):
        self.select_frame_id(self.frame_id)
        self.move_to_el(self.wait_until_el_xpath(self.jyjg))
        self.click(self.wait_until_el_xpath(self.xsryzk))
        self.click(self.wait_until_el_xpath(self.dlzxsrydmgl))
        self.select_frame_id(self.wait_until_el_xpath(self.iframe))
        self.click(self.wait_until_el_xpath(self.xstdjlpryjp))

        # 切换到【营销团队经理聘任与解聘】页面
        self.switch_to_last_window()

    @allure.step("填入姓名:{username},身份证号：{id_cards},手机号码：{mobile}")
    def input(self, username, id_cards, mobile):
        self.send_keys(self.wait_until_el_xpath(self.username), username)
        self.send_keys(self.wait_until_el_xpath(self.id_cards), id_cards)
        self.send_keys(self.wait_until_el_xpath(self.mobile), mobile)

    def get_head_text(self):
        self.get_text(
            self.get_element_xpath(self.case))

    def get_com_code_text(self):
        self.get_text(
            self.get_element_xpath(self.com_code))

    def get_make_com_text(self):
        self.get_text(
            self.get_element_xpath(self.make_com))

    def get_sex(self):
        self.get_text(
            self.get_element_xpath(self.sex))

    def get_birthday(self):
        self.get_text(
            self.get_element_xpath(self.birthday))

    def get_make_com(self):
        self.get_text(
            self.get_element_xpath(self.make_com))

    @allure.step("双击选择上级机构")
    def select_com(self):
        self.code_select(self.com_code, "32000000--中国人民财产保险股份有限公司江苏省分公司", 3)

    @allure.step("双击选择归属团队")
    def select_group(self, text):
        self.code_select(self.group_code, text, 3)

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

    @allure.step("聘任保存")
    def prepare_save(self):
        self.wait_until_el_xpath(self.save_button)

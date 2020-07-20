# -*- coding:utf-8 -*-

# @Time : 2020/6/30 11:00
# @Author: fyl
# @File : main_management_agent_salesmen.py  代理制销售人员代码管理
import allure
from selenium import webdriver

from config.global_var import sleep, g
from src.page.table_page import TablePage


class ManagementOfAgentSalesmen(TablePage):
    # frame
    frame_id = 'main'
    # 上级机构选项
    sjjg = "//input[@id='comCode']"
    # 归属机构选项
    gsjg = "//input[@id='groupcode']"
    # 人员代码
    rydm = "//input[@id='userCode']"
    # 姓名
    xm = "//input[@id='userName']"
    # 身份证号
    sfzh = "//input[@id='identifyNumber']"
    # 性别
    xb = "//select[@id='sex']"
    # 资格证号
    zgzh = "//input[@id='agentno']"
    # 职业证号
    zyzh = "//input[@id='credentialno']"
    # 人员属性
    rysx = "//select[@id='usertype22']"
    # 销售团队经理聘任与解聘
    xstdjlpryjp = "//input[@value='营销团队经理聘任与解聘']"
    query = "//input[@value='查询']"
    # iframe->营销团队经理聘任与解聘
    iframe = "//iframe[@name='page']"

    # ---------------------查询信息------------------------------ #

    user_code = "//input[@id='userCode']"  # 内部流转码
    table_first_usercode = "//td[@id='yui-dt0-bdrow0-cell2']"  # 内部流转码
    table_first_name = "//td[@id='yui-dt0-bdrow0-cell3']"  # 姓名
    table_first_id_cards = "//td[@id='yui-dt0-bdrow0-cell4']"  # 身份证
    table_first_sjjg = "//td[@id='yui-dt0-bdrow0-cell6']"  # 上级机构
    table_first_group = "//td[@id='yui-dt0-bdrow0-cell7']"  # 归属团队

    @allure.step("经营机构->销售人员->代理制销售人员代码管理->查询")
    def into_page_query(self, user_code1):
        self.select_frame_id(self.frame_id)
        self.move_to_el(self.wait_until_el_xpath(self.jyjg))
        self.click(self.wait_until_el_xpath(self.xsryzk))
        self.click(self.wait_until_el_xpath(self.dlzxsrydmgl))
        self.select_frame_id(self.wait_until_el_xpath(self.iframe))
        self.click(self.wait_until_el_xpath(self.user_code))
        self.send_keys(self.wait_until_el_xpath(self.user_code), user_code1)
        self.click(self.wait_until_el_xpath(self.query))

    def assert_table_msg(self, usercode, name, id_cards, sjjg, group):
        # usercode1 = self.get_text(self.wait_until_el_xpath(self.table_first_usercode))
        # name1 = self.get_text(self.wait_until_el_xpath(self.table_first_name))
        # id_cards1 = self.get_text(self.wait_until_el_xpath(self.table_first_id_cards))
        # sjjg1 = self.get_text(self.wait_until_el_xpath(self.table_first_sjjg))
        # group1 = self.get_text(self.wait_until_el_xpath(self.table_first_group))

        # 需要加一个等待数据加载完成

        usercode1 = self.get_cell_text(0, 2)
        name1 = self.get_cell_text(0, 3)
        id_cards1 = self.get_cell_text(0, 4)
        sjjg1 = self.get_cell_text(0, 6)
        group1 = self.get_cell_text(0, 7)
        self.assertEqual("验证内部流转码", usercode1, usercode)
        self.assertEqual("验证姓名", name1, name)
        self.assertEqual("验证身份证", id_cards1, id_cards)
        self.assertEqual("验证上级机构", sjjg1, sjjg)
        self.assertEqual("验证归属机构", group1, group)

    @allure.step("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
    def into_page(self):
        self.select_frame_id(self.frame_id)
        self.click(self.wait_until_el_xpath(self.jyjg))
        self.execute_script("arguments[0].style.visibility='visible';", self.wait_until_el_xpath("//*[@id='menumain8000223038']"))
        self.click(self.wait_until_el_xpath(self.xsryzk))
        self.execute_script("arguments[0].style.visibility='visible';", self.wait_until_el_xpath("//*[@id='menumain8000223038']"))
        self.click(self.wait_until_el_xpath(self.dlzxsrydmgl))
        # self.execute_script("arguments[0].style.visibility='hidden';", self.wait_until_el_xpath("//*[@id='menumain8000223038']"))
        self.select_frame_id(self.wait_until_el_xpath(self.iframe))
        self.click(self.wait_until_el_xpath(self.xstdjlpryjp))
        # self.open_url("http://10.133.247.40:8004/sales/deputy/engageOrFire.do?efOrmau=e")
        sleep(2)
        # 切换到【营销团队经理聘任与解聘】页面
        self.switch_to_window()
        self.maximize_window()

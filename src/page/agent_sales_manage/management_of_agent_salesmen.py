# -*- coding:utf-8 -*-
#@Time : 2020/6/30 11:00
#@Author: fyl
#@File : management_of_agent_salesmen.py  代理制销售人员代码管理
from src.page.base_page import BasePage


class ManagementOfAgentSalesmen(BasePage):

    #frame
    frame_id = 'main'
    #上级机构选项
    sjjg = "//input[@id='comCode']"
    #归属机构选项
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
    #销售团队经理聘任与解聘
    xstdjlpryjp = "//input[@name='add' and text()='营销团队经理聘任与解聘']"

    def into_page(self):
        self.select_frame_id(self.frame_id)
        self.move_to_el(self.get_element_xpath(self.jyjg))
        self.click(self.wait_until_el_xpath(self.xsryzk))
        self.click(self.wait_until_el_xpath(self.dlzxsrydmgl))




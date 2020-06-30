# -*- coding:utf-8 -*-
#@Time : 2020/6/30 15:01
#@Author: fyl
#@File : appointment_and_dismissal.py
import allure

from src.page.base_page import BasePage, sleep


class AppointmentAndDismissal(BasePage):

    #frame
    frame_id = 'main'
    #销售团队经理聘任与解聘
    xstdjlpryjp = "//input[@value='营销团队经理聘任与解聘']"
    #iframe->营销团队经理聘任与解聘
    iframe = "//iframe[@name='page']"

    @allure.step("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
    def into_page(self):
        self.select_frame_id(self.frame_id)
        self.move_to_el(self.wait_until_el_xpath(self.jyjg))
        self.click(self.wait_until_el_xpath(self.xsryzk))
        self.click(self.wait_until_el_xpath(self.dlzxsrydmgl))
        self.select_frame_id(self.wait_until_el_xpath(self.iframe))
        self.click(self.wait_until_el_xpath(self.xstdjlpryjp))
        self.open_url("http://10.133.247.40:8004/sales/deputy/engageOrFire.do?efOrmau=e")
        # self.execute_script('window.open("http://10.133.247.40:8004/sales/deputy/engageOrFire.do?efOrmau=e");')
        #self.current_window()


# -*- coding:utf-8 -*-

# @Time : 2020/6/30 11:00
# @Author: fyl
# @File : main_management_agent_salesmen.py  代理制销售人员代码管理
import allure

from config.global_var import sleep
from src.page.table_page import TablePage


class ManagementOfAgentSalesmen(TablePage):
    sjjg = "//input[@id='comCode']"  # 上级机构选项
    gsjg = "//input[@id='groupcode']"  # 归属机构选项
    rydm = "//input[@id='userCode']"  # 人员代码
    xm = "//input[@id='userName']"  # 姓名
    sfzh = "//input[@id='identifyNumber']"  # 身份证号
    xb = "//select[@id='sex']"  # 性别
    zgzh = "//input[@id='agentno']"  # 资格证号
    zyzh = "//input[@id='credentialno']"  # 职业证号
    rysx = "//select[@id='usertype22']"  # 人员属性
    xstdjlpryjp = "//input[@value='营销团队经理聘任与解聘']"  # 销售团队经理聘任与解聘
    query_btn = "//input[@value='查询']"
    status = "//input[@id='taskstatus{}']"  # 任务状态

    # ---------------------查询信息------------------------------ #

    user_code = "//input[@id='userCode']"  # 内部流转码
    submit_frame = "//iframe[@name='submitFrame']"  # 提示解雇的提示框iframe
    dismissal_btn = "//form[@id='fm1']/table/tbody/tr[4]/td/input[2]"  # 解聘按钮

    @allure.step("经营机构->销售人员->代理制销售人员代码管理")
    def into_page(self):
        self.to_main_page("经营机构", "销售人员", "代理制销售人员代码管理")

    @allure.step("查询")
    def query(self, user_code1, status=""):
        self.click(self.wait_until_el_xpath(self.user_code))
        self.send_keys(self.wait_until_el_xpath(self.user_code), user_code1)
        if status:
            self.click(self.wait_until_el_xpath(self.status.format(status)))
        self.click(self.wait_until_el_xpath(self.query_btn))
        sleep(3)

    def assert_table_msg(self, usercode, name, id_cards, sjjg, group):
        # 需要加一个等待数据加载完成
        usercode1 = self.get_cell_text_by_head('内部流转码', 0)
        name1 = self.get_cell_text_by_head('姓名', 0)
        id_cards1 = self.get_cell_text_by_head('身份证', 0)
        sjjg1 = self.get_cell_text_by_head('上级机构', 0)
        group1 = self.get_cell_text_by_head('归属机构', 0)
        self.assertEqual("验证内部流转码", usercode1, usercode)
        self.assertEqual("验证姓名", name1, name)
        self.assertEqual("验证身份证", id_cards1, id_cards)
        self.assertEqual("验证上级机构", sjjg1, sjjg)
        self.assertEqual("验证归属机构", group1, group)

    @allure.step("营销团队经理聘任与解聘")
    def appointment(self):
        self.click(self.wait_until_el_xpath(self.xstdjlpryjp))
        # self.open_url("http://10.133.247.40:8004/sales/deputy/engageOrFire.do?efOrmau=e")
        sleep(2)
        # 切换到【营销团队经理聘任与解聘】页面
        self.switch_to_window()
        self.maximize_window()

    def select_by_user_code(self, user_code):
        """
        选择需要解聘的员工并返回归属团队代码
        """
        list = self.get_cell_text_by_head('内部流转码')
        index = list.index(user_code)
        self.click(self.get_radio_by_head(index, '选择'))
        return index

    def select_dismissal(self):
        """
        切换提示框frame，并点击解聘按钮
        """
        self.select_frame_id(self.wait_until_el_xpath(self.submit_frame))
        self.click(self.wait_until_el_xpath(self.dismissal_btn))

    def assert_workflow_msg(self):
        status = self.get_cell_text_by_head('业务状态', 1)
        self.assertEqual("验证业务状态", status, "同意并提交")

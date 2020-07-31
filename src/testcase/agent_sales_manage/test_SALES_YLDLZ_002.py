# -*- coding:utf-8 -*-
# @Time : 2020/6/28 17:22
# @Author: fyl
# @File : test_SALES_YLDLZ_001.py   营销团队经理聘任与解聘（有效团队成员任命为经理）
import allure
import pytest

from src.page.Personal_agency_channel.main_management_agent_sales_approve import ManagementAgentSalesApprove
from src.page.Personal_agency_channel.sales_query import SalesQuery
from src.page.agent_sales_manage.appointment_manager import AppointmentManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils.driver_util import *


@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘（有效团队成员任命为经理）")
class Test_YLDLZ_002():
    appointment = AppointmentManager()
    main_page = ManagementOfAgentSalesmen()
    ASR = AgentSalesRecheck()
    MASA = ManagementAgentSalesApprove()
    SQ = SalesQuery()

    data = [("83258563")]
    msg = None

    @allure.story("提交有效团队成员任命为经理")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.parametrize("user_code", data)
    def test_appointment_valid(self, user_code):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.main_page.into_page()
        self.main_page.query(user_code)
        Test_YLDLZ_002.msg = {"group_name": self.main_page.get_cell_text_by_head("归属团队"),
                              "user_name": self.main_page.get_cell_text_by_head("姓名")}
        info("选择人员->代码：{}，状态：有效".format(user_code))
        self.main_page.select_data("状态", "有效", "选择")
        self.main_page.click_btn("营销团队经理聘任与解聘")
        info("选择聘任")
        self.main_page.select_appointment()
        # self.main_page.switch_to_window()
        # self.main_page.maximize_window()
        self.appointment.assertEqual("验证页面", self.appointment.get_head_text(), "营销团队经理聘任")
        info("团队职务选择")
        self.appointment.select_rolecode("经理")
        info("保存并提交")
        self.appointment.click(self.appointment.wait_until_el_xpath(self.appointment.save_commit2))
        self.appointment.choose_ok_on_alert()
        self.appointment.submit_interaction(self.appointment.submit_iframe)
        # 关闭
        # 切换
        # self.main_page.back_to_page()
        # self.main_page.query(user_code, status="010")
        # self.main_page.set_table_num(3)
        # 根据状态选择查看信息    状态:经理聘任复核
        # self.main_page.select_data("状态", "经理聘任复核", "操作")

    @allure.story("省级个代渠道审核岗审核流程")
    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_recheck(self, user_code):
        self.MASA.into_page()
        self.MASA.query(user_code)
        self.MASA.select_data("经理聘任审核")
        self.MASA.switch_to_window()
        self.MASA.maximize_window()
        self.MASA.approve()
        self.MASA.submit_interaction(self.MASA.submit_iframe, textarea="ui测试")
        # 关闭

    @allure.story("省级销售管理综合岗复核流程")
    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_recheck(self, user_code):
        self.ASR.into_page()
        self.ASR.query(user_code)
        self.ASR.select_data("经理聘任复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        self.ASR.recheck_ope(textarea="ui测试")
        # 关闭

    @allure.story("验证审核通过后核对人员信息")
    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_sales_query(self, user_code):
        self.SQ.into_page()
        self.SQ.query(user_code)
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")

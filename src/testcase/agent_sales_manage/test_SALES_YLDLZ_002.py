# -*- coding:utf-8 -*-
# @Time : 2020/6/28 17:22
# @Author: fyl
# @File : test_SALES_YLDLZ_001.py   代理制人员代码管理>>营销团队经理聘任与解聘（有效团队成员任命为经理）
import allure
import pytest

from src.page.Personal_agency_channel.main_management_agent_sales_approve import ManagementAgentSalesApprove
from src.page.Personal_agency_channel.sales_query import SalesQuery
from src.page.agent_sales_manage.appointment_manager import AppointmentManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.appointment_manager_recheck import AppointmentManagerRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.driver_util import *
from src.utils.except_util import get_screenshot


@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘（有效团队成员任命为经理）")
class Test_YLDLZ_002():
    AM = AppointmentManager()
    MOAS = ManagementOfAgentSalesmen()
    ASR = AgentSalesRecheck()
    SQ = SalesQuery()
    AMR = AppointmentManagerRecheck()

    data = csv_util.data_reader("agent_sales_manage/002_data.csv")
    msg = None

    @allure.story("提交有效团队成员任命为经理")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize("user_code", data)
    def test_001(self, user_code):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        self.MOAS.query(user_code)
        Test_YLDLZ_002.msg = {"group_name": self.MOAS.get_cell_text_by_head("归属团队"),
                              "user_name": self.MOAS.get_cell_text_by_head("姓名")}
        info("选择人员->代码：{}，状态：有效".format(user_code))
        self.MOAS.select_data("状态", "有效", "选择")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("营销团队经理聘任与解聘")))
        info("选择聘任")
        self.MOAS.select_appointment()
        self.MOAS.switch_to_window()
        self.MOAS.maximize_window()
        self.AM.assertEqual("判断页面标题", self.AM.get_head_text(), "营销团队经理聘任")
        get_screenshot("聘任")
        info("团队职务选择")
        self.AM.select_rolecode("经理")
        info("保存并提交")
        self.AM.click(self.AM.wait_until_el_xpath(self.AM.save_commit2))
        self.AM.choose_ok_on_alert()
        self.AM.submit_interaction(self.AM.submit_iframe)
        text = self.AM.get_text(self.AM.get_element_xpath(self.AM.save_success))
        self.AM.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        # 关闭
        # 切换
        # self.MOAS.back_to_page()
        # self.MOAS.query(user_code, status="010")
        # self.MOAS.set_table_num(3)
        # 根据状态选择查看信息    状态:经理聘任复核
        # self.MOAS.select_data("状态", "经理聘任复核", "操作")

    @allure.story("有效团队成员任命为经理--复核流程")
    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002(self, user_code):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.ASR.query(user_code)
        self.ASR.select_data("经理聘任复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        get_screenshot("复核页")
        info("复核")
        self.AMR.assertEqual("判断页面标题", self.AMR.get_head_text(), "经理聘任复核")
        self.AMR.recheck_ope(textarea="有效团队成员任命为经理--ui测试")
        get_screenshot("提交")
        self.AMR.close_button_ty()
        # 关闭

    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @allure.story("验证审核通过后核对人员信息")
    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_003(self, user_code):
        self.SQ.into_page()
        self.SQ.query(user_code)
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        get_screenshot("验证")
        self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")

#  -*- coding:utf-8 -*-
# @Time : 2020/7/21 16:00
# @Author: fyl
# @File : test_SALES_YLDLZ_005.py   代理制人员代码管理>>营销团队经理聘任与解聘（有效的经理解聘该人员经理职务） 待测
import allure
import pytest

from config.global_var import sleep
from src.page.agent_sales_manage.dismissal_manager import DismissalManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.dismissal_manager_recheck import DismissalManagerRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import *


@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘（有效的经理解聘该人员经理职务）")
class Test_YLDLZ_005():
    MOAS = ManagementOfAgentSalesmen()
    DM = DismissalManager()
    ASR = AgentSalesRecheck()
    DMR = DismissalManagerRecheck()
    msg = None

    # data = [("83258554")]
    data = csv_util.data_reader("agent_sales_manage/005_data.csv")

    @allure.story("有效的经理解聘该人员经理职务")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_YLDLZ_005(self, user_code):
        Test_YLDLZ_005.msg = {"user_code": user_code}
        info("进入代理制销售人员代码管理页面")
        self.MOAS.into_page()
        info("查询该人员代码是否存在数据")
        self.MOAS.query(user_code)
        # 判断查询的数据 在状态列的值为”有效“
        info("选择数据")
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("进入“营销团队经理解聘”页面")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("营销团队经理聘任与解聘")))
        self.MOAS.select_dismissal()
        info("切换“营销团队经理解聘”页面")
        self.MOAS.switch_to_window()
        self.MOAS.maximize_window()
        info("选择需要解聘的员工并获取归属团队代码")
        self.DM.assertEqual("判断页面标题", self.DM.get_head_text(), "营销团队经理解聘")
        self.DM.select_by_user_code(user_code)
        # info("解聘保存")
        # self.DM.prepare_save()
        # get_screenshot("营销团队经理解聘保存")
        # self.DM.prepare_save_close()
        # #  切换到查询页面
        # self.MOAS.switch_to_window()
        # self.MOAS.select_frame_id(self.MOAS.frame_id)
        # self.MOAS.select_frame_id(self.MOAS.iframe_page)
        # self.MOAS.set_table_num(3)
        # self.MOAS.query(user_code)
        # info("选择数据")
        # row = self.MOAS.select_by_user_code(user_code)
        # text = self.MOAS.get_cell_text_by_head("状态", row)
        # self.MOAS.assertEqual("判断状态列的值为”经理解聘“", text, "经理解聘")
        # get_screenshot("营销团队经理解聘查询")
        # info("进入“营销团队经理解聘”页面")
        # self.MOAS.click(
        #     self.MOAS.wait_until_el_xpath(
        #         self.MOAS.input_btn.format("营销团队经理聘任与解聘")))
        # info("切换“营销团队经理解聘”页面")
        # self.DM.switch_to_window()
        # self.DM.maximize_window()
        # info("选择需要解聘的员工")
        # self.DM.select_by_user_code(user_code)
        info("解聘保存并提交")
        self.DM.save_submit()
        self.DM.submit_interaction(iframe_xpath=self.DM.submit_iframe)
        text = self.DM.get_text(self.DM.get_element_xpath(self.DM.save_success))
        self.DM.assertEqual("验证解聘提交成功", text, "保存成功!")
        self.DM.click(self.wait_until_el_xpath(self.submit_close_btn))

    # @pytest.mark.skip
    @allure.story("有效的经理解聘该人员经理职务-复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_YLDLZ_005_recheck(self):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}".format(Test_YLDLZ_005.msg["user_code"]))
        self.ASR.query(Test_YLDLZ_005.msg["user_code"])
        info("进入复核界面")
        self.ASR.select_data("经理解聘复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        info("检查信息点")
        info("复核")
        self.DMR.assertEqual("判断页面标题", self.DMR.get_head_text(), "经理解聘复核")
        self.DMR.recheck_ope(textarea="有效的经理解聘该人员经理职务--ui测试")
        text = self.DMR.get_text(self.DMR.get_element_xpath(self.DMR.save_success))
        self.DMR.assertEqual("验证复核成功", text, "保存成功!")

    # @pytest.mark.skip
    @allure.story("验证审核通过后核对人员信息")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_003_sales_query(self):
        self.SQ.into_page()
        self.SQ.query(Test_YLDLZ_005.msg["user_code"])
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        # self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")

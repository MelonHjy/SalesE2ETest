# -*- coding:utf-8 -*-
# @Time : 2020/7/10 17:22
# @Author: zyb
# @File : test_SALES_YLDLZ_013.py   代理制销售人员代码管理>>代理制销售人员出单权注销（有效人员进行注销）
import allure
import pytest

from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.agent_sales_manage.deputy_check import DeputyCheck
from src.page.base_page import BasePage
from src.page.process_page import ProcessPage
from src.page.table_page import TablePage
from src.utils import csv_util
from src.utils.driver_util import *
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.page.integrated_management.deputy_recheck import DeputyRecheck
from src.utils.except_util import get_screenshot

import os
import jaydebeapi


@allure.feature("代理制销售人员代码管理>>代理制销售人员出单权注销（有效人员进行注销）")
class Test_YLDLZ_013():
    MOAS = ManagementOfAgentSalesmen()
    DC = DeputyCheck()
    BP = BasePage()
    PP = ProcessPage()
    ASR = AgentSalesRecheck()
    DR = DeputyRecheck()
    TP = TablePage()
    msg = None

    data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_013.csv")

    @allure.step("代理制销售人员出单权查询并注销")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    @pytest.mark.parametrize("user_code", data)
    def test_001(self, user_code):
        Test_YLDLZ_013.msg = {"user_code": user_code}
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.MOAS.into_page()
        info("查询人员代码{}并选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, '选择')
        info("进入-->代理制销售人员出单权注销")
        self.MOAS.click_btn("代理制销售人员出单权注销")
        # 专职营销员会出现提示框
        # cancel_text = self.MOAS.get_alert_text()
        # info("提示信息为：" + cancel_text)
        # info("点击确认，进入确认注销页面")
        # self.BP.choose_ok_on_alert()
        info("切换到确认注销页面")
        self.BP.switch_to_window()
        self.BP.maximize_window()
        get_screenshot("注销")
        # 点击确认框
        info("确认页面信息并点击【注销】")
        self.BP.click(self.BP.wait_until_el_xpath(self.DC.dismiss))
        dismiss_reason = '自动化测试出单权注销'
        self.PP.submit_interaction(iframe_xpath=self.DC.submit_iframe, textarea=dismiss_reason)
        text = self.BP.get_text(self.BP.get_element_xpath(self.DC.save_success))
        self.BP.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.PP.close_button_ty()
        # sleep(60)
        # 专职营销员会出现提示框
        # dissmiss_text = self.deputy_check.get_alert_text()
        # info("提示信息为：" + dissmiss_text)
        # self.BP.choose_ok_on_alert()
        # confirm_text = self.deputy_check.get_alert_text()
        # info("提示信息为：" + confirm_text)
        # 点击警示框
        # self.BP.choose_ok_on_alert()
        # sleep(10)
        # 提交到默认岗位
        # 填写审核信息
        # 点击【提交任务】
        # self.BP.switch_to_window()
        # self.MOAS.select_frame_id(self.MOAS.frame_id)
        # self.MOAS.select_frame_id(self.MOAS.iframe_page)
        # self.BP.click(self.MOAS.get_a_by_head(0, '流程查询'))
        # self.BP.switch_to_window()

    # @pytest.mark.skip
    # @allure.step("代理制销售人员出单权注销复核失败打回")
    # @pytest.mark.usefixtures("login_jiangsu_p_fun")
    # def test_002(self):
    #     info("综合管理->销售人员->代理制销售人员代码复核")
    #     self.ASR.into_page()
    #     info("查询人员代码{}".format(Test_YLDLZ_013.msg['user_code']))
    #     self.ASR.query(Test_YLDLZ_013.msg["user_code"])
    #     info("进入注销复核页")
    #     self.ASR.select_data("注销复核")
    #     self.BP.switch_to_window()
    #     self.BP.maximize_window()
    #     info("复核")
    #     self.BP.click(self.BP.wait_until_el_xpath(self.DR.recheck))
    #     review_reason = "自动化测试复核不通过"
    #     # self.BP.select_frame_id("submitFrame")
    #     # self.BP.wait_until_el_xpath(self.DR.submit_iframe)
    #     self.PP.submit_interaction(iframe_xpath=self.DR.submit_iframe, check_state="复核不通过", textarea=review_reason)
    #     text = self.BP.get_text(self.BP.get_element_xpath(self.DC.save_success))
    #     self.BP.assertResult("验证复核成功", "保存成功!" in text)
    #     self.PP.close_button_ty()
    #
    # @pytest.mark.skip
    # @allure.step("代理制销售人员出单权打回终止流程")
    # @pytest.mark.usefixtures("login_jiangsu_p")
    # def test_003(self):
    #     info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
    #     self.MOAS.into_page()
    #     info("查询人员代码{}".format(Test_YLDLZ_013.msg['user_code']))
    #     self.MOAS.query(Test_YLDLZ_013.msg["user_code"], '001')
    #     # self.BP.click(self.TP.get_a_by_head(0, '终止流程'))
    #     self.MOAS.select_data("内部流转码", Test_YLDLZ_013.msg['user_code'], '终止流程')
    #     end_text = self.MOAS.get_alert_text()
    #     info("提示信息为：" + end_text)
    #     self.BP.assertEqual("判断提示信息", end_text, "确认要终止当前流程？")
    #     self.BP.choose_ok_on_alert()
    #     msg = self.MOAS.get_alert_text()
    #     info("提示信息为：" + msg)
    #     self.BP.assertEqual("判断提示信息", end_text, "流程终止成功")

    @allure.step("有效人员进行注销--复核")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @allure.step("代理制销售人员出单权注销复核成功")
    def test_004(self):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}".format(Test_YLDLZ_013.msg['user_code']))
        self.ASR.query(Test_YLDLZ_013.msg["user_code"])
        info("进入注销复核页")
        self.ASR.select_data("注销复核")
        self.BP.switch_to_window()
        self.BP.maximize_window()
        get_screenshot("复核")
        info("复核")
        self.BP.click(self.BP.wait_until_el_xpath(self.DR.recheck))
        review_reason = "自动化测试复核通过"
        self.PP.submit_interaction(iframe_xpath=self.DR.submit_iframe, check_state="复核通过", textarea=review_reason)
        text = self.BP.get_text(self.BP.get_element_xpath(self.DR.save_success))
        self.BP.assertResult("验证复核成功", "保存成功!" in text)
        get_screenshot("提交")
        self.PP.close_button_ty()

    @allure.story("有效人员进行信息变更-查询验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_003(self):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(Test_YLDLZ_013.msg["user_code"]))
        self.MOAS.query(Test_YLDLZ_013.msg["user_code"])
        text = self.MOAS.get_cell_text_by_head("状态", 0)
        self.MOAS.assertEqual("判断是否结束复核状态", text, "手动注销")
        get_screenshot("验证")
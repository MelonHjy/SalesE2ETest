#  -*- coding:utf-8 -*-
# @Time : 2020/8/3 10:39
# @Author: fyl
# @File : test_SALES_YLDLZ_010.py   代理制销售人员代码管理>>团队成员出单权赋予与变更（变更有效团队成员的团队）
import allure
import pytest

from src.page.agent_sales_manage.group_issue import GroupIssue
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.group_issue_recheck import GroupIssueRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot, sleep
from src.utils.log import info

data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_010.csv")


@allure.feature("代理制销售人员代码管理>>团队成员出单权赋予与变更（变更有效团队成员的团队）-010")
@pytest.mark.parametrize("user_code, group_code", data, scope='class')
@pytest.mark.usefixtures("login_jiangsu_p_fun")
class Test_YLDLZ_010():
    MOAS = ManagementOfAgentSalesmen()
    GI = GroupIssue()
    ASR = AgentSalesRecheck()
    GIR = GroupIssueRecheck()

    # data = [("83258549", "32990046--测试0610营销修改")]

    @allure.story("变更有效团队成员的团队")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("restore_data")
    def test_001(self, user_code, group_code):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('团队成员出单权赋予与变更')
        self.GI.assertEqual("判断页面标题", self.GI.get_head_text(), "团队成员出单权变更")
        info("修改团队信息")
        self.GI.code_edit(self.GI.group_code, group_code)
        get_screenshot("修改团队")
        info("保存并提交")
        self.GI.save_deputy()
        self.GI.submit_interaction(iframe_xpath=self.GI.submit_iframe)
        text = self.GI.get_text(self.GI.get_element_xpath(self.GI.save_success))
        self.GI.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GI.close_button_ty()

    @allure.story("变更有效团队成员的团队-复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    # @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002(self, user_code, group_code):
        # self.ASR.switch_to_default_content()
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.ASR.query(user_code1=user_code)
        self.ASR.select_data("出单权变更复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        get_screenshot("复核")
        info("复核")
        self.GIR.assertEqual("判断页面标题", self.GIR.get_head_text(), "出单权变更复核")
        self.GIR.recheck_ope(textarea="变更有效团队成员的团队--ui测试")
        text = self.GIR.get_text(self.GIR.get_element_xpath(self.GIR.save_success))
        self.GIR.assertResult("验证复核成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GIR.close_button_ty()

    @allure.story("变更有效团队成员的团队-验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    # @pytest.mark.usefixtures("login_jiangsu_p")
    def test_003(self, user_code, group_code):
        # self.MOAS.switch_to_window()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('团队成员出单权赋予与变更')
        info("团队成员出单权赋予页")
        self.GI.assertEqual("验证标签文字", self.GI.get_head_text(), "团队成员出单权变更")
        group_code_text = self.GI.get_text(self.GI.wait_until_el_xpath(self.GI.group_code))
        info("团队代码：{}".format(group_code))
        self.GI.assertResult("验证团队代码是否修改成功", group_code_text in group_code)
        get_screenshot("验证")
        sleep(2)

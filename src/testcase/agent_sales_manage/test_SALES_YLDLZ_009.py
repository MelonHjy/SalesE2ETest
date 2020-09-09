#  -*- coding:utf-8 -*-
# @Time : 2020/8/3 10:39
# @Author: fyl
# @File : test_SALES_YLDLZ_009.py   代理制销售人员代码管理>>团队成员出单权赋予与变更（无效人员复效为团队成员）
import allure
import pytest

from config.global_var import sleep
from src.page.agent_sales_manage.group_issue import GroupIssue
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.group_issue_recheck import GroupIssueRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_009.csv")


@pytest.mark.parametrize("user_code, contractstartdate1, contractenddate1, ruleNo", data, scope='class')
@pytest.mark.usefixtures("login_jiangsu_p")
@allure.feature("代理制销售人员代码管理>>团队成员出单权赋予与变更（无效人员复效为团队成员）-009")
class Test_YLDLZ_009():
    MOAS = ManagementOfAgentSalesmen()
    GI = GroupIssue()
    ASR = AgentSalesRecheck()
    GIR = GroupIssueRecheck()

    @allure.story("无效人员复效为团队成员")
    @pytest.mark.usefixtures("restore_data")
    @pytest.mark.dependency(name='test_001')
    def test_001(self, user_code, contractstartdate1, contractenddate1, ruleNo):
        self.MOAS.switch_to_default_content()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询无效人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('团队成员出单权赋予与变更')
        self.MOAS.assertEqual("判断页面标题", self.GI.get_head_text(), "团队成员出单权赋予")
        info("切换合同信息页")
        self.GI.switch_contract_tab()
        info("资格证号码-->执业证号码-->合同起始日期-->合同终止日期-->佣金配置")
        self.GI.select("//*[@id='agentno1']",
                       self.GI.get_attribute(self.GI.get_element_xpath(self.GI.qualifyno.format('0')), 'value'))
        self.GI.select("//*[@id='credentialno1']",
                       self.GI.get_attribute(self.GI.get_element_xpath(self.GI.qualifyno.format('1')), 'value'))
        self.GI.input_contract1(contractstartdate1, contractenddate1, ruleNo)
        self.GI.js_group(self.GI.ruleNo, self.GI.saUContracts1.format('1'), ruleNo)
        get_screenshot("合同信息")
        self.GI.switch_user_tab()
        info("切换基本信息页->保存并提交")
        self.GI.click(self.GI.get_element_xpath(self.GI.save_commit1))
        self.GI.submit_interaction(iframe_xpath=self.GI.submit_iframe)
        text = self.GI.get_text(self.GI.get_element_xpath(self.GI.save_success))
        self.GI.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GI.close_button_ty()
        self.GI.switch_to_window()

    @allure.story("无效人员复效为团队成员-复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    def test_002(self, user_code, contractstartdate1, contractenddate1, ruleNo):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询无效人员代码{}->选择".format(user_code))
        self.ASR.query(user_code1=user_code)
        self.ASR.select_data("出单权赋予复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        get_screenshot("复核")
        self.GIR.assertEqual("判断页面标题", self.GIR.get_head_text(), "出单权赋予复核")
        info("复核")
        self.GIR.recheck_ope(textarea="无效人员复效为团队成员--ui测试")
        text = self.GIR.get_text(self.GIR.get_element_xpath(self.GIR.save_success))
        self.GIR.assertEqual("验证复核成功", text, "保存成功!")
        get_screenshot("提交")
        self.GIR.close_button_ty()
        self.GIR.switch_to_window()

    @allure.story("代理制销售人员代码查询验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    def test_003(self, user_code, contractstartdate1, contractenddate1, ruleNo):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}".format(user_code))
        self.MOAS.query(user_code1=user_code)
        status = self.MOAS.get_cell_text_by_head("状态", 0)
        self.MOAS.assertEqual("验证团队成员状态为‘有效’", status, "有效")
        process = self.MOAS.get_cell_text_by_head("终止流程", 0)
        self.MOAS.assertEqual("判断最后一栏没有终止流程按钮", process, "")
        get_screenshot("验证")
        sleep(2)

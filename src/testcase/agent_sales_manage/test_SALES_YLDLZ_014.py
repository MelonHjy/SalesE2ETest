#  -*- coding:utf-8 -*-
# @Time : 2020/8/4 10:39
# @Author: fyl
# @File : test_SALES_YLDLZ_014.py   代理制销售人员代码管理>>合同续签（有效人员进行合同续签）
import allure
import pytest

from src.page.agent_sales_manage.contract_renewal import ContractRenewal
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.contract_renewal_recheck import ContractRenewalRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.log import info


@allure.feature("代理制销售人员代码管理>>合同续签（有效人员进行合同续签）")
class Test_YLDLZ_014():
    MOAS = ManagementOfAgentSalesmen()
    CR = ContractRenewal()
    ASR = AgentSalesRecheck()
    CRR = ContractRenewalRecheck()
    msg = None

    data = csv_util.data_reader("agent_sales_manage/014_data.csv")
    # data = [("83258572")]   # 83258551  83258572  83258562

    @allure.story("合同续签（有效人员进行合同续签）")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.parametrize("user_code", data)
    def test_001(self, user_code):
        Test_YLDLZ_014.msg = {"usercode": user_code}
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("合同续签")
        self.MOAS.click_btn("合同续签")
        self.CR.assertEqual("判断页面标题", self.CR.get_head_text(), "人员合同续签")
        Test_YLDLZ_014.msg = {"contract_start_date": self.CR.get_value(self.CR.contract_start_date),
                              "contract_end_date": self.CR.get_value(self.CR.contract_end_date)}
        info("保存并提交")
        self.CR.click(self.CR.get_element_xpath(self.CR.renew))
        self.CR.submit_interaction(self.CR.submit_iframe)

    @allure.story("省级销售管理综合岗复核流程")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.parametrize("user_code", data)
    def test_002(self, user_code):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.ASR.query(user_code)
        self.ASR.select_data("续签复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        self.CRR.assertEqual("判断页面标题", self.CR.get_head_text(), "人员合同续签复核")
        contract_start_date = self.CRR.get_text(self.CRR.get_element_xpath(self.CRR.contract_start_date))
        contract_end_date = self.CRR.get_text(self.CRR.get_element_xpath(self.CRR.contract_end_date))
        self.CRR.assertEqual("验证合同起始日期",contract_start_date, Test_YLDLZ_014.msg["contract_start_date"])
        self.CRR.assertEqual("验证合同终止日期",contract_end_date, Test_YLDLZ_014.msg["contract_end_date"])
        info("复核")
        self.CRR.click(self.CRR.get_element_xpath(self.CRR.success))
        self.CRR.submit_interaction(self.CRR.submit_iframe,textarea="合同续签（有效人员进行合同续签）--ui测试")

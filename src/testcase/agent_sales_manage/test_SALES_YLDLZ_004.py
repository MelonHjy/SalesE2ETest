#  -*- coding:utf-8 -*-
# @Time : 2020/7/30 16:23
# @Author: fyl
# @File : test_SALES_YLDLZ_004.py   代理制人员代码管理>>营销团队经理聘任与解聘（无效人员复效并任命为经理）
import allure
import pytest

from config.global_var import sleep
from src.page.Personal_agency_channel.sales_query import SalesQuery
from src.page.agent_sales_manage.appointment_manager import AppointmentManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.appointment_manager_recheck import AppointmentManagerRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_004.csv")


@pytest.mark.usefixtures("login_jiangsu_p")
@pytest.mark.parametrize("user_code, contractstartdate0, contractenddate0, ruleNo", data, scope='class')
@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘（无效人员复效并任命为经理）-004")
class Test_YLDLZ_004():
    MOAS = ManagementOfAgentSalesmen()
    AM = AppointmentManager()
    ASR = AgentSalesRecheck()
    AMR = AppointmentManagerRecheck()
    SQ = SalesQuery()

    @allure.story("无效人员复效并任命为经理")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("restore_data")
    def test_001_appointment(self, user_code, contractstartdate0, contractenddate0, ruleNo):
        self.MOAS.switch_to_default_content()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询无效人员{}".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("营销团队经理聘任与解聘")))
        # self.MOAS.select_appointment()
        self.AM.switch_to_window()
        self.AM.maximize_window()
        self.AM.assertEqual("判断页面标题", self.AM.get_head_text(), "营销团队经理聘任")
        self.AM.select_rolecode("经理")
        get_screenshot("基本信息")
        self.AM.switch_contract_tab()
        info("填写合同基本信息（资格证号码,执业证号码,合同起始日期,合同终止日期,佣金配置）")
        self.AM.select("//*[@id='agentno0']",
                       self.AM.get_attribute(self.AM.get_element_xpath(self.AM.qualifyno.format('0')), 'value'))
        self.AM.select("//*[@id='credentialno0']",
                       self.AM.get_attribute(self.AM.get_element_xpath(self.AM.qualifyno.format('1')), 'value'))
        # 日期组件
        self.AM.pick_date_old("//*[@id='imgBtncon1[0]']", contractstartdate0)
        self.AM.pick_date_old("//*[@id='imgBtncon2[0]']", contractenddate0)
        self.AM.js_group(self.AM.ruleNo, self.AM.saUContracts1.format('0'), ruleNo)
        # self.AM.code_select(self.AM.ruleNo, ruleNo)
        get_screenshot("合同信息")
        self.AM.switch_user_tab()
        info("聘任保存并提交")
        self.AM.prepare_save_commit()
        self.AM.submit_interaction(self.AM.submit_iframe)
        text = self.AM.get_text(self.AM.get_element_xpath(self.AM.save_success))
        self.AM.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.AM.close_button_ty()

    @allure.story("无效人员复效并任命为经理--复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    def test_002_rechect(self, user_code, contractstartdate0, contractenddate0, ruleNo):
        self.ASR.switch_to_window()
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询{}".format(user_code))
        self.ASR.query(user_code)
        self.ASR.select_data("经理聘任复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        get_screenshot("复核")
        info("复核")
        self.AMR.assertEqual("判断页面标题", self.AMR.get_head_text(), "经理聘任复核")
        self.AMR.recheck_ope(textarea="无效团队成员任命为经理--ui测试")
        get_screenshot("提交")
        self.AMR.close_button_ty()

    @allure.story("验证审核通过后核对人员信息")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    def test_003_sales_query(self, user_code, contractstartdate0, contractenddate0, ruleNo):
        self.SQ.switch_to_window()
        info("个代渠道->销售人员->销售人员查询")
        self.SQ.into_page()
        self.SQ.query(user_code)
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")
        # get_screenshot("验证")
        sleep(2)

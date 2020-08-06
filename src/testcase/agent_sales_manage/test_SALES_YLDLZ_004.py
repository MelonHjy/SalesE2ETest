#  -*- coding:utf-8 -*-
# @Time : 2020/7/30 16:23
# @Author: fyl
# @File : test_SALES_YLDLZ_004.py   代理制人员代码管理>>营销团队经理聘任与解聘（无效人员复效并任命为经理）
import allure
import pytest

from src.page.Personal_agency_channel.sales_query import SalesQuery
from src.page.agent_sales_manage.appointment_manager import AppointmentManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.base_page import BasePage
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.log import info


@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘（无效人员复效并任命为经理）")
class Test_YLDLZ_002():
    MOAS = ManagementOfAgentSalesmen()
    AM = AppointmentManager()
    BP = BasePage()
    ASR = AgentSalesRecheck()
    SQ = SalesQuery()
    # data = [("83258575", "123456", "321321", "2020-07-08", '2022-07-08', "RULE20120000000000001--保险经纪公司")]
    # data1 = [("83258575")]
    data = csv_util.data_reader("agent_sales_manage/004_data.csv")
    data1 = csv_util.data_reader("agent_sales_manage/004_data1.csv")

    @allure.story("提交无效人员任命为经理")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.parametrize("user_code, qualifyno, qualifyno1, contractstartdate0, contractenddate0, ruleNo", data)
    def test_001_appointment(self, user_code, qualifyno, qualifyno1, contractstartdate0, contractenddate0, ruleNo):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询无效人员{}".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("营销团队经理聘任与解聘")))
        self.MOAS.select_appointment()
        self.AM.switch_to_window()
        self.AM.maximize_window()
        self.AM.assertEqual("判断页面标题", self.AM.get_head_text(), "营销团队经理聘任")
        self.AM.select_rolecode("经理")
        self.AM.switch_contract_tab()
        info("填写合同基本信息（资格证号码,执业证号码,合同起始日期,合同终止日期,佣金配置）")
        self.AM.select("//*[@id='agentno1']", qualifyno)
        self.AM.select("//*[@id='credentialno1']", qualifyno1)
        # 日期组件
        self.AM.pick_date_old("//*[@id='imgBtncon1[1]']", contractstartdate0)
        self.AM.pick_date_old("//*[@id='imgBtncon2[1]']", contractenddate0)
        self.AM.code_select(self.AM.ruleNo, ruleNo)
        self.AM.switch_user_tab()
        info("聘任保存并提交")
        self.AM.prepare_save_commit()
        self.AM.submit_interaction(self.AM.submit_iframe)
        # 关闭
        self.AM.click(self.AM.wait_until_el_xpath(self.AM.close_over))  # 关闭不了

    @allure.story("省级销售管理综合岗复核流程")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.parametrize("user_code", data1)
    def test_002_rechect(self, user_code):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询{}".format(user_code))
        self.ASR.query(user_code)
        info("复核页面")
        self.ASR.select_data("经理聘任复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        info("复核")
        self.ASR.recheck_ope(textarea="无效人员聘任经理ui测试")

    @allure.story("验证审核通过后核对人员信息")
    @pytest.mark.parametrize("user_code", data1)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_sales_query(self, user_code):
        self.SQ.into_page()
        self.SQ.query(user_code)
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")

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
from src.page.integrated_management.appointment_manager_recheck import AppointmentManagerRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.log import info


@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘（无效人员复效并任命为经理）")
class Test_YLDLZ_004():
    MOAS = ManagementOfAgentSalesmen()
    AM = AppointmentManager()
    ASR = AgentSalesRecheck()
    AMR = AppointmentManagerRecheck()
    SQ = SalesQuery()
    user_code = None

    data = csv_util.data_reader("agent_sales_manage/004_data.csv")

    @allure.story("无效人员复效并任命为经理")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize("user_code, contractstartdate0, contractenddate0, ruleNo", data)
    def test_001_appointment(self, user_code, contractstartdate0, contractenddate0, ruleNo):
        Test_YLDLZ_004.user_code = user_code
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询无效人员{}".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("营销团队经理聘任与解聘")))
        # self.MOAS.select_appointment()
        # self.AM.switch_to_window()
        # self.AM.maximize_window()
        self.AM.open_url("http://10.10.1.104:8001/sales/deputy/engageOrFire.do?saUUser.userid=1000000002297827&efOrmau=e#")
        self.AM.assertEqual("判断页面标题", self.AM.get_head_text(), "营销团队经理聘任")
        self.AM.select_rolecode("经理")
        self.AM.switch_contract_tab()
        info("填写合同基本信息（资格证号码,执业证号码,合同起始日期,合同终止日期,佣金配置）")
        self.AM.select("//*[@id='agentno1']", self.AM.get_attribute(self.AM.get_element_xpath(self.AM.qualifyno.format('0')),'value'))
        self.AM.select("//*[@id='credentialno1']", self.AM.get_attribute(self.AM.get_element_xpath(self.AM.qualifyno.format('1')),'value'))
        # 日期组件
        self.AM.pick_date_old("//*[@id='imgBtncon1[1]']", contractstartdate0)
        self.AM.pick_date_old("//*[@id='imgBtncon2[1]']", contractenddate0)
        self.AM.js_group(self.AM.ruleNo,self.AM.saUContracts1.format('1'),ruleNo)
        # self.AM.code_select(self.AM.ruleNo, ruleNo)
        self.AM.switch_user_tab()
        info("聘任保存并提交")
        self.AM.prepare_save_commit()
        self.AM.submit_interaction(self.AM.submit_iframe)
        # 关闭
        self.AM.click(self.AM.wait_until_el_xpath(self.AM.close_over))  # 关闭不了

    @allure.story("无效人员复效并任命为经理--复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002_rechect(self):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询{}".format(Test_YLDLZ_004.user_code))
        self.ASR.query(Test_YLDLZ_004.user_code)
        self.ASR.select_data("经理聘任复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        info("复核")
        self.AMR.assertEqual("判断页面标题", self.AMR.get_head_text(), "经理聘任复核")
        self.AMR.recheck_ope(textarea="无效团队成员任命为经理--ui测试")

    @allure.story("验证审核通过后核对人员信息")
    @pytest.mark.dependency(name='test_003', depends=["test_001","test_002"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_sales_query(self):
        self.SQ.into_page()
        self.SQ.query(Test_YLDLZ_004.user_code)
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")

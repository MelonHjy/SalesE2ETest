#  -*- coding:utf-8 -*-
# @Time : 2020/8/3 10:39
# @Author: fyl
# @File : test_SALES_YLDLZ_011.py   代理制销售人员代码管理>>代理制销售人员信息变更（有效人员进行信息变更)
import allure
import pytest

from src.page.agent_sales_manage.edit_agent_sales_msg import EditAgentSaleMsg
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.edit_agent_sales_msg_recheck import EditAgentSaleMsgRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("代理制销售人员代码管理>>代理制销售人员信息变更（有效人员进行信息变更)")
class Test_YLDLZ_011():
    MOAS = ManagementOfAgentSalesmen()
    EASM = EditAgentSaleMsg()
    ASR = AgentSalesRecheck()
    EASMR = EditAgentSaleMsgRecheck()
    msg = None

    data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_011.csv")
    # data = [(
    #     "83258580", "13111111111", "汉族", "共青团员", "本科", "资格证", "111111", "2018-01-17", "B", "执业证", "222222",
    #     "2018-02-15", "2019-07-10", "2021-08-13")]

    @allure.story("有效人员进行信息变更")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    @pytest.mark.parametrize("user_code, mobile, nation, visage, culture, qualifytype,  qualifyno,"
                             "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
                             "contractenddate0", data)
    def test_001(self, user_code, mobile, nation, visage, culture, qualifytype, qualifyno,
                 qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,
                 contractenddate0):
        Test_YLDLZ_011.msg = {"usercode": user_code}
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("进入代理制销售人员信息变更页")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("代理制销售人员信息变更")))
        self.MOAS.select_dismissal()
        self.MOAS.switch_to_window()
        self.MOAS.maximize_window()
        self.EASM.assertEqual("判断页面标题", self.EASM.get_head_text(), "代理制销售人员信息变更")
        info("修改->手机号码->民族->政治面貌->学历")
        self.EASM.send_keys(self.EASM.wait_until_el_xpath(self.EASM.mobile), mobile)
        self.EASM.select_nation(nation)
        self.EASM.select_visage(visage)
        self.EASM.select_culture(culture)
        get_screenshot("变更基本信息")
        info("切换合同信息页")
        self.EASM.switch_contract_tab()
        info("修改->资质信息")
        self.EASM.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        self.EASM.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("修改->合同信息")
        self.EASM.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0)
        get_screenshot("变更合同信息")
        info("切换人员信息页")
        self.EASM.switch_user_tab()
        info("保存并提交")
        self.EASM.save_commit()
        self.EASM.submit_process()
        text = self.EASM.get_text(self.EASM.get_element_xpath(self.EASM.save_success))
        self.EASM.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")

    @allure.story("有效人员进行信息变更-复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002(self):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(Test_YLDLZ_011.msg["usercode"]))
        self.ASR.query(user_code1=Test_YLDLZ_011.msg["usercode"])
        self.ASR.select_data("信息变更复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        self.EASMR.assertEqual("判断页面标题", self.EASMR.get_head_text(), "信息变更复核")
        get_screenshot("复核")
        info("复核")
        self.EASMR.recheck_ope(textarea="有效人员进行信息变更--ui测试")
        text = self.EASMR.get_text(self.EASMR.get_element_xpath(self.EASMR.save_success))
        self.EASMR.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        # self.EASMR.click(self.ASR.wait_until_el_xpath(self.EASMR.submit_close))

    @allure.story("有效人员进行信息变更-查询验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_003(self):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(Test_YLDLZ_011.msg["usercode"]))
        self.MOAS.query(Test_YLDLZ_011.msg["usercode"])
        text = self.MOAS.get_cell_text_by_head("状态", 0)
        self.MOAS.assertEqual("判断是否结束复核状态", text, "有效")
        get_screenshot("验证")

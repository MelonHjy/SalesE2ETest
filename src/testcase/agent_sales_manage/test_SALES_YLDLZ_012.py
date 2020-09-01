#  -*- coding:utf-8 -*-
# @Time : 2020/8/4 16:10
# @Author: fyl
# @File : test_SALES_YLDLZ_012.py   代理制销售人员代码管理>>代理制销售人员信息变更(无效人员进行信息变更)
import allure
import pytest

from src.page.agent_sales_manage.edit_agent_sales_msg import EditAgentSaleMsg
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_012.csv")


@pytest.mark.parametrize("user_code, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName",
                         data,scope='class')
@allure.feature("代理制销售人员代码管理>>代理制销售人员信息变更(无效人员进行信息变更)")
class Test_YLDLZ_012():
    MOAS = ManagementOfAgentSalesmen()
    EASM = EditAgentSaleMsg()
    ASR = AgentSalesRecheck()
    msg = None

    # data = [("83258561", "1112223334521", "折", "交通银行", "天津市_天津市", "交通银行天津南开支行")]#83258557


    @allure.story("无效人员进行信息变更")
    @pytest.mark.usefixtures("login_jiangsu_p","restore_data")

    def test_001(self, user_code, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        self.MOAS.switch_to_default_content()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("进入代理制销售人员信息变更页")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("代理制销售人员信息变更")))
        self.MOAS.select_appointment()
        self.MOAS.switch_to_window()
        self.MOAS.maximize_window()
        self.EASM.assertEqual("判断页面标题", self.EASM.get_head_text(), "无效/有效人员修改账户")
        info("修改->收款人账号->账号类型->银行名称->银行区域名称->联行号")
        self.EASM.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName)
        self.EASM.manage_account()
        get_screenshot("变更账号信息")
        self.EASM.close_tab()
        # self.EASM.click(self.EASM.wait_until_el_xpath(self.EASM.close_btn))

    @allure.story("无效人员进行信息变更-验证修改信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_002(self, user_code, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        self.MOAS.switch_to_window()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码{}->选择".format(user_code))
        self.MOAS.query(user_code)
        self.MOAS.select_data("内部流转码", user_code, "选择")
        info("进入代理制销售人员信息变更页")
        self.MOAS.click(self.MOAS.wait_until_el_xpath(self.MOAS.input_btn.format("代理制销售人员信息变更")))
        self.MOAS.select_appointment()
        self.MOAS.switch_to_window()
        self.MOAS.maximize_window()
        get_screenshot("验证")
        self.EASM.assertEqual("验证标签文字", self.EASM.get_head_text(), "无效/有效人员修改账户")
        self.EASM.assertEqual("验证账号",
                              self.EASM.get_attribute(self.EASM.get_element_xpath(self.EASM.accountno), 'value'),
                              accountno)

        self.EASM.assertEqual("验证账号类型", self.EASM.get_cardtype(), cardtype)
        self.EASM.assertEqual("验证银行名称",
                              self.EASM.get_attribute(self.EASM.get_element_xpath(self.EASM.saDAccount_bankName),
                                                      'value'),
                              saDAccount_bankName)
        self.EASM.assertEqual("验证银行区域名称",
                              self.EASM.get_attribute(self.EASM.get_element_xpath(self.EASM.saDAccount_bankareaname),
                                                      'value'),
                              saDAccount_bankareaname)
        self.EASM.assertEqual("验证联行号",
                              self.EASM.get_attribute(self.EASM.get_element_xpath(self.EASM.bankName), 'value'),
                              bankName)
        #get_screenshot("验证")

# -*- coding:utf-8 -*-
# @Time : 2020/6/28 17:22
# @Author: fyl
# @File : test_SALES_YLDLZ_001.py   代理制人员代码管理>>营销团队经理聘任与解聘(新增人员聘任为经理)
import random

import allure
import pytest

from config.global_var import sleep
from src.page.agent_sales_manage.appointment_manager import AppointmentManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.appointment_manager_recheck import AppointmentManagerRecheck
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils import csv_util
from src.utils.create_identity import IdNumber
from src.utils.driver_util import *
from src.utils.except_util import get_screenshot

data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_001.csv")


@allure.feature("代理制人员代码管理>>营销团队经理聘任与解聘(新增人员聘任为经理)-001")
@pytest.mark.parametrize(
    "userName, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,"
    "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
    "contractenddate0, ruleNo, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
    "bankName", data, scope='class')
@pytest.mark.usefixtures("login_jiangsu_p_fun")
class Test_YLDLZ_001():
    AM = AppointmentManager()
    MOAS = ManagementOfAgentSalesmen()
    ASR = AgentSalesRecheck()
    AMR = AppointmentManagerRecheck()

    # data = [("杨闰圣ui测试", "61011519990217147x", "13311212125", "32990038--测试0506营销", "经理", "汉族", "中共党员", "研究生")]
    # data1 = [("资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2020-07-08", '2022-07-08',
    #           "RULE20120000000000001--保险经纪公司", "1234567891011", "折", "中国工商银行股份有限公司",
    #           "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]
    # data2 = [("杨闰圣ui测试", "61011519990217147x", "32000000", "测试0506营销")]

    msg = None

    @allure.story("新增人员聘任为经理--填写信息")
    @pytest.mark.dependency(name='test_001')
    # @pytest.mark.usefixtures("flash_idcard")
    def test_001(self, userName, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,
                 qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,
                 contractenddate0, ruleNo, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
        idCard = IdNumber.generate_id(random_sex)  # 随机生成身份证号
        accountno = idCard[0:13]
        info("身份证：{0}，银行账号：{1}".format(idCard,accountno))
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.MOAS.into_page()
        self.MOAS.click_btn('营销团队经理聘任与解聘')
        info("营销团队经理聘任与解聘检查")
        self.AM.assertEqual("判断页面标题", self.AM.get_head_text(), "营销团队经理聘任")
        info("填入基本信息")
        self.AM.user_tab_input(userName, idCard, mobile)
        self.AM.select_group(group)
        # self.AM.js_group(self.AM.group_code, self.AM.group_name, group, self.AM.group_code_hold, groupcodehold)
        self.AM.select_rolecode(rolecode)
        self.AM.select_nation(nation)
        self.AM.select_visage(visage)
        self.AM.select_culture(culture)
        info("检查填写身份证号码后，性别和出生日期是否自动填入")
        self.AM.select(self.AM.sex, self.AM.get_sex_by_idCard(idCard))
        # self.AM.assertEqual("验证出生日期是否与身份证匹配", self.AM.get_birthday(),
        #                     self.AM.get_birthday_by_idCard(idCard))
        get_screenshot("基本信息")
        self.AM.switch_contract_tab()
        self.AM.add_user_button()
        self.AM.add_user_button()
        info("填写'资格证'资质信息-->证件类型,证件号码,发证日期,证件类型")
        self.AM.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        info("填写'执业证'资质信息-->证件类型,证件号码,发证日期")
        self.AM.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("填写合同基本信息（资格证号码,执业证号码,合同起始日期,合同终止日期,佣金配置）")
        self.AM.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0,
                               ruleNo)
        self.AM.js_group(self.AM.ruleNo, self.AM.saUContracts1.format('0'), ruleNo)
        info("填写账户信息（收款人账号,卡折标志,银行名称,银行区域名称,联行号）")
        self.AM.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,
                              bankName)
        get_screenshot("合同信息")
        self.AM.switch_user_tab()
        self.AM.click(self.AM.wait_until_el_xpath(self.AM.save_commit1))
        self.AM.submit_interaction(iframe_xpath=self.AM.submit_iframe)
        info("获取人员代码，合同号")
        Test_YLDLZ_001.msg = self.AM.get_msg()
        info(Test_YLDLZ_001.msg)
        text = self.AM.get_text(self.AM.get_element_xpath(self.AM.save_success))
        self.AM.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.AM.close_button_ty()

    @allure.story("新增人员聘任为经理--复核")
    # @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    def test_002(self, userName, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,
                 qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,
                 contractenddate0, ruleNo, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        # self.ASR.switch_to_default_content()
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}".format(Test_YLDLZ_001.msg['usercode']))
        self.ASR.query(Test_YLDLZ_001.msg['usercode'])
        info("进入聘任经理复核页")
        status_list = self.ASR.get_cell_text_by_head('审核状态')
        index = status_list.index("经理聘任复核")
        self.ASR.click(self.ASR.get_a_by_head(index, '操作'))
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        info("检查信息点")
        get_screenshot("复核页")
        info("复核")
        self.AMR.recheck_ope(textarea="新增人员聘任为经理--ui自动化测试")
        get_screenshot("提交")
        self.AMR.close_button_ty()

    @allure.story("新增人员聘任为经理--验证人员状态")
    # @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_003', depends=['test_002'])
    def test_003(self, userName, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,
                 qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,
                 contractenddate0, ruleNo, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName):
        # self.MOAS.switch_to_window()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码：{}，未提交状态".format(Test_YLDLZ_001.msg["usercode"]))
        self.MOAS.query(Test_YLDLZ_001.msg["usercode"])
        self.MOAS.assertEqual("判断该人员状态为‘有效’", self.MOAS.get_cell_text_by_head("状态", 0), "有效")

        # get_screenshot("复核页")
        sleep(2)

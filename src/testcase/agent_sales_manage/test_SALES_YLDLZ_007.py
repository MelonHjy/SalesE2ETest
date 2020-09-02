#  -*- coding:utf-8 -*-
# @Time : 2020/7/27 10:39
# @Author: fyl
# @File : test_SALES_YLDLZ_007.py   代理制人员代码管理>>团队成员出单权赋予与变更（新增普通代理制成员）  待测
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

data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_007.csv")
@pytest.mark.parametrize("username, id_cards, mobile, group_com, nation, visage, culture,qualifytype, qualifyno,"
                             "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
                             "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
                             "bankName", data,scope='class')
@allure.feature("代理制销售人员代码管理>>团队成员出单权赋予与变更（新增普通代理制成员）-007")
class Test_YLDLZ_007():
    MOAS = ManagementOfAgentSalesmen()
    GI = GroupIssue()
    ASR = AgentSalesRecheck()
    GIR = GroupIssueRecheck()
    msg = None

    # data = [("甘冬龙ui测试", "370126198007046159", "13999999999", "32990000--测试0519营销", "汉族", "中共党员", "研究生")]
    # data1 = [("资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2020-07-08", '2022-07-08',
    #           "RULE20120000000000001--保险经纪公司", "121222333529", "折", "中国工商银行股份有限公司",
    #           "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]

    # data1 = csv_util.data_reader("agent_sales_manage/007_data1.csv")

    @allure.story("新增普通代理制成员-填写信息")
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    @pytest.mark.dependency(name='test_001')
    def test_001_base_msg(self, username, id_cards, mobile, group_com, nation, visage, culture, qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1, qualifyno1,
                             qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                             saDAccount_bankName, saDAccount_bankareaname, bankName):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('团队成员出单权赋予与变更')
        self.GI.assertEqual("判断页面标题", self.GI.get_head_text(), "团队成员出单权赋予")
        info("填入姓名:{0}->身份证号：{1}->手机号码：{2}".format(username, id_cards, mobile))
        self.GI.user_tab_input(username, id_cards, mobile)
        info("选择上级机构:32000000--中国人民财产保险股份有限公司江苏省分公司，归属机构:{0}".format(group_com))
        self.GI.select_org(self.GI.com_code, "32000000--中国人民财产保险股份有限公司江苏省分公司")
        self.GI.select_org(self.GI.group_code, group_com)
        info("民族:{0}->政治面貌:{1}->学历:{2}".format(nation, visage, culture))
        self.GI.select_base(nation, visage, culture)
        get_screenshot("基本信息")
        info("切换到合同信息tab")
        self.GI.switch_contract_tab()
        self.GI.add_user_button()
        self.GI.add_user_button()
        info("证件类型:{0}->证件号码：{1}->发证日期：{2}->证件类型：{3}".format(qualifytype, qualifyno, qualifystartdate, agentType))
        self.GI.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        info("证件类型:{0}->证件号码：{1}->发证日期：{2}".format(qualifytype1, qualifyno1, qualifystartdate1))
        self.GI.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("资格证号码:{0}->执业证号码：{1}->合同起始日期：{2}->合同终止日期：{3}->佣金配置：{4}".format(qualifyno, qualifyno1, contractstartdate0,
                                                                             contractenddate0, ruleNo))
        self.GI.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0, ruleNo)
        self.GI.js_group(self.GI.ruleNo, self.GI.saUContracts1.format('0'), ruleNo)
        info("收款人账号:{0}->卡折标志:{1}->银行名称：{2}->银行区域名称：{3}->联行号：{4}".format(accountno, cardtype, saDAccount_bankName,
                                                                         saDAccount_bankareaname, bankName))
        self.GI.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName)
        get_screenshot("合同信息")
        info("切换到基本信息tab")
        self.GI.switch_user_tab()
        info("保存并提交")
        self.GI.click(self.GI.get_element_xpath(self.GI.add_deputy))
        self.GI.submit_interaction(iframe_xpath=self.GI.submit_iframe)
        # self.GI.choose_ok_on_alert()
        # sleep(3)
        Test_YLDLZ_007.msg = self.GI.get_msg()
        info("人员代码{0}，合同号{1}".format(Test_YLDLZ_007.msg['usercode'], Test_YLDLZ_007.msg['contract']))
        text = self.GI.get_text(self.GI.get_element_xpath(self.GI.save_success))
        self.GI.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GI.close_button_ty()

    @allure.story("新增普通代理制成员-复核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_002_issue_recheck(self, username, id_cards, mobile, group_com, nation, visage, culture, qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1, qualifyno1,
                             qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                             saDAccount_bankName, saDAccount_bankareaname, bankName):
        self.ASR.switch_to_default_content()
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}".format(Test_YLDLZ_007.msg['usercode']))
        self.ASR.query(Test_YLDLZ_007.msg['usercode'])
        # 选择指定状态的数据进入复核页面
        self.ASR.select_data("出单权赋予复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        # 复核信息检查
        self.GIR.assertEqual("判断页面标题", self.GIR.get_head_text(), "出单权赋予复核")
        get_screenshot("复核")
        info("复核")
        self.GIR.recheck_ope(textarea="新增普通代理制成员-ui测试")
        text = self.GIR.get_text(self.GIR.get_element_xpath(self.GIR.save_success))
        self.GIR.assertEqual("验证复核成功", text, "保存成功!")
        get_screenshot("提交")
        self.GIR.close_button_ty()

    @allure.story("新增普通代理制成员查询验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_003(self, username, id_cards, mobile, group_com, nation, visage, culture, qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1, qualifyno1,
                             qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                             saDAccount_bankName, saDAccount_bankareaname, bankName):
        self.MOAS.switch_to_window()
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询无效人员代码{}->选择".format(Test_YLDLZ_007.msg['usercode']))
        self.MOAS.query(user_code1=Test_YLDLZ_007.msg['usercode'])
        status = self.MOAS.get_cell_text_by_head("状态", 0)
        self.MOAS.assertEqual("验证团队成员状态为‘有效’", status, "有效")
        process = self.MOAS.get_cell_text_by_head("终止流程", 0)
        self.MOAS.assertEqual("判断最后一栏没有终止流程按钮", process, "")
        get_screenshot("验证")

#  -*- coding:utf-8 -*-
# @Time : 2020/8/5 14:56
# @Author: fyl
# @File : test_SALES_YLDLZ_015.py   代理制销售人员代码管理>>团队成员出单权赋予与变更（人员转制-无效的合同制销售/合同制非销售转制为代理制人员)-（团队成员出单权赋予）
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


@allure.feature("团队成员出单权赋予与变更（人员转制-无效的合同制销售/合同制非销售转制为代理制人员)-（团队成员出单权赋予）")
class Test_YLDLZ_015():
    MOAS = ManagementOfAgentSalesmen()
    GI = GroupIssue()
    ASR = AgentSalesRecheck()
    GIR = GroupIssueRecheck()
    msg = None

    data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_015.csv")
    # data1 = csv_util.data_reader("agent_sales_manage/015_data1.csv")

    @allure.story("人员转制-（团队成员出单权赋予）")
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize(
        "id_cards,com_group,group,qualifytype,qualifyno,qualifystartdate,agentType,qualifytype1,qualifyno1,qualifystartdate1,contractstartdate0,contractenddate0,ruleNo,accountno,cardtype,saDAccount_bankName,saDAccount_bankareaname,bankName",
        data)
    def test_001(self, id_cards, com_group, group, qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1,
                 qualifyno1, qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                 saDAccount_bankName, saDAccount_bankareaname, bankName):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('团队成员出单权赋予与变更')
        self.GI.assertEqual("判断页面标题", self.GI.get_head_text(), "团队成员出单权赋予")
        info("填入身份证号：{}".format(id_cards))
        self.GI.send_keys(self.GI.get_element_xpath(self.GI.id_cards), id_cards)
        self.GI.switch_user_tab()
        info("提示框信息：{}".format(self.GI.get_alert_text()))
        self.GI.choose_ok_on_alert()
        sleep(2)
        user_code = self.GI.get_attribute(self.GI.wait_until_el_xpath(self.GI.user_code), 'value')
        info("人员代码：{}".format(user_code))
        Test_YLDLZ_015.msg = {"user_code": user_code}
        info("选择归属机构:{0}".format(group))
        # self.GI.js_group(self.GI.group_code, self.GI.group_name, group, self.GI.group_code_hold, group_code_hold)
        self.GI.select_org(self.GI.com_code, com_group)
        self.GI.select_org(self.GI.group_code, group)
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
        self.GI.click(self.GI.get_element_xpath(self.GI.save_commit1))
        sleep(3)
        self.GI.submit_interaction(self.GI.submit_iframe)
        text = self.GI.get_text(self.GI.get_element_xpath(self.GI.save_success))
        self.GI.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GI.close_button_ty()

    @allure.story("人员转制-（团队成员出单权赋予）-复核")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002(self):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(Test_YLDLZ_015.msg["user_code"]))
        self.ASR.query(Test_YLDLZ_015.msg["user_code"])
        self.ASR.select_data("出单权赋予复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        self.GIR.assertEqual("判断页面标题", self.GIR.get_head_text(), "出单权赋予复核")
        get_screenshot("复核")
        # 检查点
        info("复核")
        self.GIR.click(self.GIR.get_element_xpath(self.GIR.success))
        self.GIR.submit_interaction(self.GIR.submit_iframe, textarea="人员转制-（团队成员出单权赋予）-ui测试")
        text = self.GIR.get_text(self.GIR.get_element_xpath(self.GIR.save_success))
        self.GIR.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GIR.close_button_ty()

    @allure.story("人员转制-（团队成员出单权赋予）-验证人员状态")
    @pytest.mark.dependency(name='test_003', depends=['test_001', 'test_002'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_003(self):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码：{}，未提交状态".format(Test_YLDLZ_015.msg["user_code"]))
        self.MOAS.query(Test_YLDLZ_015.msg["user_code"])
        self.MOAS.assertEqual("判断该人员状态为‘有效’", self.MOAS.get_cell_text_by_head("状态", 0), "有效")
        get_screenshot("验证")

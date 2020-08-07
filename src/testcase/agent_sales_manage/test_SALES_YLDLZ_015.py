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
from src.utils.log import info


@allure.feature("团队成员出单权赋予与变更（人员转制-无效的合同制销售/合同制非销售转制为代理制人员)-（团队成员出单权赋予）")
class Test_YLDLZ_015():
    MOAS = ManagementOfAgentSalesmen()
    GI = GroupIssue()
    ASR = AgentSalesRecheck()
    GIR = GroupIssueRecheck()
    msg = None

    # data = csv_util.data_reader("agent_sales_manage/014_data.csv")

    data = [
        ("320122197911084429", "13999999999", "32019405--南京市分公司直属第一营业部中介业务部", "1131V3100000000000UK", "汉族", "本科", "群众")]
    data1 = [("资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2019-07-08", '2020-09-08',
              "RULE20120000000000001--保险经纪公司", "122222333529", "折", "中国工商银行股份有限公司",
              "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]

    @allure.story("人员转制-（团队成员出单权赋予）-基本信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("id_cards, mobile, group, group_code_hold, nation, culture, visage", data)
    def test_001(self, id_cards, mobile, group, nation, culture, visage, group_code_hold):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('团队成员出单权赋予与变更')
        # self.MOAS.open_url("http://10.10.1.104:8001/sales/deputy/updateDeputy.do?")
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
        self.GI.js_group(self.GI.group_code, self.GI.group_name, group, self.GI.group_code_hold, group_code_hold)
        # self.GI.select_org(self.GI.group_code, group)
        self.GI.send_keys(self.GI.get_element_xpath(self.GI.mobile), mobile)
        info("民族:{0}->政治面貌:{1}->学历:{2}".format(nation, visage, culture))
        self.GI.select_base(nation, visage, culture)

    @allure.story("人员转制-（团队成员出单权赋予）-资质信息、合同信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("qualifytype, qualifyno,"
                             "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
                             "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
                             "bankName", data1)
    def test_002(self, qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1, qualifyno1,
                 qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                 saDAccount_bankName, saDAccount_bankareaname, bankName):
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
        self.GI.js_group(self.GI.ruleNo, self.GI.saUContracts1, ruleNo)
        info("收款人账号:{0}->卡折标志:{1}->银行名称：{2}->银行区域名称：{3}->联行号：{4}".format(accountno, cardtype, saDAccount_bankName,
                                                                         saDAccount_bankareaname, bankName))
        self.GI.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName)
        info("切换到基本信息tab")
        self.GI.switch_user_tab()
        info("保存并提交")
        self.GI.save_deputy()
        sleep(3)
        self.GI.submit_interaction(self.GI.submit_iframe)
        # Test_YLDLZ_015.msg = self.GI.get_msg()
        # info("人员代码{0}，合同号{1}".format(Test_YLDLZ_015.msg['usercode'], Test_YLDLZ_015.msg['contract']))
        # # 关闭
        # self.GI.click(self.GI.wait_until_el_xpath(self.GI.submit_close))

    @allure.story("人员转制-（团队成员出单权赋予）-复核")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("id_cards, mobile, group, group_code_hold, nation, culture, visage", data)
    def test_003(self, id_cards, mobile, group, nation, culture, visage, group_code_hold):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(Test_YLDLZ_015.msg["user_code"]))
        self.ASR.query(Test_YLDLZ_015.msg["user_code"])
        # self.ASR.query(user_code1="32366511")
        self.ASR.select_data("出单权赋予复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        self.GIR.assertEqual("判断页面标题", self.GIR.get_head_text(), "出单权赋予复核")
        # 检查点
        info("复核")
        self.GIR.click(self.GIR.get_element_xpath(self.GIR.success))
        self.GIR.submit_interaction(self.GIR.submit_iframe, textarea="人员转制-（团队成员出单权赋予）-ui测试")

    @allure.story("人员转制-（团队成员出单权赋予）-验证人员状态")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_004(self):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("查询人员代码：{}，未提交状态".format(Test_YLDLZ_015.msg["user_code"]))
        self.MOAS.query(Test_YLDLZ_015.msg["user_code"])
        # info("查询人员代码：{}，未提交状态".format("32366511"))
        # self.MOAS.query("32366511")
        self.MOAS.assertEqual("判断该人员状态为‘有效’", self.MOAS.get_cell_text_by_head("状态", 0), "有效")

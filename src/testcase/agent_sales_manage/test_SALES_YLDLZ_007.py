#  -*- coding:utf-8 -*-
# @Time : 2020/7/27 10:39
# @Author: fyl
# @File : test_SALES_YLDLZ_007.py   代理制人员代码管理>>团队成员出单权赋予与变更（新增普通代理制成员）
import allure
import pytest

from config.global_var import sleep
from src.page.agent_sales_manage.group_issue import GroupIssue
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils.log import info


@allure.feature("代理制销售人员代码管理>>团队成员出单权赋予与变更（新增普通代理制成员）")
class Test_YLDLZ_007():
    main_page = ManagementOfAgentSalesmen()
    group_issue = GroupIssue()
    agent_sales_recheck = AgentSalesRecheck()
    msg = None

    data = [("甘冬龙ui测试", "370126198007046159", "13999999999", "32990000--测试0519营销", "汉族", "中共党员", "研究生")]
    data1 = [("资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2020-07-08", '2022-07-08',
              "RULE20120000000000001--保险经纪公司", "121222333529", "折", "中国工商银行股份有限公司",
              "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]


    @allure.story("填写基本信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("username, id_cards, mobile, group_com, nation, visage, culture", data)
    def test_01_base_msg(self, username, id_cards, mobile, group_com, nation, visage, culture):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.main_page.into_page()
        info("团队成员出单权赋予与变更")
        self.main_page.click_btn('团队成员出单权赋予与变更')
        self.main_page.switch_to_window()
        self.main_page.maximize_window()
        self.group_issue.assertEqual("验证标签文字", self.group_issue.get_head_text(), "团队成员出单权赋予")
        info("填入姓名:{0}->身份证号：{1}->手机号码：{2}".format(username, id_cards, mobile))
        self.group_issue.user_tab_input(username, id_cards, mobile)
        info("选择上级机构:32000000--中国人民财产保险股份有限公司江苏省分公司，归属机构:{0}".format(group_com))
        self.group_issue.select_org("32000000--中国人民财产保险股份有限公司江苏省分公司", group_com)
        info("民族:{0}->政治面貌:{1}->学历:{2}".format(nation, visage, culture))
        self.group_issue.select_base(nation, visage, culture)

    @allure.story("填写资质信息、合同信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("qualifytype, qualifyno,"
                             "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
                             "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
                             "bankName", data1)
    def test_02_contract_msg(self, qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1, qualifyno1,
                             qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                             saDAccount_bankName, saDAccount_bankareaname, bankName):
        info("切换到合同信息tab")
        self.group_issue.switch_contract_tab()
        self.group_issue.add_user_button()
        self.group_issue.add_user_button()

        info("证件类型:{0}->证件号码：{1}->发证日期：{2}->证件类型：{3}".format(qualifytype, qualifyno, qualifystartdate, agentType))
        self.group_issue.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        info("证件类型:{0}->证件号码：{1}->发证日期：{2}".format(qualifytype1, qualifyno1, qualifystartdate1))
        self.group_issue.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("资格证号码:{0}->执业证号码：{1}->合同起始日期：{2}->合同终止日期：{3}->佣金配置：{4}".format(qualifyno, qualifyno1, contractstartdate0,
                                                                             contractenddate0, ruleNo))
        self.group_issue.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0, ruleNo)
        info("收款人账号:{0}->卡折标志:{1}->银行名称：{2}->银行区域名称：{3}->联行号：{4}".format(accountno, cardtype, saDAccount_bankName,
                                                                         saDAccount_bankareaname, bankName))
        self.group_issue.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName)
        info("切换到基本信息tab")
        self.group_issue.switch_user_tab()
        info("保存")
        self.group_issue.prepare_add_deputy()
        self.group_issue.choose_ok_on_alert()
        sleep(3)
        Test_YLDLZ_007.msg = self.group_issue.get_msg()
        info("人员代码{0}，合同号{1}".format(Test_YLDLZ_007.msg['usercode'], Test_YLDLZ_007.msg['contract']))
        # 关闭
        self.group_issue.click(self.group_issue.wait_until_el_xpath(self.group_issue.save_close))

    @allure.story("团队成员信息修改")
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_03_edit_msg(self):
        # 切换主页面
        self.main_page.switch_to_window()
        self.main_page.back_to_page()
        # 输入条件usercode查询
        self.main_page.query(Test_YLDLZ_007.msg['usercode'])
        # 选择查询后的数据点击‘团队成员出单权赋予与变更’
        status_list = self.main_page.get_cell_text_by_head('状态')
        index = status_list.index('出单权赋予')
        self.main_page.click(self.main_page.get_radio_by_head(index, '选择'))
        self.main_page.click_btn('团队成员出单权赋予与变更')
        self.group_issue.switch_to_window()
        self.group_issue.maximize_window()
        # 保存并提交
        self.group_issue.click(self.group_issue.wait_until_el_xpath(self.group_issue.save_commit))
        # 进入流程流转页面
        self.group_issue.submit_interaction(iframe_xpath=self.group_issue.submit_iframe)
        # 关闭
        self.group_issue.click(self.group_issue.wait_until_el_xpath(self.group_issue.submit_close))

    @allure.story("省级销售管理综合岗复核流程")
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_04_issue_recheck(self):
        self.agent_sales_recheck.switch_to_window()
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.agent_sales_recheck.into_page()
        info("查询人员代码{}".format(Test_YLDLZ_007.msg['usercode']))
        self.agent_sales_recheck.query(Test_YLDLZ_007.msg['usercode'])
        # 选择指定状态的数据进入复核页面
        self.agent_sales_recheck.select_data("出单权赋予复核")
        self.agent_sales_recheck.switch_to_window()
        self.agent_sales_recheck.maximize_window()
        # 复核信息检查
        info("复核")
        self.agent_sales_recheck.recheck_ope(textarea="ui测试")
        # 关闭
        self.agent_sales_recheck.click(
            self.agent_sales_recheck.wait_until_el_xpath(self.agent_sales_recheck.submit_close))

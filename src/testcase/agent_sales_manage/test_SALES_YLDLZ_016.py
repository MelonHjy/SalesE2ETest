#  -*- coding:utf-8 -*-
# @Time : 2020/8/6 14:37
# @Author: fyl
# @File : test_SALES_YLDLZ_016.py   代理制销售人员代码管理>>营销团队经理聘任与解聘(人员转制-无效的合同制销售/合同制非销售转制为代理制人员)-(经理聘任）
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


@allure.feature("营销团队经理聘任与解聘(人员转制-无效的合同制销售/合同制非销售转制为代理制人员)-(经理聘任）")
class Test_YLDLZ_016():
    MOAS = ManagementOfAgentSalesmen()
    AM = AppointmentManager()
    ASR = AgentSalesRecheck()
    AMR = AppointmentManagerRecheck()
    SQ = SalesQuery()
    msg = None

    # data = [("320102195201282450", "13999999999", "32019937--ces团队0319", "1131B81000000002I5DD", "汉族", "本科", "群众","经理")]
    # data1 = [("资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2019-07-08", '2020-09-08',
    #           "RULE20120000000000001--保险经纪公司", "123222333529", "折", "中国工商银行股份有限公司",
    #           "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]

    data = csv_util.data_reader("agent_sales_manage/test_SALES_YLDLZ_016.csv")
    # data1 = csv_util.data_reader("agent_sales_manage/015_data1.csv")

    @allure.story("人员转制-（营销团队经理聘任与解聘）")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize("id_cards,com_group,group,qualifytype, qualifyno,"
                             "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
                             "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
                             "bankName", data)
    def test_001(self, id_cards,com_group,group,qualifytype, qualifyno, qualifystartdate, agentType, qualifytype1, qualifyno1,
                 qualifystartdate1, contractstartdate0, contractenddate0, ruleNo, accountno, cardtype,
                 saDAccount_bankName, saDAccount_bankareaname, bankName):
        info("经营机构->销售人员->代理制销售人员代码管理")
        self.MOAS.into_page()
        info("团队成员出单权赋予与变更")
        self.MOAS.click_btn('营销团队经理聘任与解聘')
        self.AM.assertEqual("判断页面标题", self.AM.get_head_text(), "营销团队经理聘任")
        info("填入身份证号：{}".format(id_cards))
        self.AM.send_keys(self.AM.get_element_xpath(self.AM.id_cards), id_cards)
        self.AM.switch_user_tab()
        info("提示框信息：{}".format(self.AM.get_alert_text()))
        self.AM.choose_ok_on_alert()
        sleep(2)
        user_code = self.AM.get_attribute(self.AM.wait_until_el_xpath(self.AM.user_code), 'value')
        info("人员代码：{}".format(user_code))
        Test_YLDLZ_016.msg = {"user_code": user_code}
        info("选择归属机构:{0}".format(group))
        # self.AM.js_group(self.AM.group_code, self.AM.group_name, group, self.AM.group_code_hold, group_code_hold)
        self.AM.select_org(self.AM.com_code, com_group)
        self.AM.select_org(self.AM.group_code, group)
        self.AM.select_rolecode("经理")
        get_screenshot("基本信息")
        info("切换到合同信息tab")
        self.AM.switch_contract_tab()
        self.AM.add_user_button()
        self.AM.add_user_button()
        info("证件类型:{0}->证件号码：{1}->发证日期：{2}->证件类型：{3}".format(qualifytype, qualifyno, qualifystartdate, agentType))
        self.AM.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        info("证件类型:{0}->证件号码：{1}->发证日期：{2}".format(qualifytype1, qualifyno1, qualifystartdate1))
        self.AM.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("资格证号码:{0}->执业证号码：{1}->合同起始日期：{2}->合同终止日期：{3}->佣金配置：{4}".format(qualifyno, qualifyno1, contractstartdate0,
                                                                             contractenddate0, ruleNo))
        self.AM.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0, ruleNo)
        self.AM.js_group(self.AM.ruleNo, self.AM.saUContracts1.format('0'), ruleNo)
        info("收款人账号:{0}->卡折标志:{1}->银行名称：{2}->银行区域名称：{3}->联行号：{4}".format(accountno, cardtype, saDAccount_bankName,
                                                                         saDAccount_bankareaname, bankName))
        self.AM.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname, bankName)
        get_screenshot("合同信息")
        info("切换到基本信息tab")
        self.AM.switch_user_tab()
        info("保存并提交")
        self.AM.prepare_save_commit()
        sleep(3)
        self.AM.submit_interaction(self.AM.submit_iframe)
        text = self.AM.get_text(self.AM.get_element_xpath(self.AM.save_success))
        self.AM.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.AM.close_button_ty()

    @allure.story("人员转制-（营销团队经理聘任与解聘）--复核")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_003(self):
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.ASR.into_page()
        info("查询人员代码{}->选择".format(Test_YLDLZ_016.msg["user_code"]))
        self.ASR.query(Test_YLDLZ_016.msg["user_code"])
        self.ASR.select_data("经理聘任复核")
        self.ASR.switch_to_window()
        self.ASR.maximize_window()
        self.AMR.assertEqual("判断页面标题", self.AMR.get_head_text(), "经理聘任复核")
        get_screenshot("复核")
        # 检查点
        info("复核")
        self.AMR.click(self.AMR.get_element_xpath(self.AMR.success))
        self.AMR.submit_interaction(self.AMR.submit_iframe, textarea="人员转制-（营销团队经理聘任与解聘）-ui测试")
        text = self.AMR.get_text(self.AMR.get_element_xpath(self.AMR.save_success))
        self.AMR.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("提交")
        self.AMR.close_button_ty()

    @allure.story("人员转制-（营销团队经理聘任与解聘）--验证人员状态")
    @pytest.mark.dependency(name='test_003', depends=['test_001', 'test_002'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_004(self):
        info("个代渠道->销售人员->销售人员查询")
        self.SQ.into_page()
        info("查询人员代码：{}，未提交状态".format(Test_YLDLZ_016.msg["user_code"]))
        self.SQ.query(Test_YLDLZ_016.msg["user_code"])
        text = self.SQ.get_cell_text_by_head("职级", row=0)
        self.SQ.assertEqual("判断该销售人员职级是否营销团队经理", text, "营销团队经理")
        get_screenshot("验证")
# -*- coding:utf-8 -*-
# @Time : 2020/6/28 17:22
# @Author: fyl
# @File : test_SALES_YLDLZ_001.py
import allure
import pytest

from src.page.agent_sales_manage.appointment_manager import AppointmentManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.page.integrated_management.main_agent_sales_recheck import AgentSalesRecheck
from src.utils.driver_util import *
from src.utils.except_util import get_screenshot


@allure.feature("经理聘任主流程")
class Test_YLDLZ_001():
    appointment_and_dismissal = AppointmentManager()
    main_management_agent_salesmen = ManagementOfAgentSalesmen()
    agent_sales_recheck = AgentSalesRecheck()
    # try:
    #     sql = "select * from SaUUser"
    #     data = g.db.select(sql)
    #     data = g.db.random_choice(data, 3)
    #     for d in data:
    #         print(d)
    # finally:
    #     g.db.close_connection()

    data = [("袁维卫ui测试", "110102199608211442", "13311212125", "32990038--测试0506营销", "经理", "汉族", "中共党员", "研究生")]

    data1 = [("资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2020-07-08", '2022-07-08',
              "RULE20120000000000001--保险经纪公司", "1199211192249", "折", "中国工商银行股份有限公司",
              "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]

    data2 = [("袁维卫ui测试", "110102199608211442", "32000000", "测试0506营销")]
    msg = {'usercode': '83258573'}

    # @pytest.mark.skip
    @allure.story("填写基本信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("userName, idCard, mobile, group, rolecode, nation, visage, culture", data)
    def test_001_basemag(self, userName, idCard, mobile, group, rolecode, nation, visage, culture):
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.main_management_agent_salesmen.into_page()
        self.main_management_agent_salesmen.appointment()
        info("营销团队经理聘任与解聘检查")
        self.appointment_and_dismissal.assertEqual("验证标签文字", self.appointment_and_dismissal.get_head_text(), "营销团队经理聘任")
        self.appointment_and_dismissal.assertEqual("验证上级机构是否默认‘32000000’",
                                                   self.appointment_and_dismissal.get_com_code_text(), "32000000")
        info("填入基本信息")
        self.appointment_and_dismissal.user_tab_input(userName, idCard, mobile)
        self.appointment_and_dismissal.select_group(group)
        self.appointment_and_dismissal.select_rolecode(rolecode)
        self.appointment_and_dismissal.select_nation(nation)
        self.appointment_and_dismissal.select_visage(visage)
        self.appointment_and_dismissal.select_culture(culture)

        info("检查填写身份证号码后，性别和出生日期是否自动填入")
        self.appointment_and_dismissal.get_sex(self.appointment_and_dismissal.get_sex_by_idCard(idCard))
        self.appointment_and_dismissal.assertEqual("验证出生日期是否与身份证匹配", self.appointment_and_dismissal.get_birthday(),
                                                   self.appointment_and_dismissal.get_birthday_by_idCard(idCard))
        info("检查选择归属团队后，出单归属机构是否自动填入")
        self.appointment_and_dismissal.assertEqual("验证出单归属机构是否与所选归属团队匹配",
                                                   self.appointment_and_dismissal.get_make_com_text(),
                                                   group.split('--')[0])
        get_screenshot("基本信息")

    @allure.story("填写资质信息、合同信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("qualifytype, qualifyno,"
                             "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
                             "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
                             "bankName", data1)
    def test_002_contract(self, qualifytype, qualifyno,
                                qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1,
                                contractstartdate0,
                                contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName,
                                saDAccount_bankareaname,
                                bankName):
        self.appointment_and_dismissal.switch_contract_tab()
        self.appointment_and_dismissal.add_user_button()
        self.appointment_and_dismissal.add_user_button()
        info("填写'资格证'资质信息-->证件类型,证件号码,发证日期,证件类型")
        self.appointment_and_dismissal.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        info("填写'执业证'资质信息-->证件类型,证件号码,发证日期")
        self.appointment_and_dismissal.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("填写合同基本信息（资格证号码,执业证号码,合同起始日期,合同终止日期,佣金配置）")
        self.appointment_and_dismissal.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0,
                                                      ruleNo)
        info("填写账户信息（收款人账号,卡折标志,银行名称,银行区域名称,联行号）")
        self.appointment_and_dismissal.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,
                                                     bankName)
        get_screenshot("合同信息")
        self.appointment_and_dismissal.switch_user_tab()
        info("聘任保存")
        self.appointment_and_dismissal.prepare_save()
        self.appointment_and_dismissal.choose_ok_on_alert()
        sleep(3)
        info("获取人员代码，合同号")
        Test_YLDLZ_001.msg = self.appointment_and_dismissal.get_msg()
        info(Test_YLDLZ_001.msg)
        get_screenshot("聘任保存")
        self.appointment_and_dismissal.close_btn()

    @allure.story("查询未提交中是否存在该数据，聘任保存并提交")
    @pytest.mark.parametrize("name, id_cards, sjjg, group", data2)
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_003_commit(self, name, id_cards, sjjg, group):
        self.main_management_agent_salesmen.into_page()
        self.main_management_agent_salesmen.query(Test_YLDLZ_001.msg['usercode'])
        self.main_management_agent_salesmen.set_table_num(0)
        sleep(2)  # 等待数据返回
        self.main_management_agent_salesmen.assert_table_msg(Test_YLDLZ_001.msg['usercode'], name, id_cards, sjjg,
                                                             group)
        self.main_management_agent_salesmen.click(self.main_management_agent_salesmen.get_radio_by_head(0, '选择'))
        self.main_management_agent_salesmen.appointment()
        self.appointment_and_dismissal.prepare_save_commit()
        self.agent_sales_recheck.submit()
        sleep(3)
        self.agent_sales_recheck.close_button_ty()

    @allure.story("查询已提交中是否存在该数据，流程查看岗位信息")
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_004_assert(self):
        # 切换到‘代理制销售人员代码管理’页面
        self.main_management_agent_salesmen.into_page()
        self.main_management_agent_salesmen.query(Test_YLDLZ_001.msg['usercode'], 1)
        self.main_management_agent_salesmen.set_table_num(1)
        self.main_management_agent_salesmen.click(self.main_management_agent_salesmen.get_radio_by_head(0, '流程查询'))
        # 切换到‘工作流列表’页面
        self.main_management_agent_salesmen.switch_to_window()
        self.main_management_agent_salesmen.set_table_num(0)
        self.main_management_agent_salesmen.assert_workflow_msg()
        g.driver.close()

    @allure.story("地市级销售管理综合岗复核")
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_005_recheck(self):
        self.main_management_agent_salesmen.switch_to_window()
        info("综合管理->销售人员->代理制销售人员代码复核")
        self.agent_sales_recheck.into_page()
        info("查询人员代码{}".format(Test_YLDLZ_001.msg['usercode']))
        self.agent_sales_recheck.query(Test_YLDLZ_001.msg['usercode'])
        info("进入操作界面")
        status_list = self.agent_sales_recheck.get_cell_text_by_head('审核状态')
        index = status_list.index("经理聘任复核")
        self.agent_sales_recheck.click(self.agent_sales_recheck.get_a_by_head(index, '操作'))
        self.agent_sales_recheck.switch_to_window()
        self.agent_sales_recheck.maximize_window()
        info("检查信息点")
        info("复核")
        self.agent_sales_recheck.click_success()
        self.agent_sales_recheck.submit(textarea="ui自动化测试")
        sleep(3)
        self.agent_sales_recheck.close_button_ty()

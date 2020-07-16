# -*- coding:utf-8 -*-
# @Time : 2020/7/14 15:46
# @Author: fyl
# @File : test_SALES_validate.py    输入信息验证
import allure
import pytest

from config.global_var import sleep
from src.page.agent_sales_manage.appointment_and_dismissal import AppointmentAndDismissal
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("经理聘任流程的信息验证")
class Test_not_empty():
    appointment_and_dismissal = AppointmentAndDismissal()
    main_management_agent_salesmen = ManagementOfAgentSalesmen()

    data = [("苏嘉秀iu测试", "410101199602194981", "13313313313", "32990038--测试0506营销", "经理", "汉族", "中共党员", "研究生", "资格证",
             "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", '2020-05-05', '2020-12-07',
             "RULE20120000000000001--保险经纪公司", "111222333445", "折", "中国工商银行股份有限公司", "新疆维吾尔自治区_巴音郭楞蒙古自治州",
             "中国工商银行股份有限公司库尔勒人民东路支行")]
    data1 = [['2019-05-05', '2017-03-02', False], ['2020-10-05', '2020-10-04', False],
             ['2020-10-05', '2020-10-05', True], ['2020-10-05', '2020-10-06', True],
             ['2019-05-05', '2020-03-02', False], ['2020-05-05', '2020-12-07', True]]
    # 资格证、执业证日期(合同起始日期)
    data2 = [['2020-07-03', '2020-07-03', False], ['2020-07-03', '2020-02-03', False],
             ['2020-04-03', '2020-07-03', False],
             ['2020-05-05', '2020-02-03', True], ['2020-02-03', '2020-05-05', True], ['2020-05-03', '2020-05-03', True]]
    data3 = [['2020-01-01', '2019-02-02', False], ['2020-01-01', '2020-01-01', True], ['2019-02-02', '2020-01-01', True]]

    @allure.story("验证前基本信息填入")
    @pytest.mark.vervify
    @pytest.mark.dependency(name="one")
    @pytest.mark.usefixtures("login_jiangsu_p_v")
    @pytest.mark.parametrize(
        "userName, idCard, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,"
        "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
        "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
        "bankName", data)
    def test_YLDLZ_001_basemag(self, userName, idCard, mobile, group, rolecode, nation,
                               visage, culture, qualifytype, qualifyno,
                               qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1,
                               contractstartdate0,
                               contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName,
                               saDAccount_bankareaname,
                               bankName):
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.main_management_agent_salesmen.into_page()
        info("填入基本信息")
        self.appointment_and_dismissal.user_tab_input(userName, idCard, mobile)
        self.appointment_and_dismissal.select_group(group)
        self.appointment_and_dismissal.select_rolecode(rolecode)
        self.appointment_and_dismissal.select_nation(nation)
        self.appointment_and_dismissal.select_visage(visage)
        self.appointment_and_dismissal.select_culture(culture)
        get_screenshot("基本信息")
        self.appointment_and_dismissal.switch_contract_tab()
        self.appointment_and_dismissal.add_user_button()
        self.appointment_and_dismissal.add_user_button()
        info("填写'资格证'资质信息-->证件类型,证件号码,发证日期,证件类型")
        self.appointment_and_dismissal.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        info("填写'执业证'资质信息-->证件类型,证件号码,发证日期")
        self.appointment_and_dismissal.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        info("填写合同基本信息（资格证号码,执业证号码,合同起始日期,合同终止日期,佣金配置）")
        self.appointment_and_dismissal.input_contract(qualifyno, qualifyno1, contractstartdate0,
                                                      contractenddate0, ruleNo)
        info("填写账户信息（收款人账号,卡折标志,银行名称,银行区域名称,联行号）")
        self.appointment_and_dismissal.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,
                                                     bankName)
        get_screenshot("合同信息")

    @allure.story("验证合同起始、终止日期")
    @allure.description("合同终止日期不能小于起始日期、合同终止日期不能小于今天")
    @pytest.mark.vervify
    @pytest.mark.dependency(dency="one")
    @pytest.mark.usefixtures("login_jiangsu_p_v")
    @pytest.mark.parametrize("start_date, end_date, expect", data1)
    def test_contract_date(self, start_date, end_date, expect):
        self.appointment_and_dismissal.input_contract_date(start_date, end_date)
        self.appointment_and_dismissal.switch_user_tab()
        self.appointment_and_dismissal.prepare_save_commit()
        if expect:
            self.appointment_and_dismissal.close_submit()
        else:
            self.appointment_and_dismissal.choose_ok_on_alert()
        self.appointment_and_dismissal.switch_contract_tab()
        text = self.appointment_and_dismissal.get_title_att(self.appointment_and_dismissal.contractenddate0)
        info(text)
        get_screenshot("合同日期检验")
        self.appointment_and_dismissal.assertEqual("检查合同起始与终止日期是否符合要求", text == "", expect)

    @allure.story("验证合同起始日期跟证书关系")
    @allure.description("合同起始日期不能小于代理资格证、执业证发证日期")
    @pytest.mark.vervify
    @pytest.mark.dependency(dency="one")
    @pytest.mark.usefixtures("login_jiangsu_p_v")
    @pytest.mark.parametrize("qualifystartdate0, qualifystartdate1, expect", data2)
    def test_contract_date(self, qualifystartdate0, qualifystartdate1, expect):
        self.appointment_and_dismissal.input_qualify_date(qualifystartdate0, qualifystartdate1)
        self.appointment_and_dismissal.switch_user_tab()
        self.appointment_and_dismissal.prepare_save_commit()
        if expect:
            self.appointment_and_dismissal.close_submit()
        else:
            self.appointment_and_dismissal.choose_ok_on_alert()
        self.appointment_and_dismissal.switch_contract_tab()
        text = self.appointment_and_dismissal.get_title_att(self.appointment_and_dismissal.contractstartdate0)
        info(text)
        self.appointment_and_dismissal.assertEqual("检查合同起始日期与证书日期关系是否符合要求", text == "", expect)


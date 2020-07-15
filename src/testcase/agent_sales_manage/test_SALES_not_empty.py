# -*- coding:utf-8 -*-
# @Time : 2020/7/14 15:46
# @Author: fyl
# @File : test_SALES_not_empty.py    输入信息非空验证
import pytest

from config.global_var import g, sleep
from src.page.agent_sales_manage.appointment_and_dismissal import AppointmentAndDismissal
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.testcase.agent_sales_manage.test_validate_date import Test_Validate
from src.utils.except_util import get_screenshot
from src.utils.log import info


class Test_not_empty():
    appointment_and_dismissal = AppointmentAndDismissal()
    main_management_agent_salesmen = ManagementOfAgentSalesmen()

    data = [("苏嘉秀iu测试", "410101199602194981", "13313313313", "32990038--测试0506营销", "经理", "汉族", "中共党员", "研究生", "资格证",
             "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2020-07-08", '2022-07-08',
             "RULE20120000000000001--保险经纪公司", "111222333445", "折", "中国工商银行股份有限公司", "新疆维吾尔自治区_巴音郭楞蒙古自治州",
             "中国工商银行股份有限公司库尔勒人民东路支行")]

    date = [['2019-05-05', '2017-03-02', 'False'], ['2019-05-05', '2019-05-04', 'False'],
            ['2019-05-05', '2019-05-05', 'True'], ['2019-05-05', '2019-05-06', 'True'],
            ['2019-05-05', '2020-02-07', 'True']]

    @pytest.mark.dependency(name="one")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("start_date, end_date, expect", date)
    @pytest.mark.parametrize(
        "userName, idCard, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,"
        "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
        "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
        "bankName", data)
    def test_YLDLZ_001_basemag(self, start_date, end_date, expect, userName, idCard, mobile, group, rolecode, nation,
                               visage, culture, qualifytype, qualifyno,
                               qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1,
                               contractstartdate0,
                               contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName,
                               saDAccount_bankareaname,
                               bankName):
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.main_management_agent_salesmen.into_page()
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
        Test_Validate().test_contract_date(start_date, end_date, expect)

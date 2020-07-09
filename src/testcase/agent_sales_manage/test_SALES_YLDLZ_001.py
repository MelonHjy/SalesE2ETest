# -*- coding:utf-8 -*-
# @Time : 2020/6/28 17:22
# @Author: fyl
# @File : test_SALES_YLDLZ_001.py
import pytest

from src.page.agent_sales_manage.appointment_and_dismissal import AppointmentAndDismissal
from src.utils.driver_util import *


class Test_YLDLZ_001():
    appointment_and_dismissal = AppointmentAndDismissal()
    # try:
    #     sql = "select * from SaUUser"
    #     data = g.db.select(sql)
    #     data = g.db.random_choice(data, 3)
    #     for d in data:
    #         print(d)
    # finally:
    #     g.db.close_connection()

    data = [("尉迟茗潮", "530421198904150153", "13313313313", "87654321--test111", "经理", "汉族", "中共党员", "研究生",
             "资格证", "123456", "2019-01-01", "B", "执业证", "654321", "2019-02-02", "2020-07-08", '2022-07-08',
             "RULE20120000000000001--保险经纪公司", "111222333444", "折", "中国工商银行股份有限公司",
             "新疆维吾尔自治区_巴音郭楞蒙古自治州", "中国工商银行股份有限公司库尔勒人民东路支行")]

    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize(
        "userName, idCard, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,"
        "qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,"
        "contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,"
        "bankName", data)
    def test_YLDLZ_001(self, userName, idCard, mobile, group, rolecode, nation, visage, culture, qualifytype, qualifyno,
                       qualifystartdate, agentType, qualifytype1, qualifyno1, qualifystartdate1, contractstartdate0,
                       contractenddate0, ruleNo, accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,
                       bankName):
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.appointment_and_dismissal.into_page()
        info("营销团队经理聘任与解聘检查")
        self.appointment_and_dismissal.assertEqual("验证标签文字", self.appointment_and_dismissal.get_head_text(), "营销团队经理聘任")
        self.appointment_and_dismissal.assertEqual("验证上级机构是否默认‘32000000’",
                                                   self.appointment_and_dismissal.get_com_code_text(), "32000000")
        info("填入信息")
        self.appointment_and_dismissal.user_tab_input(userName, idCard, mobile)
        self.appointment_and_dismissal.select_group(group)
        self.appointment_and_dismissal.select_rolecode(rolecode)
        self.appointment_and_dismissal.select_nation(nation)
        self.appointment_and_dismissal.select_visage(visage)
        self.appointment_and_dismissal.select_culture(culture)

        info("检查填写身份证号码后，性别和出生日期是否自动填入")
        self.appointment_and_dismissal.assertEqual("验证性别是否与身份证匹配", self.appointment_and_dismissal.get_sex(),
                                                   self.appointment_and_dismissal.get_sex_by_idCard(idCard))
        self.appointment_and_dismissal.assertEqual("验证出生日期是否与身份证匹配", self.appointment_and_dismissal.get_birthday(),
                                                   self.appointment_and_dismissal.get_birthday_by_idCard(idCard))
        info("检查选择归属团队后，出单归属机构是否自动填入")
        self.appointment_and_dismissal.assertEqual("验证出单归属机构是否与所选归属团队匹配",
                                                   self.appointment_and_dismissal.get_make_com_text(),
                                                   group.split('--')[0])

        self.appointment_and_dismissal.switch_contract_tab()
        self.appointment_and_dismissal.add_user_button()
        self.appointment_and_dismissal.add_user_button()
        self.appointment_and_dismissal.input_qualify(0, qualifytype, qualifyno, qualifystartdate, agentType)
        self.appointment_and_dismissal.input_qualify(1, qualifytype1, qualifyno1, qualifystartdate1)
        self.appointment_and_dismissal.input_contract(qualifyno, qualifyno1, contractstartdate0, contractenddate0,
                                                      ruleNo)
        self.appointment_and_dismissal.input_account(accountno, cardtype, saDAccount_bankName, saDAccount_bankareaname,
                                                     bankName)
        self.appointment_and_dismissal.switch_user_tab()
        info("聘任保存")
        self.appointment_and_dismissal.prepare_save()

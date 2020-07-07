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

    data = [("尉迟茗潮", "530421198904150153", "13313313313", "87654321--test111", "经理", "汉族", "中共党员", "研究生")]

    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("userName, idCard, mobile, group, rolecode, nation, visage, culture", data)
    def test_YLDLZ_001(self, userName, idCard, mobile, group, rolecode, nation, visage, culture):
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        self.appointment_and_dismissal.into_page()
        info("营销团队经理聘任与解聘检查")
        self.appointment_and_dismissal.assertEqual("验证标签文字", self.appointment_and_dismissal.get_head_text(), "营销团队经理聘任")
        self.appointment_and_dismissal.assertEqual("验证上级机构是否默认‘32000000’",
                                                   self.appointment_and_dismissal.get_com_code_text(), "32000000")
        info("填入信息")
        self.appointment_and_dismissal.input(userName, idCard, mobile)
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
        self.appointment_and_dismissal.assertEqual("验证出单归属机构是否与所选归属团队匹配", self.appointment_and_dismissal.get_make_com_text(),
                                                   group.split('--')[0])
        info("聘任保存")
        self.appointment_and_dismissal.prepare_save()

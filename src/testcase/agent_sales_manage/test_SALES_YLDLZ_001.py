# -*- coding:utf-8 -*-
#@Time : 2020/6/28 17:22
#@Author: fyl
#@File : test_SALES_YLDLZ_001.py
import pytest

from src.page.agent_sales_manage.appointment_and_dismissal import AppointmentAndDismissal
from src.utils.driver_util import *


class Test_YLDLZ_001():

    # try:
    #     sql = "select * from SaUUser"
    #     data = g.db.select(sql)
    #     data = g.db.random_choice(data, 3)
    #     for d in data:
    #         print(d)
    # finally:
    #     g.db.close_connection()

    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_YLDLZ_001(self):
        info("经营机构->销售人员->代理制销售人员代码管理->营销团队经理聘任与解聘")
        AppointmentAndDismissal().into_page()
        info("营销团队经理聘任与解聘检查")

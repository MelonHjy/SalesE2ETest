#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 20:29
# @Author: fyl
# @File : test_SALES_YLZJ_008.py    中介模块>>渠道类型码查询
import allure
import pytest

from config.global_var import sleep
from src.page.agency_module.main_channel_type_code_query import MainChannelTypeCodeQuery
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("中介模块>>渠道类型码查询-008")
class Test_SALES_YLZJ_008():
    MCTCQ = MainChannelTypeCodeQuery()

    data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_008.csv")

    @allure.story("渠道类型码查询")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("channel", data)
    def test_001(self, channel):
        self.MCTCQ.switch_to_default_content()
        info("渠道类型码查询页")
        self.MCTCQ.into_page(channel)
        self.MCTCQ.assertEqual("验证页面标题", self.MCTCQ.get_head_text(), "渠道类型码查询")
        info("查询")
        self.MCTCQ.click_btn("查询")
        text = self.MCTCQ.get_text(self.MCTCQ.get_element_xpath(self.MCTCQ.query_data))
        info(text)
        flag = self.MCTCQ.table_cell_text("操作", "查看")
        self.MCTCQ.assertResult("判断查询数据是无记录或者有记录列表", text in "无记录." or flag)
        get_screenshot("渠道类型码查询-{}".format(channel))
        sleep(2)

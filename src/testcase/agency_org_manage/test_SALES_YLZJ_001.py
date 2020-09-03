#  -*- coding:utf-8 -*-
# @Time : 2020/8/19 16:44
# @Author: fyl
# @File : test_SALES_YLZJ_001.py    中介机构>>中介机构新增和变更申报>>查询
import allure
import pytest

from config.global_var import sleep
from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("中介机构>>中介机构新增和变更申报>>查询-001")
class Test_SALES_YLZJ_001():
    MAOM = MainAgencyOrgManage()
    data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_001.csv")

    @allure.story("查询")
    @pytest.mark.usefixtures("login_jiangsu_c")
    @pytest.mark.parametrize("channel,contractType,apartment_type", data)
    def test_001(self, channel, contractType, apartment_type):
        self.MAOM.switch_to_default_content()
        info("中介机构新增和变更申报页:{}".format(channel))
        self.MAOM.into_page(channel)
        self.MAOM.assertEqual("验证页面标题", self.MAOM.get_head_text(), "中介机构新增和变更申报")
        info("查询")
        self.MAOM.query(contractType=contractType)
        alert = self.MAOM.get_alert_text()
        self.MAOM.assertEqual("判断不选部门类型查询时提示信息", alert, "请选择部门类型")
        get_screenshot("中介机构{}查询提示".format(channel))
        self.MAOM.choose_ok_on_alert()
        self.MAOM.query(contractType=contractType, apartment_type=apartment_type)
        text = self.MAOM.get_text(self.MAOM.get_element_xpath(self.MAOM.query_data))
        info(text)
        flag = self.MAOM.table_cell_text("合同类型", contractType)
        self.MAOM.assertResult("判断查询数据是无记录或者有记录列表", text in "无记录." or flag)
        get_screenshot("中介机构{}查询结果".format(channel))
        sleep(2)

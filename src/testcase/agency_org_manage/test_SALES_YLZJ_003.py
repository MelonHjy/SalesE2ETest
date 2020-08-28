#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 9:48
# @Author: fyl
# @File : test_SALES_YLZJ_003.py    中介机构>>中介机构新增和变更申报>>重置
import allure
import pytest

from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("中介机构>>中介机构新增和变更申报>>重置")
class Test_SALES_YLZJ_003():
    MAOM = MainAgencyOrgManage()
    data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_003.csv")

    @allure.story("查询")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("channel,contractType,contract_no", data)
    def test_001(self, channel, contractType, contract_no):
        info("中介机构新增和变更申报页:{}".format(channel))
        self.MAOM.into_page(channel)
        self.MAOM.assertEqual("验证页面标题", self.MAOM.get_head_text(), "中介机构新增和变更申报")
        info("查询")
        self.MAOM.query(contract_no, contractType, "1")
        info("重置")
        self.MAOM.click_btn("重置")
        self.MAOM.assertEqual("验证合同号输入框被清空",
                              self.MAOM.get_attribute(self.MAOM.get_element_xpath(self.MAOM.contract_no), "value"), "")
        flag = (not self.MAOM.is_selected("0")) or (not self.MAOM.is_selected("1")) or (not self.MAOM.is_selected("3"))
        self.MAOM.assertResult("验证任务状态清空", flag)
        get_screenshot("中介机构{}查询重置".format(channel))
        self.MAOM.switch_to_default_content()
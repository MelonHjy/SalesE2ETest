#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 13:42
# @Author: fyl
# @File : test_SALES_YLZJ_007.py    中介机构>>中介机构查询
import allure
import pytest

from config.global_var import sleep
from src.page.agency_module.main_agency_org_query import MainAgencyOrgQuery
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("中介机构>>中介机构查询-007")
class Test_SALES_YLZJ_007:
    MAOQ = MainAgencyOrgQuery()

    data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_007.csv")

    @allure.story("中介机构查询")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.parametrize("channel,contract_no", data)
    def test_001(self, channel, contract_no):
        self.MAOQ.switch_to_default_content()
        info("中介机构查询页：{}".format(channel))
        self.MAOQ.into_page(channel)
        self.MAOQ.assertEqual("验证页面标题", self.MAOQ.get_head_text(), "中介机构查询")
        info("输入合同号")
        self.MAOQ.send_keys(self.MAOQ.wait_until_el_xpath(self.MAOQ.contract_no), contract_no)
        info("查询")
        self.MAOQ.click(self.MAOQ.get_element_xpath(self.MAOQ.query_btn))
        sleep(3)
        info("验证")
        text = self.MAOM.get_text(self.MAOM.get_element_xpath(self.MAOM.query_data))
        if text.strip() == "无记录.":
            self.MAOQ.assertResult("判断查询数据是否有数据", "加载中" in text.strip())
        else:
            self.MAOQ.assertEqual("验证查询到的数据合同号是否一致", self.MAOQ.get_cell_text_by_head("合同编号", 0), contract_no)

        get_screenshot("中介机构{}查询".format(channel))
        sleep(2)

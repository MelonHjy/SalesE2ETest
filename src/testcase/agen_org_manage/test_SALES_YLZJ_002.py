#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 9:48
# @Author: fyl
# @File : test_SALES_YLZJ_002.py    中介机构>>中介机构新增和变更申报>>重置
import allure
import pytest

from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils.log import info


@allure.feature("中介机构>>中介机构新增和变更申报>>重置")
class Test_SALES_YLZJ_002():
    MAOM = MainAgencyOrgManage()

    # data = [("个代渠道", "交叉销售委托合同", "32993J220082100"), ("经代渠道", "保险专业代理委托合同", "1"), ("银保渠道", "保险专业代理委托合同", "1"),
    #         ("车商渠道", "保险兼业代理委托合同(外部)", "1")]
    data = [("个代渠道", "交叉销售委托合同", "32993J220082100")]

    @allure.story("查询")
    @pytest.mark.usefixtures("login_jiangsu_c_fun")
    @pytest.mark.parametrize("channel,contractType,contract_no", data)
    def test_001(self, channel, contractType, contract_no):
        info("中介机构新增和变更申报页:{}".format(channel))
        self.MAOM.into_page(channel)
        info("查询")
        self.MAOM.query(contract_no,contractType, "1")
        
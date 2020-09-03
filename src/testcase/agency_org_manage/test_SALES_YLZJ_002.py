#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 15:48
# @Author: hjy
# @File : test_SALES_YLZJ_002.py    中介机构>>中介机构新增和变更申报>>续签
import allure
import pytest

from config.global_var import sleep
from src.page.agency_module.agency_module_page.agency_contract_renew_approval import AgencyContractRenewApproval
from src.page.agency_module.agency_module_page.agency_contract_renew import AgencyContractRenew
from src.page.agency_module.main_agency_org_approval import MainAgencyOrgApproval
from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("中介机构>>中介机构新增和变更申报>>续签-002")
class Test_SALES_YLZJ_002():
    MAOM = MainAgencyOrgManage()
    ACR = AgencyContractRenew()
    MAOA = MainAgencyOrgApproval()  # 审批
    ACRA = AgencyContractRenewApproval()

    data = csv_util.data_reader("agency_org_manage/Test_SALES_YLZJ_002.csv")

    # data = [("个代渠道", "交叉销售委托合同", "32993J220082400"), ("经代渠道", "保险专业代理委托合同", "329921120082400"), ("银保渠道", "保险兼业代理委托合同(外部)", "329930020082600"),
    #        ("车商渠道", "保险兼业代理委托合同(外部)", "329930020082500")]
    # data = [("银保渠道", "保险兼业代理委托合同(外部)", "329930020082600")]

    @allure.story("续签、审批")
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    @pytest.mark.parametrize("channel,contractType,contract_no", data)
    def test_001(self, channel, contractType, contract_no):
        self.MAOM.switch_to_default_content()
        info("中介机构新增和变更申报页:{}".format(channel))
        self.MAOM.into_page(channel)
        info("查询")
        self.MAOM.query(contract_no, contractType, "1")
        self.MAOM.select_data("状态", "有效", "选择")
        self.MAOM.click_btn("续签")
        self.MAOM.switch_max_window()
        self.ACR.assertEqual("判断页面标题", self.ACR.get_head_text(), "中介合同续签")
        self.ACR.click(self.ACR.get_element_xpath(self.ACR.renew_submit))
        self.ACR.choose_ok_on_alert()
        self.ACR.submit_interaction(self.ACR.submit_frame)
        text = self.ACR.get_text(self.ACR.get_element_xpath(self.ACR.save_success))
        self.ACR.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("中介机构{}续签提交".format(channel))
        contract_no = text.split("：")[1]
        self.ACR.close_button_ty()
        info("中介机构续签-审批")
        self.MAOA.switch_to_window()
        info("中介机构审批页")
        self.MAOA.into_page(channel)
        info("查询合同号：{}".format(contract_no))
        self.MAOA.query(contract_no)
        info("选择数据")
        self.MAOA.select_data("续签审批")
        info("中介合同续签审批页")
        self.MAOA.switch_max_window()
        self.ACRA.assertEqual("判断页面标题", self.ACRA.get_head_text(), "中介合同续签审批")
        info("审批")
        self.ACRA.click(self.ACRA.get_element_xpath(self.ACRA.pass_check))
        self.ACRA.choose_ok_on_alert()
        info("提交任务")
        self.ACRA.submit_interaction(iframe_xpath=self.ACRA.submit_frame, textarea="中介机构{}续签-ui测试".format(channel))
        text = self.ACRA.get_text(self.ACRA.get_element_xpath(self.ACRA.save_success))
        get_screenshot("中介机构{}续签审核".format(channel))
        self.ACRA.assertResult("验证提交成功", "保存成功!" in text)
        self.ACRA.close_button_ty()
        sleep(2)

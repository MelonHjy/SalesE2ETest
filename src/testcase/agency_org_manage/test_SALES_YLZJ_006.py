#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 15:41
# @Author: fyl
# @File : test_SALES_YLZJ_006.py    中介机构>>中介机构新增和变更申报>>终止
import allure
import pytest

from src.page.agency_module.agency_module_page.agency_contract_cancel import AgencyContractCancel
from src.page.agency_module.agency_module_page.agency_contract_concel_approval import AgencyContractConcelApproval
from src.page.agency_module.main_agency_org_approval import MainAgencyOrgApproval
from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils import csv_util
from src.utils.log import info

data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_006.csv")

@allure.feature("中介机构>>中介机构新增和变更申报>>终止")
@pytest.mark.parametrize("channel,contract_no,contractType", data,scope="class")
class Test_SALES_YLZJ_006():
    MAOM = MainAgencyOrgManage()
    ACC = AgencyContractCancel()
    MAOA = MainAgencyOrgApproval()  # 审批
    ACCA = AgencyContractConcelApproval()
    msg = None

    @allure.story("中介机构合同终止")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_001(self, channel, contract_no, contractType):
        info("中介机构>>中介机构新增和变更申报>>终止")
        info("中介机构新增和变更申报页:{}".format(channel))
        self.MAOM.into_page(channel)
        self.MAOM.assertEqual("验证页面标题", self.MAOM.get_head_text(), "中介机构新增和变更申报")
        info("查询")
        self.MAOM.query(contract_no, contractType, "1")
        info("选择数据")
        self.MAOM.select_data("合同编号", contract_no, "选择")
        info("终止中介合同页")
        self.MAOM.click_btn("终止")
        self.MAOM.switch_max_window()
        self.ACC.assertEqual("验证页面标题", self.ACC.get_head_text(), "终止中介合同")
        info("终止")
        self.ACC.click(self.ACC.get_element_xpath(self.ACC.contract_cancel))
        info("提交任务")
        self.ACC.submit_interaction(self.ACC.submit_frame, textarea="ui测试-中介机构合同终止")
        text = self.ACC.get_text(self.ACC.get_element_xpath(self.ACC.save_success))
        self.ACC.assertResult("验证提交成功", "保存成功!" in text)
        self.ACC.close_button_ty()
        info("中介机构合同终止")
        self.MAOA.switch_to_window()
        info("中介机构审批页")
        self.MAOA.into_page(channel)
        info("查询合同号：{}".format(contract_no))
        self.MAOA.query(contract_no)
        info("选择数据")
        self.MAOA.select_data("注销审批")
        self.MAOA.switch_max_window()
        info("中介合同注销审批页")
        self.ACCA.assertEqual("验证页面标题", self.ACCA.get_head_text(), "中介合同注销审批")
        info("审批")
        self.ACCA.click(self.ACCA.get_element_xpath(self.ACCA.pass_check))
        info("保存提交")
        self.ACCA.submit_interaction(self.ACCA.submit_frame, textarea="ui测试-中介机构合同终止审批")
        text = self.ACCA.get_text(self.ACCA.get_element_xpath(self.ACCA.save_success))
        self.ACCA.assertResult("验证提交成功", "保存成功!" in text)
        self.ACCA.close_button_ty()
        info("中介机构合同终止-验证")
        self.MAOM.switch_to_window()
        info("中介机构审批页")
        self.MAOM.into_page(channel)
        info("查询合同号：{}".format(contract_no))
        self.MAOM.query(contract_no, contractType, "1")
        text = self.MAOM.get_cell_text_by_head("状态", 0)
        self.MAOM.assertEqual("验证机构是否有效", text, "无效")

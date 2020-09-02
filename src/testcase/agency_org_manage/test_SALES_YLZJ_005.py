#  -*- coding:utf-8 -*-
# @Time : 2020/8/25 14:27
# @Author: hjy
# @File : test_SALES_YLZJ_005.py    中介机构>>中介机构新增和变更申报>>修改
import allure
import pytest

from src.page.agency_module.agency_module_page.agency_contract_modify import AgencyContractModify
from src.page.agency_module.agency_module_page.agency_contract_modify_approval import AgencyContractModifyApproval
from src.page.agency_module.main_agency_org_approval import MainAgencyOrgApproval
from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("中介机构>>中介机构新增和变更申报>>修改-005")
class Test_SALES_YLZJ_005():
    MAOM = MainAgencyOrgManage()
    ACM = AgencyContractModify()
    MAOA = MainAgencyOrgApproval()  # 审批
    ACMA = AgencyContractModifyApproval()

    data = csv_util.data_reader("agency_org_manage/Test_SALES_YLZJ_005.csv")

    # data = [("个代渠道", "交叉销售委托合同", "32993J220082501"), ("经代渠道", "保险专业代理委托合同", "329921120082500"), ("银保渠道", "保险专业代理委托合同(外部)", "329930020082601"),
    #         ("车商渠道", "保险兼业代理委托合同(外部)", "329930020082502")]
    # data = [("车商渠道", "保险兼业代理委托合同(外部)", "329930020082502", "2020-12-30", "中国工商银行股份有限公司", "新疆维吾尔自治区_巴音郭楞蒙古自治州",
    #          "中国工商银行股份有限公司库尔勒人民东路支行")]

    @allure.story("修改、审批")
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    @pytest.mark.parametrize("channel,contractType,contract_no,start_date,sa_Account_bankName,bank_area,bank_Name",
                             data)
    def test_001(self, channel, contractType, contract_no, start_date, sa_Account_bankName, bank_area, bank_Name):
        self.MAOM.switch_to_default_content()
        info("中介机构新增和变更申报页:{}".format(channel))
        self.MAOM.into_page(channel)
        info("查询")
        self.MAOM.query(contract_no, contractType, "1")
        self.MAOM.select_data("状态", "有效", "选择")
        self.MAOM.click_btn("修改")
        self.MAOM.switch_max_window()
        self.ACM.assertEqual("判断页面标题", self.ACM.get_head_text(), "编辑中介合同信息")
        self.ACM.pick_date_old(self.ACM.imgBtn1.format("1"), start_date)
        self.ACM.click(self.ACM.get_element_xpath(self.ACM.add_account.format('0')))
        self.ACM.switch_to_window()
        if self.ACM.get_head_text() == "银行账号编辑":
            info("添加银行账号")
            self.ACM.send_keys_(self.ACM.sa_Account_bankName, sa_Account_bankName)
            self.ACM.send_keys_(self.ACM.bank_area, bank_area)
            self.ACM.send_keys_(self.ACM.bank_Name, bank_Name)
            self.ACM.click(self.ACM.get_element_xpath(self.ACM.save_account))
            self.ACM.choose_ok_on_alert()
            self.ACM.switch_to_window()
        self.ACM.click(self.ACM.get_element_xpath(self.ACM.contractUpdate_submit))
        self.ACM.choose_ok_on_alert()
        self.ACM.submit_interaction(self.ACM.submit_frame)
        text = self.ACM.get_text(self.ACM.get_element_xpath(self.ACM.save_success))
        self.ACM.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("中介机构{}修改".format(channel))
        contract_no = text.split("：")[1]
        info("关闭")
        self.ACM.close_button_ty()
        info("中介机构修改-审批")
        self.MAOA.switch_to_window()
        info("中介机构审批页")
        self.MAOA.into_page(channel)
        info("查询合同号：{}".format(contract_no))
        self.MAOA.query(contract_no)
        info("选择数据")
        self.MAOA.select_data("修改审批")
        info("中介合同修改审批页")
        self.MAOA.switch_max_window()
        self.ACMA.assertEqual("判断页面标题", self.ACMA.get_head_text(), "中介合同修改审批")
        info("审批")
        self.ACMA.click(self.ACMA.get_element_xpath(self.ACMA.pass_check))
        self.ACMA.choose_ok_on_alert()
        info("提交任务")
        self.ACMA.submit_interaction(self.ACMA.submit_frame, "中介机构修改-ui测试")
        text = self.ACMA.get_text(self.ACMA.get_element_xpath(self.ACMA.save_success))
        self.ACMA.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("中介机构{}修改审核".format(channel))
        self.ACMA.close_button_ty()

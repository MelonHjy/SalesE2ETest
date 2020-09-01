#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:05
# @Author: fyl
# @File : test_SALES_YLZJ_012.py    中介模块>>佣金比例上限标准查询修改>>修改
import allure
import pytest

from src.page.agency_module.agency_module_page.commission_approval import CommissionApproval
from src.page.agency_module.agency_module_page.commission_edit import CommissionEdit
from src.page.agency_module.main_commission_approval import MainCommissionApproval
from src.page.agency_module.main_commission_edit import MainCommisson_edit
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_012.csv")


@allure.feature("中介模块>>佣金比例上限标准查询修改>>修改")
@pytest.mark.parametrize("channel,rule_no,rule_name, new_rule_name", data, scope="class")
class Test_SALES_YLZJ_012():
    MCE = MainCommisson_edit()
    CE = CommissionEdit()
    MCA = MainCommissionApproval()
    CA = CommissionApproval()

    @allure.story("佣金比例上限标准查询修改")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_001(self, channel, rule_no, rule_name, new_rule_name):
        info("中介模块>>佣金比例上限标准查询修改>>修改:{}".format(channel))
        self.MCE.into_page(channel)
        self.MCE.assertEqual("验证页面标题", self.MCE.get_head_text(), "佣金比例上限标准查询修改")
        info("查询配置单号{}".format(rule_no))
        self.MCE.query(rule_no)
        if self.MCE.alert_is_present():
            self.MCE.choose_ok_on_alert()
        info("选择数据")
        self.MCE.select_data("佣金配置名称", rule_name, "操作")
        self.MCE.switch_max_window()
        self.CE.assertEqual("验证页面标题", self.CE.get_head_text(), "佣金配置信息编辑")
        info("修改配置佣金名")
        self.CE.send_keys(self.CE.get_element_xpath(self.CE.rule_name), new_rule_name)
        self.CE.click(self.CE.get_element_xpath(self.CE.submit))
        text = self.CE.get_text(self.CE.get_element_xpath(self.CE.save_success))
        self.CE.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("佣金配置修改-{}".format(channel))
        self.CE.close_button_ty()
        self.CE.switch_to_window()
        info("佣金比例上限标准查询修改-审核")
        self.MCA.into_page(channel)
        info("查询")
        self.MCA.query(rule_no=rule_no)
        info("选择数据")
        self.MCA.select_data("配置单号", rule_no, "操作")
        self.MCA.switch_max_window()
        # 页面
        self.CA.click(self.CA.wait_until_el_xpath(self.CA.check_pass))
        text = self.CA.get_text(self.CA.get_element_xpath(self.CA.save_success))
        self.CA.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("佣金配置修改审核-{}".format(channel))
        self.CA.close_button_ty()
        self.CA.switch_to_window()
        info("佣金比例上限标准查询修改-验证")
        self.MCE.into_page(channel)
        info("查询")
        self.MCE.query(rule_no)
        self.MCE.assertEqual("验证修改的信息", self.MCE.get_cell_text_by_head("佣金配置名称")[0], new_rule_name)
        get_screenshot("佣金配置修改验证-{}".format(channel))

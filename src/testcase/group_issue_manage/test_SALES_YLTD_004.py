#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_004.py    团队出单权管理>>团队信息变更（变更团队非重要信息）
import allure
import pytest

from config.global_var import sleep
from src.page.group_issue_manage.main_group_issue_manage import MainGroupIssueManage
from src.page.group_issue_manage.main_group_issue_page.edit_group import EditGroup
from src.page.group_issue_manage.main_group_issue_page.group_view import GroupView
from src.page.integrated_management.main_sales_group import MainSalesGroup
from src.page.integrated_management.sales_group_recheck_page.valid_group_edit_recheck import ValidGroupEditRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("group_issue_manage/Test_SALES_YLTD_004.csv")


@allure.feature("团队出单权管理>>团队信息变更（变更团队非重要信息）")
@pytest.mark.usefixtures("login_jiangsu_p")
@pytest.mark.parametrize("pk_deptdoc, group_name, business_focus, business_desc,build_date", data)
class Test_SALES_YLTD_004():
    MGIM = MainGroupIssueManage()
    EG = EditGroup()
    MSG = MainSalesGroup()
    VGER = ValidGroupEditRecheck()
    GV = GroupView()

    # data = [("32990090", "ui测试-004", "重点行业", "ui测试指定重点行业", "2021-01-01")]

    @allure.story("变更团队非重要信息-004")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("restore_data")
    def test_001(self, pk_deptdoc, group_name, business_focus, business_desc, build_date):
        self.MGIM.switch_to_default_content()
        info("进入团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名：{}".format(group_name))
        self.MGIM.query(group_name=group_name)
        info("选择团队")
        self.MGIM.select_data("团队代码", pk_deptdoc, "选择")
        self.MGIM.click_btn("团队信息变更")
        self.MGIM.switch_max_window()
        info("团队信息变更页")
        self.EG.assertEqual("判断页面标题", self.EG.get_head_text(), "团队修改")
        info("修改->重点发展->建团日期")
        self.EG.select(self.EG.business_focus, business_focus)
        self.EG.send_keys(self.EG.get_element_xpath(self.EG.business_desc), business_desc)
        self.EG.pick_date_old(self.EG.img_Btn, build_date)
        info("保存并提交")
        self.EG.click(self.EG.get_element_xpath(self.EG.submit_btn))
        self.EG.submit_interaction(self.EG.submit_iframe)
        get_screenshot("团队非重要信息变更")
        self.EG.close_button_ty()
        info("变更团队非重要信息-审核")
        self.MSG.switch_to_window()
        info("团队审核")
        self.MSG.into_page()
        info("查询团队名称：{}".format(group_name))
        self.MSG.query(group_name=group_name)
        self.MSG.select_data("有效修改审核")
        self.MSG.switch_max_window()
        self.VGER.assertEqual("判断页面标题", self.VGER.get_head_text(), "有效修改团队审核")
        info("审核")
        self.VGER.click(self.VGER.wait_until_el_xpath(self.VGER.submit_btn))
        self.VGER.submit_interaction(iframe_xpath=self.VGER.submit_iframe, textarea="ui测试-变更团队非重要信息-审核")
        get_screenshot("团队非重要信息变更审核")
        self.VGER.close_button_ty()
        sleep(2)

    @allure.story("变更团队非重要信息-验证")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    def test_002(self, pk_deptdoc, group_name, business_focus, business_desc, build_date):
        self.MGIM.switch_to_window()
        info("团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名称：{}".format(group_name))
        self.MGIM.query(group_name=group_name)
        # self.MGIM.query("ui测试-003")
        text = self.MGIM.get_cell_text_by_head("团队状态", 0)
        self.MGIM.assertEqual("判断团队状态是否有效", text, "有效")
        process = self.MGIM.get_cell_text_by_head("终止流程", 0)
        self.MGIM.assertEqual("判断最后一栏没有终止流程按钮", process, "")
        self.MGIM.select_data("团队名称", group_name, "查看")
        self.MGIM.switch_max_window()
        self.GV.assertEqual("判断页面标题", self.GV.get_head_text(), "团队查看")
        # self.GV.assertEqual("验证重点发展", self.GV.get_business_focus(), Test_SALES_YLTD_004.msg["business_focus"])
        self.GV.assertEqual("验证重点发展描述", self.GV.get_business_desc(), business_desc)
        self.GV.assertEqual("验证团队组建日期", self.GV.get_build_date().strip(), build_date)
        get_screenshot("团队非重要信息变更验证")
        sleep(2)

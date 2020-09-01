#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_003.py    团队出单权管理>>团队信息变更（变更团队重要信息）   待处理
import sys

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

data = csv_util.data_reader("group_issue_manage/Test_SALES_YLTD_003.csv")


@allure.feature("团队出单权管理>>团队信息变更（变更团队重要信息）-003")
@pytest.mark.parametrize("pk_deptdoc, group_name,group_type,business_name,business_focus,business_desc", data)
class Test_SALES_YLTD_003():
    MGIM = MainGroupIssueManage()
    EG = EditGroup()
    MSG = MainSalesGroup()
    VGER = ValidGroupEditRecheck()
    GV = GroupView()

    # data = [("32990089", "ui测试-003", "直销团队", "其它", "重点客户", "ui测试指定客户")]

    # def get_data(self):
    #     return super().get_data()

    @allure.story("变更团队重要信息")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p","restore_data")
    def test_001(self, pk_deptdoc, group_name, group_type, business_name, business_focus, business_desc):
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
        info("修改")
        info("团队属性：{}".format(group_type))
        self.EG.select(self.EG.grouptype1, group_type)
        info("团队主营业务分类：{}".format(business_name))
        self.EG.send_keys(self.EG.get_element_xpath(self.EG.business_name), business_name)
        info("重点发展业务")
        self.EG.select(self.EG.business_focus, business_focus)
        self.EG.send_keys(self.EG.get_element_xpath(self.EG.business_desc), business_desc)
        info("保存并提交")
        self.EG.click(self.EG.get_element_xpath(self.EG.submit_btn))
        self.EG.submit_interaction(self.EG.submit_iframe)
        get_screenshot("团队信息变更")
        self.EG.close_button_ty()
        info("变更团队重要信息-审核")
        self.MSG.switch_to_window()
        info("团队审核")
        self.MSG.into_page()
        info("查询团队名称：{}".format(group_name))
        self.MSG.query(group_name=group_name)
        self.MSG.select_data("有效修改审核")
        self.MSG.switch_max_window()
        self.VGER.assertEqual("判断页面标题", self.VGER.get_head_text(), "有效修改团队审核")
        info("审核")
        self.VGER.click(self.VGER.wait_until_el_xpath(self.VGER.recheck_btn))
        sleep(2)
        text = self.VGER.get_alert_text()
        info("提示信息：{}".format(text))
        self.VGER.assertEqual("判断提示信息", text, "确定推送至HR系统吗？")
        self.VGER.choose_ok_on_alert()
        sleep(2)
        text = self.VGER.get_alert_text()
        get_screenshot("团队信息变更审核")
        info("提示信息：{}".format(text))
        self.VGER.assertEqual("判断提示信息", text, "{}:团队信息推送成功！".format(group_name))
        self.VGER.choose_ok_on_alert()
        self.VGER.close_tab()

    @allure.story("模拟Hr推送至销管系统")
    @pytest.mark.dependency(name='test_send', depends=['test_001'])
    def test_send(self, pk_deptdoc, group_name, group_type, business_name, business_focus, business_desc):
        self.MGIM.hr_send_change(group_name)

    @allure.story("变更团队重要信息-验证")
    @pytest.mark.dependency(name='test_002', depends=['test_send'])
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_002(self, pk_deptdoc, group_name, group_type, business_name, business_focus, business_desc):
        self.MGIM.switch_to_window()
        info("团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名称：{}".format(group_name))
        self.MGIM.query(group_name=group_name)
        # self.MGIM.query("ui测试-003")
        text = self.MGIM.get_text(self.MGIM.get_element_xpath(self.MGIM.query_data))
        if text not in "无记录.":
            text = self.MGIM.get_cell_text_by_head("团队状态", 0)
            self.MGIM.assertEqual("判断团队状态是否有效", text, "有效")
            process = self.MGIM.get_cell_text_by_head("终止流程", 0)
            self.MGIM.assertEqual("判断最后一栏没有终止流程按钮", process, "")
            self.MGIM.select_data("团队名称", group_name, "查看")
            self.MGIM.switch_max_window()
            self.GV.assertEqual("判断页面标题", self.GV.get_head_text(), "团队查看")
            self.GV.assertEqual("验证团队属性", self.GV.get_group_type(), group_type)
            self.GV.assertEqual("验证主营业务", self.GV.get_business_name(), business_name)
            # self.GV.assertEqual("验证重点发展", self.GV.get_business_focus(),Test_SALES_YLTD_003.msg["business_focus"])
            self.GV.assertEqual("验证重点发展描述", self.GV.get_business_desc(), business_desc)
            get_screenshot("团队信息变更验证")
            sleep(2)

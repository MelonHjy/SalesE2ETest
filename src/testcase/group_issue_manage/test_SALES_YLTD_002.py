#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_002.py    团队出单权管理>>团队信息变更（无效的团队进行复效）
import allure
import pytest

from config.global_var import sleep
from src.page.group_issue_manage.main_group_issue_manage import MainGroupIssueManage
from src.page.group_issue_manage.main_group_issue_page.edit_group import EditGroup
from src.page.integrated_management.main_sales_group import MainSalesGroup
from src.page.integrated_management.sales_group_recheck_page.edit_group_recheck import EditGroupRecheck
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("group_issue_manage/test_SALES_YLTD_002.csv")


@allure.feature("团队出单权管理>>团队信息变更（无效的团队进行复效）-002")
@pytest.mark.parametrize("pk_deptdoc, group_name", data)
class Test_SALES_YLTD_002():
    MGIM = MainGroupIssueManage()
    EG = EditGroup()
    MSG = MainSalesGroup()
    EGR = EditGroupRecheck()

    # data = [("32990092", "ui测试-002x")]

    @allure.story("无效的团队进行复效")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p","restore_data")
    def test_001(self, pk_deptdoc, group_name):
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
        info("保存并提交")
        self.EG.click(self.EG.get_element_xpath(self.EG.submit_btn))
        self.EG.submit_interaction(self.EG.submit_iframe)
        get_screenshot("团队复效提交")
        self.EG.close_button_ty()
        info("无效的团队进行复效-审核")
        self.MSG.switch_to_window()
        info("团队审核")
        self.MSG.into_page()
        info("查询团队名称：{}".format(group_name))
        self.MSG.query(group_name=group_name)
        self.MSG.select_data("无效修改审核")
        self.MSG.switch_max_window()
        self.EGR.assertEqual("判断页面标题", self.EGR.get_head_text(), "无效修改团队审核")
        info("审核")
        self.EGR.click(self.EGR.get_element_xpath(self.EGR.recheck_btn))
        sleep(2)
        text = self.EGR.get_alert_text()
        info("提示信息：{}".format(text))
        self.EGR.assertEqual("判断提示信息", text, "确定推送至HR系统吗？")
        self.EGR.choose_ok_on_alert()
        sleep(2)
        text = self.EGR.get_alert_text()
        get_screenshot("团队复效审核")
        info("提示信息：{}".format(text))
        self.EGR.assertEqual("判断提示信息", text, "{}:团队信息推送成功！".format(group_name))
        self.EGR.choose_ok_on_alert()
        self.EGR.close_tab()
        self.EGR.switch_to_window()

    @allure.story("模拟Hr推送至销管系统")
    @pytest.mark.dependency(name='test_send', depends=['test_001'])
    def test_send(self, pk_deptdoc, group_name):
        self.MGIM.hr_send_recovery(group_name)

    @allure.story("无效的团队进行复效-验证")
    @pytest.mark.dependency(name='test_002', depends=['test_send'])
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_002(self, pk_deptdoc, group_name):
        info("团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名称：{}".format(group_name))
        self.MGIM.query(group_name=group_name)
        # self.MGIM.query("ui测试-002")
        text = self.MGIM.get_text(self.MGIM.get_element_xpath(self.MGIM.query_data))
        get_screenshot("团队复效验证")
        if text.strip() != "无记录.":
            text = self.MGIM.get_cell_text_by_head("团队状态", 0)
            self.MGIM.assertEqual("判断团队状态是否有效", text, "有效")
            process = self.MGIM.get_cell_text_by_head("终止流程", 0)
            self.MGIM.assertEqual("判断最后一栏没有终止流程按钮", process, "")
            get_screenshot("团队复效验证")
            sleep(2)

#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_005.py    团队出单权管理>>团队注销
import allure
import pytest

from config.global_var import sleep
from src.page.group_issue_manage.main_group_issue_manage import MainGroupIssueManage
from src.page.group_issue_manage.main_group_issue_page.dismiss_group import DismissGroup
from src.page.integrated_management.sales_group_recheck_page.dismiss_group_recheck import DismissGroupRecheck
from src.page.integrated_management.main_sales_group import MainSalesGroup
from src.utils.log import info


@allure.feature("团队出单权管理>>团队注销")
class Test_SALES_YLTD_005():
    MGIM = MainGroupIssueManage()
    DG = DismissGroup()
    MSG = MainSalesGroup()
    DGR = DismissGroupRecheck()
    msg = None

    data = [("32990087", "ui测试-005")]
    # @pytest.mark.skip
    @allure.story("团队注销")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize("pk_deptdoc, group_name", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_001(self, pk_deptdoc, group_name):
        Test_SALES_YLTD_005.msg = {"pk_deptdoc": pk_deptdoc, "group_name": group_name}
        info("进入团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名：{}".format(group_name))
        self.MGIM.query(group_name=group_name)
        info("选择团队")
        self.MGIM.select_data("团队代码", pk_deptdoc, "选择")
        info("团队注销页")
        self.MGIM.click_btn("团队注销")
        self.MGIM.switch_max_window()
        self.DG.assertEqual("判断页面标题", self.DG.get_head_text(), "团队注销")
        info("注销")
        self.DG.click(self.DG.get_element_xpath(self.DG.dismiss_group))
        self.DG.submit_interaction(self.DG.submit_iframe)
        self.DG.close_button_ty()

    @allure.story("团队注销-审核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002(self):
        info("团队审核")
        self.MSG.into_page()
        info("查询团队名称：{}".format(Test_SALES_YLTD_005.msg["group_name"]))
        self.MSG.query(group_name=Test_SALES_YLTD_005.msg["group_name"])
        # self.MSG.query(group_name="32990087")
        self.MSG.select_data(status_text="注销审核")
        self.MSG.switch_max_window()
        self.DGR.assertEqual("判断页面标题", self.DGR.get_head_text(), "团队注销")
        info("审核")
        self.DGR.click(self.DGR.get_element_xpath(self.DGR.recheck_btn))
        sleep(2)
        text = self.DGR.get_alert_text()
        info("提示信息：{}".format(text))
        self.DGR.assertEqual("判断提示信息", text, "确定推送至HR系统吗？")
        self.DGR.choose_ok_on_alert()
        sleep(2)
        text = self.DGR.get_alert_text()
        info("提示信息：{}".format(text))
        self.DGR.assertEqual("判断提示信息", text, "{}:团队信息推送成功！".format(Test_SALES_YLTD_005.msg["group_name"]))
        self.DGR.choose_ok_on_alert()

    @allure.story("团队申报-验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_003(self):
        info("团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名称：{}".format(Test_SALES_YLTD_005.msg["group_name"]))
        self.MGIM.query(group_name=Test_SALES_YLTD_005.msg["group_name"])
        # self.MGIM.query("ui测试-005")
        text = self.MGIM.get_cell_text_by_head("团队状态", 0)
        self.MGIM.assertEqual("判断团队状态是否有效", text, "注销")
        process = self.MGIM.get_cell_text_by_head("终止流程", 0)
        self.MGIM.assertEqual("判断最后一栏没有终止流程按钮", process, "")

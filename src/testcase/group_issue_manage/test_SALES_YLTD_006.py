#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_006.py    经营机构>>团队模块>>综拓团队申请
import allure
import pytest

from src.page.group_issue_manage.main_zt_group_apply import MainZtGroupApply
from src.page.integrated_management.main_zt_group_approval import MainZtGroupApproval
from src.page.integrated_management.zt_group_approval_page.zt_group_approval import ZtGroupApproval
from src.utils import csv_util
from src.utils.except_util import get_screenshot, sleep
from src.utils.log import info

data = csv_util.data_reader("group_issue_manage/Test_SALES_YLTD_006.csv")


@allure.feature("经营机构>>团队模块>>综拓团队申请")
@pytest.mark.parametrize("pk_deptdoc, group_name", data)
class Test_SALES_YLTD_006():
    MZGA = MainZtGroupApply()
    ZGA = MainZtGroupApproval()
    ZTP = ZtGroupApproval()

    # data = [("32019960", "ui测试-006")]

    @allure.story("综拓团队申请")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_c_fun")
    def test_001(self, pk_deptdoc, group_name):
        info("进入团队出单权管理页")
        self.MZGA.into_page()
        # 验证页面
        self.MZGA.assertEqual("判断页面标题", self.MZGA.get_head_text(), "综拓团队申请")
        info("查询团队名：{}".format(group_name))
        self.MZGA.query(group_name=group_name)
        info("选择团队")
        self.MZGA.select_data("团队代码", pk_deptdoc, "选择")
        info("申请")
        self.MZGA.click(self.MZGA.get_element_xpath(self.MZGA.input_btn.format("申请")))
        alert = self.MZGA.get_alert_text()
        self.MZGA.assertEqual("判断提示语句是否申请成功", alert, "提交申请成功")
        get_screenshot("综拓团队申请")
        self.MZGA.choose_ok_on_alert()
        info("综拓团队申请-审批")
        self.ZGA.switch_to_window()
        info("进入团队出单权管理页")
        self.ZGA.into_page()
        info("查询申请团队")
        self.ZGA.query(group_name)
        info("选择")
        self.ZGA.select_data("有效修改审批")
        self.ZGA.switch_max_window()
        info("审批")
        self.ZTP.click(self.ZTP.wait_until_el_xpath(self.ZTP.approval_btn))
        self.ZTP.assertEqual("判断页面标题", self.ZTP.get_head_text(), "综拓团队申请审批")
        self.ZTP.submit_interaction(self.ZTP.submit_iframe, textarea="综拓团队申请-ui测试")
        get_screenshot("综拓团队申请审核")
        self.ZTP.close_button_ty()

    @allure.story("综拓团队申请-验证")
    @pytest.mark.dependency(name='test_003', depends=["test_001", "test_002"])
    @pytest.mark.usefixtures("login_jiangsu_c_fun")
    def test_003(self, pk_deptdoc, group_name):
        info("进入团队出单权管理页")
        self.MZGA.into_page()
        info("查询团队名：{}".format(group_name))
        self.MZGA.query(group_name=group_name)
        index = self.MZGA.get_cell_text_by_head("团队代码").index(pk_deptdoc)
        text = self.MZGA.get_cell_text_by_head("团队主营业务分类", index)
        self.MZGA.assertEqual("验证团队主营业务分类", text.strip(), "综拓")
        sleep(2)

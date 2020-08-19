#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_001.py    团队出单权管理>>新增团队
import allure
import pytest

from config.global_var import sleep
from src.page.group_issue_manage.main_group_issue_manage import MainGroupIssueManage
from src.page.group_issue_manage.main_group_issue_page.group_declare import GroupDeclare
from src.page.integrated_management.main_sales_group import MainSalesGroup
from src.page.integrated_management.sales_group_recheck_page.sales_group_recheck import SalesGroupRecheck
from src.utils.except_util import get_screenshot
from src.utils.log import info


@allure.feature("团队出单权管理>>新增团队")
class Test_SALES_YLTD_001():
    MGIM = MainGroupIssueManage()
    GD = GroupDeclare()
    MSG = MainSalesGroup()
    SGR = SalesGroupRecheck()

    msg = None

    data = [("ui测试-001", "32000000--中国人民财产保险股份有限公司江苏省分公司", "营销团队", "其它--营销", "2020-09-30")]

    @allure.story("团队申报")
    @pytest.mark.parametrize("group_name,com_code,group_type,business_name,build_date", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_001')
    def test_001(self, group_name, com_code, group_type, business_name, build_date):
        Test_SALES_YLTD_001.msg = {"group_name": group_name}
        info("进入团队出单权管理页")
        self.MGIM.into_page()
        info("进入新增团队页")
        self.MGIM.click_btn("新增团队")
        self.MGIM.switch_max_window()
        info("团队申报页")
        self.GD.assertEqual("判断页面标题", self.GD.get_head_text(), "团队申报")
        info("团队名称：{}".format(group_name))
        self.GD.input_group_name(group_name)
        info("上级机构：{}".format(com_code))
        self.GD.code_select_input(self.GD.com_code, com_code)
        info("团队属性：{}".format(group_type))
        self.GD.select(self.GD.grouptype1, group_type)
        info("团队主营业务分类：{}".format(business_name))
        self.GD.code_select_input(self.GD.business_name, business_name)
        info("团队组建如期：{}".format(build_date))
        self.GD.pick_date_old(self.GD.img_Btn, build_date)
        info("保存并提交")
        self.GD.click(self.GD.wait_until_el_xpath(self.GD.submit_btn))
        self.GD.submit_interaction(self.GD.submit_iframe)
        text = self.GD.get_text(self.GD.wait_until_el_xpath(self.GD.save_success))
        self.GD.assertResult("验证复核成功", "保存成功!" in text)
        get_screenshot("提交")
        self.GD.close_button_ty()

    @allure.story("团队申报-审核")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    def test_002(self):
        info("团队审核")
        self.MSG.into_page()
        info("查询团队名称：{}".format(Test_SALES_YLTD_001.msg["group_name"]))
        self.MSG.query(group_name=Test_SALES_YLTD_001.msg["group_name"])
        self.MSG.select_data("新增审核")
        self.MSG.switch_max_window()
        info("审核")
        self.SGR.click(self.SGR.wait_until_el_xpath(self.SGR.recheck_btn))
        sleep(3)
        text = self.SGR.get_alert_text()
        info("提示信息：{}".format(text))
        self.MSG.assertEqual("判断提示信息", text, "确定推送至HR系统吗？")
        self.MSG.choose_ok_on_alert()
        sleep(2)
        text = self.SGR.get_alert_text()
        info("提示信息：{}".format(text))
        self.MSG.assertEqual("判断提示信息", text, "{}:团队信息推送成功！".format(Test_SALES_YLTD_001.msg["group_name"]))
        self.MSG.choose_ok_on_alert()

    @allure.story("团队申报-验证")
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    @pytest.mark.dependency(name='test_003', depends=['test_002'])
    def test_003(self):
        self.MGIM.hr_send_create(Test_SALES_YLTD_001.msg["group_name"], '32999999', '1130B810000000UITEST')
        info("团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名称：{}".format(Test_SALES_YLTD_001.msg["group_name"]))
        self.MGIM.query(group_name=Test_SALES_YLTD_001.msg["group_name"])
        # self.MGIM.query("ui测试-001")
        text = self.MGIM.get_cell_text_by_head("团队状态", 0)
        self.MGIM.assertEqual("判断团队状态是否有效", text, "有效")
        process = self.MGIM.get_cell_text_by_head("终止流程", 0)
        self.MGIM.assertEqual("判断最后一栏没有终止流程按钮", process, "")

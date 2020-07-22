#  -*- coding:utf-8 -*-
# @Time : 2020/7/21 16:00
# @Author: fyl
# @File : test_SALES_YLDLZ_005.py   营销团队经理解聘
import allure
import pytest

from config.global_var import sleep
from src.page.agent_sales_manage.dismissal_manager import DismissalManager
from src.page.agent_sales_manage.main_management_agent_salesmen import ManagementOfAgentSalesmen
from src.utils.except_util import get_screenshot
from src.utils.log import *


@allure.feature("有效的经理解聘该人员经理职务")
class Test_YLDLZ_005():
    main_management_agent_salesmen = ManagementOfAgentSalesmen()
    dismissal_manager = DismissalManager()

    data = [("83258554")]

    @pytest.mark.parametrize("user_code", data)
    @pytest.mark.usefixtures("login_jiangsu_p")
    def test_YLDLZ_005(self, user_code):
        info("进入代理制销售人员代码管理页面")
        self.main_management_agent_salesmen.into_page()
        info("查询该人员代码是否存在数据")
        self.main_management_agent_salesmen.query(user_code)
        # 判断查询的数据 在状态列的值为”有效“
        info("选择数据")
        row = self.main_management_agent_salesmen.select_by_user_code(user_code)
        text = self.main_management_agent_salesmen.get_cell_text_by_head("状态", row)
        self.main_management_agent_salesmen.assertEqual("判断状态列的值为”有效“", text, "有效")
        info("进入“营销团队经理解聘”页面")
        self.main_management_agent_salesmen.click(
            self.main_management_agent_salesmen.wait_until_el_xpath(self.main_management_agent_salesmen.xstdjlpryjp))
        self.main_management_agent_salesmen.select_dismissal()
        info("切换“营销团队经理解聘”页面")
        self.main_management_agent_salesmen.switch_to_window()
        self.main_management_agent_salesmen.maximize_window()
        info("选择需要解聘的员工并获取归属团队代码")
        group_id = self.dismissal_manager.select_by_user_code(user_code)
        info("解聘保存")
        self.dismissal_manager.prepare_save()
        get_screenshot("营销团队经理解聘保存")
        self.dismissal_manager.prepare_save_close()
        #  切换到查询页面
        self.main_management_agent_salesmen.switch_to_window()
        self.main_management_agent_salesmen.select_frame_id(self.main_management_agent_salesmen.frame_id)
        self.main_management_agent_salesmen.select_frame_id(self.main_management_agent_salesmen.iframe_page)
        self.main_management_agent_salesmen.set_table_num(3)
        self.main_management_agent_salesmen.query(user_code)
        info("选择数据")
        row = self.main_management_agent_salesmen.select_by_user_code(user_code)
        text = self.main_management_agent_salesmen.get_cell_text_by_head("状态", row)
        self.main_management_agent_salesmen.assertEqual("判断状态列的值为”经理解聘“", text, "经理解聘")
        get_screenshot("营销团队经理解聘查询")
        info("进入“营销团队经理解聘”页面")
        self.main_management_agent_salesmen.click(
            self.main_management_agent_salesmen.wait_until_el_xpath(self.main_management_agent_salesmen.xstdjlpryjp))
        info("切换“营销团队经理解聘”页面")
        self.dismissal_manager.switch_to_window()
        self.dismissal_manager.maximize_window()
        info("选择需要解聘的员工")
        self.dismissal_manager.select_by_user_code(user_code)
        info("解聘保存并提交")
        self.dismissal_manager.save_submit()
        self.dismissal_manager.switch_iframe_Reviewer()
        self.dismissal_manager.submit_close()
        #  切换到查询页面
        self.main_management_agent_salesmen.switch_to_window()
        self.main_management_agent_salesmen.select_frame_id(self.main_management_agent_salesmen.frame_id)
        self.click(self.wait_until_el_xpath(self.jyjg))
        self.execute_script("arguments[0].style.visibility='visible';", self.wait_until_el_xpath(self.menu_list))
        self.click(self.wait_until_el_xpath(self.dlzxsrydmgl))
        self.main_management_agent_salesmen.select_frame_id(self.main_management_agent_salesmen.iframe)
        self.main_management_agent_salesmen.query(user_code, status='1')
        self.main_management_agent_salesmen.set_table_num(1)
        text = self.main_management_agent_salesmen.get_cell_text_by_head("状态", row)
        self.main_management_agent_salesmen.assertEqual("判断状态列的值为”经理解聘复核“", text, "经理解聘复核")

    # @pytest.mark.usefixtures("login_jiangsu_p")
    # def test_YLDLZ_005_(self, user_code):   # 复核

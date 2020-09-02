#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:05
# @Author: fyl
# @File : test_SALES_YLZJ_011.py    中介模块>>渠道类型码作废
import allure
import pytest

from config.global_var import sleep
from src.page.agency_module.agency_module_page.channel_type_cancel import ChannelTypeCancel
from src.page.agency_module.agency_module_page.channel_type_code_approval import ChannelTypeCodeApproval
from src.page.agency_module.main_channel_type_code_approval import MainChannelTypeCodeApproval
from src.page.agency_module.main_channel_type_code_query import MainChannelTypeCodeQuery
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_011.csv")


@allure.feature("中介模块>>渠道类型码作废-011")
@pytest.mark.parametrize("channel,agent_type,agent_type_name", data, scope="class")
class Test_SALES_YLZJ_011():
    CTC = ChannelTypeCancel()
    MCTCA = MainChannelTypeCodeApproval()
    CTCA = ChannelTypeCodeApproval()
    MCTCQ = MainChannelTypeCodeQuery()

    @allure.story("渠道类型码作废")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_h_fun", "restore_data")
    def test_001(self, channel, agent_type, agent_type_name):
        self.CTC.switch_to_default_content()
        info("中介模块>>渠道类型码作废:{}".format(channel))
        info("渠道类型码作废页")
        self.CTC.into_page(channel)
        info("查询")
        self.CTC.query(agent_type)
        info("选择数据")
        self.CTC.select_data("渠道类型码名称", agent_type_name, "操作")
        self.CTC.switch_max_window()
        info("作废")
        self.CTC.click(self.CTC.wait_until_el_xpath(self.CTC.cancel_agent_type))
        if not self.CTC.alert_is_present():
            text = self.CTC.get_text(self.CTC.get_element_xpath(self.CTC.save_success))
            self.CTC.assertResult("验证提交成功", "保存成功!" in text)
            get_screenshot("渠道类型码作废-{}".format(channel))
            self.CTC.close_button_ty()
            self.MCTCA.switch_to_window()
            info("渠道类型码作废-审核")
            info("渠道类型码审核页")
            self.MCTCA.into_page(channel)
            info("输入渠道类型码查询")
            self.MCTCA.query(agent_type, status="001")
            info("选择数据")
            self.MCTCA.select_data("渠道类型码名称", agent_type_name, "操作")
            self.MCTCA.switch_max_window()
            info("渠道类型码审核页")
            self.CTCA.send_keys(self.CTCA.wait_until_el_xpath(self.CTCA.reason), "作废{}码-ui测试".format(channel))
            info("审核")
            self.CTCA.click(self.CTCA.wait_until_el_xpath(self.CTCA.pass_check))
            text = self.CTCA.get_text(self.CTCA.get_element_xpath(self.CTCA.save_success))
            self.CTCA.assertResult("验证保存成功", "保存成功!" in text)
            get_screenshot("渠道类型码作废审核-{}".format(channel))
            self.CTCA.close_button_ty()
            info("渠道类型码作废-验证")
            self.MCTCQ.switch_to_window()
            info("渠道类型码查询页")
            self.MCTCQ.into_page(channel)
            info("查询")
            self.MCTCQ.send_keys(self.MCTCQ.wait_until_el_xpath(self.MCTCQ.agent_type), agent_type)
            self.MCTCQ.click_btn("查询")
            info("验证")
            text = self.MCTCQ.get_cell_text_by_head("当前状态", 0)
            self.MCTCQ.assertEqual("验证状态是否有效", text, "作废审核通过")
            get_screenshot("渠道类型码作废验证-{}".format(channel))
        else:
            text = self.CTC.get_alert_text()
            info(text)
            self.CTC.assertResult("判断提示信息", "不允许作废" in text)
            get_screenshot("渠道类型码作废提示-{}".format(channel))
        sleep(2)

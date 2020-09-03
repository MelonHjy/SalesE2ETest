#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:05
# @Author: fyl
# @File : test_SALES_YLZJ_010.py    中介模块>>渠道类型码修改
import allure
import pytest

from config.global_var import sleep
from src.page.agency_module.agency_module_page.channel_type_code_approval import ChannelTypeCodeApproval
from src.page.agency_module.agency_module_page.edit_channel_type_code import EditChannelTypeCode
from src.page.agency_module.agency_module_page.new_channel_type_code import NewChannelTypeCode
from src.page.agency_module.main_channel_type_code_approval import MainChannelTypeCodeApproval
from src.page.agency_module.main_channel_type_code_edit import MainChannelTypeCodeEdit
from src.page.agency_module.main_channel_type_code_query import MainChannelTypeCodeQuery
from src.utils import csv_util
from src.utils.except_util import get_screenshot
from src.utils.log import info

data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_010.csv")


@allure.feature("中介模块>>渠道类型码修改-010")
@pytest.mark.parametrize("channel,agent_type,agent_type_name,new_agent_type_name", data, scope="class")
class Test_SALES_YLZJ_010():
    MCTCE = MainChannelTypeCodeEdit()
    ECTC = EditChannelTypeCode()
    MCTCA = MainChannelTypeCodeApproval()
    CTCA = ChannelTypeCodeApproval()
    MCTCQ = MainChannelTypeCodeQuery()

    # ,
    #             ("银保渠道", "", "银保ui测试-011"),
    #             ("车商渠道", "211", "车商ui测试","555555555555555", "2025-12-12") 数据未准备
    @allure.story("渠道类型码修改")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p_fun","restore_data")
    def test_001(self, channel, agent_type, agent_type_name, new_agent_type_name):
        info("中介模块>>渠道类型码修改")
        info("渠道类型码修改页")
        self.MCTCE.into_page(channel)
        self.MCTCE.assertEqual("验证页面标签", self.MCTCE.get_head_text(), "渠道类型码修改")
        self.MCTCE.query(agent_type=agent_type)
        info("选择数据")
        self.MCTCE.select_data("渠道类型码名称", agent_type_name, "操作")
        self.MCTCE.switch_max_window()
        info("修改渠道类型码名称" + new_agent_type_name)
        self.ECTC.send_keys(self.ECTC.wait_until_el_xpath(self.ECTC.sap_agent_type_name), new_agent_type_name)
        self.ECTC.click(self.ECTC.wait_until_el_xpath(self.ECTC.full_name))
        info("保存")
        self.ECTC.click(self.ECTC.wait_until_el_xpath(self.ECTC.update_agent_type))
        text = self.ECTC.get_text(self.ECTC.get_element_xpath(self.ECTC.save_success))
        self.ECTC.assertResult("验证提交成功", "保存成功!" in text)
        get_screenshot("渠道类型码修改-{}".format(channel))
        self.ECTC.close_button_ty()

    @allure.story("渠道类型码修改-审核")
    @pytest.mark.usefixtures("login_jiangsu_h_fun")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    def test_002(self, channel, agent_type, agent_type_name, new_agent_type_name):
        info("渠道类型码审核")
        self.MCTCA.into_page(channel)
        self.MCTCA.assertEqual("验证页面标题", self.MCTCA.get_head_text(), "渠道类型码审核")
        info("输入渠道类型码查询")
        self.MCTCA.query(agent_type=agent_type, status="010")
        info("选择数据")
        self.MCTCA.select_data("渠道类型码名称", agent_type_name, "操作")
        info("渠道类型码审核页")
        self.MCTCA.switch_to_window()
        self.CTCA.assertEqual("验证页面标题", self.CTCA.get_head_text(), "渠道类型码审核")
        self.CTCA.send_keys(self.CTCA.wait_until_el_xpath(self.CTCA.reason), "修改{}渠道码-ui测试".format(channel))
        info("审核")
        self.CTCA.click(self.CTCA.wait_until_el_xpath(self.CTCA.pass_check))
        text = self.CTCA.get_text(self.CTCA.get_element_xpath(self.CTCA.save_success))
        self.CTCA.assertResult("验证保存成功", "保存成功!" in text)
        get_screenshot("渠道类型码修改审核-{}".format(channel))
        self.CTCA.close_button_ty()
        self.CTCA.switch_to_window()
        info("渠道类型码新增-验证")
        info("渠道类型码查询页")
        self.MCTCQ.into_page(channel)
        self.MCTCQ.send_keys(self.MCTCQ.wait_until_el_xpath(self.MCTCQ.agent_type), agent_type)
        self.MCTCQ.click_btn("查询")
        info("验证")
        text = self.MCTCQ.get_cell_text_by_head("渠道类型码名称", 0)
        self.MCTCQ.assertEqual("验证是否修改有效", text, new_agent_type_name)
        get_screenshot("渠道类型码修改验证-{}".format(channel))
        sleep(2)

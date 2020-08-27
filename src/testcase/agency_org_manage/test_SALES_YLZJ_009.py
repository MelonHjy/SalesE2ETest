#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 21:05
# @Author: fyl
# @File : test_SALES_YLZJ_009.py    中介模块>>渠道类型码新增
import allure
import pytest

from src.page.agency_module.agency_module_page.channel_type_code_approval import ChannelTypeCodeApproval
from src.page.agency_module.agency_module_page.new_channel_type_code import NewChannelTypeCode
from src.page.agency_module.main_channel_type_code_approval import MainChannelTypeCodeApproval
from src.page.agency_module.main_channel_type_code_query import MainChannelTypeCodeQuery
from src.utils import csv_util

from src.utils.log import info

data = csv_util.data_reader("agency_org_manage/test_SALES_YLZJ_009.csv")

@allure.feature("中介模块>>渠道类型码新增")
@pytest.mark.parametrize("channel,agent_type_code,sap_agent_type_name,permit_no,date", data, scope="class")
class Test_SALES_YLZJ_009:
    NCTC = NewChannelTypeCode()
    MCTCA = MainChannelTypeCodeApproval()
    CTCA = ChannelTypeCodeApproval()
    MCTCQ = MainChannelTypeCodeQuery()
    msg = None

    @allure.story("渠道类型码新增")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_001(self, channel, agent_type_code, sap_agent_type_name, permit_no, date):
        info("中介模块>>渠道类型码新增:{}".format(channel))
        info("渠道类型码新增页")
        self.NCTC.into_page(channel)
        self.NCTC.assertEqual("验证页面标题", self.NCTC.get_head_text(), "渠道类型码新增")
        info("选择三级渠道类型码")
        self.NCTC.click_agent_type(agent_type_code)
        info("渠道类型码名称")
        self.NCTC.send_keys(self.NCTC.wait_until_el_xpath(self.NCTC.sap_agent_type_name), sap_agent_type_name)
        info("许可证机构编码")
        self.NCTC.send_keys(self.NCTC.wait_until_el_xpath(self.NCTC.permit_no), permit_no)
        info("许可证到期日")
        self.NCTC.pick_date_old(self.NCTC.img_btn1, date)
        info("保存")
        self.NCTC.click(self.NCTC.wait_until_el_xpath(self.NCTC.save_agent_type))
        text = self.NCTC.get_text(self.NCTC.get_element_xpath(self.NCTC.save_success))
        Test_SALES_YLZJ_009.msg = {"agent_type":text.split("：")[1]}
        self.NCTC.assertResult("验证提交成功", "保存成功!" in text)
        # self.NCTC.switch_to_default_content()

    @allure.story("渠道类型码新增-审核")
    @pytest.mark.dependency(name='test_002', depends=["test_001"])
    @pytest.mark.usefixtures("login_jiangsu_h_fun")
    def test_002(self, channel, agent_type_code, sap_agent_type_name, permit_no, date):
        info("渠道类型码审核")
        self.MCTCA.into_page(channel)
        self.MCTCA.assertEqual("验证页面标题", self.NCTC.get_head_text(), "渠道类型码审核")
        info("输入渠道类型码查询")
        self.MCTCA.query(agent_type=Test_SALES_YLZJ_009.msg["agent_type"])
        info("选择数据")
        self.MCTCA.select_data("渠道类型码名称", sap_agent_type_name, "操作")
        info("渠道类型码审核页")
        self.MCTCA.switch_to_window()
        self.NCTC.assertEqual("验证页面标题", self.NCTC.get_head_text(), "渠道类型码审核")
        self.CTCA.send_keys(self.CTCA.wait_until_el_xpath(self.CTCA.reason), "新增{}码-ui测试".format(channel))
        info("审核")
        self.CTCA.click(self.CTCA.wait_until_el_xpath(self.CTCA.pass_check))
        text = self.CTCA.get_text(self.CTCA.get_element_xpath(self.CTCA.save_success))
        self.CTCA.assertResult("验证保存成功", "保存成功!" in text)
        self.CTCA.close_button_ty()
        self.CTCA.switch_to_window()
        info("渠道类型码新增-验证")
        info("渠道类型码查询页")
        self.MCTCQ.into_page(channel)
        info("查询")
        self.MCTCQ.send_keys(self.MCTCQ.wait_until_el_xpath(self.MCTCQ.agent_type), Test_SALES_YLZJ_009.msg["agent_type"])
        self.MCTCQ.click_btn("查询")
        info("验证")
        text = self.MCTCQ.get_cell_text_by_head("当前状态", 0)
        self.MCTCQ.assertEqual("验证状态是否有效", text, "新增审核通过")
        # self.MCTCQ.switch_to_default_content()

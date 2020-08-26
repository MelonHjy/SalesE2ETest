#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 10:30
# @Author: fyl
# @File : test_SALES_YLZJ_004.py    中介机构>>中介机构新增和变更申报>>新增
import allure
import pytest

from src.page.agency_module.agency_module_page.new_agency_contract_approval import NewAgencyContractApproval
from src.page.agency_module.agency_module_page.new_agency_org import NewAgencyOrg
from src.page.agency_module.main_agency_org_approval import MainAgencyOrgApproval
from src.page.agency_module.main_agency_org_manage import MainAgencyOrgManage
from src.utils.log import info


@allure.feature("中介机构>>中介机构新增和变更申报>>新增")
class Test_SALES_YLZJ_004():
    MAOM = MainAgencyOrgManage()
    NAO = NewAgencyOrg()
    MAOA = MainAgencyOrgApproval()  # 审批
    NACA = NewAgencyContractApproval()  # 中介合同新增审批
    msg = None

    # data = [("个代渠道","保险兼业代理委托合同(外部)", "个人代理")]32019961--ui测试-中介机构,11003H100001--北京华通伟业汽车销售服务有限公司
    # RULE20120000000000001--保险经纪公司

    data = [("个代渠道", "交叉销售委托合同", "32990091--ui测试-006", "ui测试-中介004", "2020-08-21", "2022-12-30",
             "32003J200040--ui测试-中介01", "32000000--中国人民财产保险股份有限公司江苏省分公司", "RULE20120000000000001--保险经纪公司", "ui测试-中介004",
             "1111110", "交通银行", "新疆维吾尔自治区_伊犁哈萨克自治州", "交通银行股份有限公司伊宁辽宁路支行")]

    # ("经代渠道", "保险专业代理委托合同", "32990091--ui测试-006", "ui测试-中介经代004", "2020-08-21", "2022-12-30",
    #  "320021101770--ui测试-经代渠道", "32000000--中国人民财产保险股份有限公司江苏省分公司", "RULE20120000000000001--保险经纪公司",
    #  "ui测试-中介经代004", "1111112", "交通银行", "新疆维吾尔自治区_伊犁哈萨克自治州", "交通银行股份有限公司伊宁辽宁路支行")
    # ("银保渠道", "保险兼业代理委托合同(外部)", "32990091--ui测试-006", "ui测试-中介银保004", "2020-08-21", "2022-12-30",
    #  "32003J300157--ui测试-银保渠道", "32000000--中国人民财产保险股份有限公司江苏省分公司", "RULE20120000000000001--保险经纪公司",
    #  "ui测试-中介经代004", "1111114", "交通银行", "新疆维吾尔自治区_伊犁哈萨克自治州", "交通银行股份有限公司伊宁辽宁路支行")
    # ("车商渠道", "保险兼业代理委托合同(外部)", "32990091--ui测试-006", "ui测试-中介车商004-1", "2020-08-21", "2022-12-30",
    #  "32003L100008--ui测试-车商渠道", "32000000--中国人民财产保险股份有限公司江苏省分公司", "RULE20120000000000001--保险经纪公司",
    #  "ui测试-中介车商004", "1111116", "交通银行", "新疆维吾尔自治区_伊犁哈萨克自治州", "交通银行股份有限公司伊宁辽宁路支行")
    # @pytest.mark.skip
    @allure.story("中介机构新增")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize(
        "channel,contract_type,com_code,agent_name,contract_start,contract_end,sa_agent_code,sa_comCode,fee_rule_No,"
        "his_payee_name,his_account_no,sa_Account_bankName,bank_area,bank_Name", data)
    def test_001(self, channel, contract_type, com_code, agent_name, contract_start, contract_end, sa_agent_code,
                 sa_comCode, fee_rule_No, his_payee_name, his_account_no, sa_Account_bankName, bank_area, bank_Name):
        info("中介机构新增和变更申报页")
        self.MAOM.into_page(channel)
        info("中介机构新增页")
        self.MAOM.click_btn("新增")
        self.MAOM.switch_max_window()
        self.MAOM.assertEqual("判断页面标题", self.MAOM.get_head_text(), "编辑中介合同信息")
        info("填写申请信息")
        info("合同类型")
        self.NAO.select_type(contract_type)
        info("我司机构代码")
        self.NAO.double_click_org(self.NAO.com_code, com_code.split("--")[0])
        info("签约中介机构全称")
        self.NAO.send_keys(self.NAO.get_element_xpath(self.NAO.agent_name), agent_name)
        info("合同日期")
        self.NAO.contract_date(contract_start, contract_end)
        self.NAO.click(self.NAO.get_element_xpath(self.NAO.add_agent_contract_button))
        info("渠道码{}".format(sa_agent_code.split("--")[0]))
        text = sa_agent_code.split("--")[0]
        self.NAO.send_keys_(self.NAO.get_element_xpath(self.NAO.sa_agent_code.format("0")), text)
        info("我司专营机构/团队{}".format(sa_comCode.split("--")[0]))
        self.NAO.double_click_org(self.NAO.sa_comCode.format("0"), sa_comCode.split("--")[0])
        info("配置单号{}".format(fee_rule_No.split("--")[0]))
        self.NAO.send_keys_(self.NAO.get_element_xpath(self.NAO.fee_rule_No), fee_rule_No.split("--")[0])
        info("编辑银行账号")
        self.NAO.click(self.NAO.get_element_xpath(self.NAO.add_account.format('0')))
        self.NAO.switch_to_window()
        if self.NAO.get_head_text() == "银行账号编辑":
            info("添加银行账号")
            self.NAO.send_keys_(self.NAO.his_payee_name, his_payee_name)
            self.NAO.send_keys_(self.NAO.his_account_no, his_account_no)
            self.NAO.send_keys_(self.NAO.sa_Account_bankName, sa_Account_bankName)
            self.NAO.send_keys_(self.NAO.bank_area, bank_area)
            self.NAO.send_keys_(self.NAO.bank_Name, bank_Name)
            self.NAO.click(self.NAO.get_element_xpath(self.NAO.save_account))
            self.NAO.choose_ok_on_alert()
            self.NAO.switch_to_window()
        self.NAO.click(self.NAO.get_element_xpath(self.NAO.contract_submit))
        self.NAO.choose_ok_on_alert()
        self.NAO.submit_interaction(self.NAO.submit_iframe)
        text = self.NAO.get_text(self.NAO.get_element_xpath(self.NAO.save_success))
        self.NAO.assertResult("验证提交成功", "保存成功!" in text)
        Test_SALES_YLZJ_004.msg = {"channel": channel, "contract_type": contract_type, "contract_no": text.split("：")[1]}
        # 关闭
        self.NAO.close_button_ty()

    @allure.story("中介机构新增-审批")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.dependency(name='test_002', depend='test_001')
    def test_002(self):
        self.MAOA.switch_to_window()
        info("中介机构审批页")
        self.MAOA.into_page(Test_SALES_YLZJ_004.msg["channel"])
        info("查询合同号：{}".format(Test_SALES_YLZJ_004.msg["contract_no"]))
        self.MAOA.query(Test_SALES_YLZJ_004.msg["contract_no"])
        # self.MAOA.into_page("个代渠道")
        # info("查询合同号：{}".format("32013J220082000"))
        # self.MAOA.query("32013J220082000")
        info("选择数据")
        self.MAOA.select_data("新增审批")
        info("中介合同新增审批页")
        self.MAOA.switch_max_window()
        self.NACA.assertEqual("判断页面标题", self.NACA.get_head_text(), "中介合同新增审批")
        info("审批")
        self.NACA.click(self.NACA.get_element_xpath(self.NACA.pass_check))
        self.NACA.choose_ok_on_alert()
        info("提交任务")
        self.NACA.submit_interaction("中介机构新增-ui测试")
        text = self.NACA.get_text(self.NACA.get_element_xpath(self.NACA.save_success))
        self.NACA.assertResult("验证提交成功", "保存成功!" in text)
        self.NACA.close_button_ty()

    @allure.story("中介机构新增-验证")
    @pytest.mark.usefixtures("login_jiangsu_p")
    @pytest.mark.dependency(name='test_003', depend='test_001')
    def test_003(self):
        self.MAOM.switch_to_window()
        info("中介机构审批页")
        self.MAOM.into_page(Test_SALES_YLZJ_004.msg["channel"])
        info("查询合同号：{}".format(Test_SALES_YLZJ_004.msg["contract_no"]))
        self.MAOM.query(Test_SALES_YLZJ_004.msg["contract_no"], Test_SALES_YLZJ_004.msg["contract_type"], "1")
        # self.MAOM.into_page("个代渠道")
        # info("查询合同号：{}".format("32993J220082101"))
        # self.MAOM.query("32993J220082101")
        text = self.MAOM.get_cell_text_by_head("状态", 0)
        self.MAOM.assertEqual("验证机构是否有效", text, "有效")

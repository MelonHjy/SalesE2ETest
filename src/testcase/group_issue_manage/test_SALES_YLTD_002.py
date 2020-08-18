#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_002.py    团队出单权管理>>团队信息变更（无效的团队进行复效）
import allure
import pytest

from config.global_var import sleep
from src.page.group_issue_manage.main_group_issue_manage import MainGroupIssueManage
from src.page.group_issue_manage.main_group_issue_page.edit_group import EditGroup
from src.page.integrated_management.sales_group_recheck_page.edit_group_recheck import EditGroupRecheck
from src.utils.log import info



@allure.feature("团队出单权管理>>团队信息变更（无效的团队进行复效）")
class Test_SALES_YLTD_002():
    MGIM = MainGroupIssueManage()
    EG = EditGroup()
    EGR = EditGroupRecheck()
    msg = None

    data = [("32990088", "ui测试-002")]

    @allure.story("无效的团队进行复效")
    @pytest.mark.dependency(name='test_001')
    @pytest.mark.parametrize("pk_deptdoc, group_name", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_001(self, pk_deptdoc, group_name):
        Test_SALES_YLTD_002.msg = {"pk_deptdoc": pk_deptdoc, "group_name": group_name}
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
        self.EG.submit_interaction()

    @allure.story("无效的团队进行复效-审核")
    @pytest.mark.dependency(name='test_002', depends=['test_001'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_002(self):
        info("团队审核")
        self.MSG.into_page()
        info("查询团队名称：{}".format(Test_SALES_YLTD_002.msg["group_name"]))
        self.MSG.query(group_name=Test_SALES_YLTD_002.msg["group_name"])
        self.MSG.select_data(self.MSG.select_data("无效修改审核"))
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
        info("提示信息：{}".format(text))
        self.EGR.assertEqual("判断提示信息", text, "{}:团队信息推送成功！")
        self.EGR.choose_ok_on_alert()

    @allure.story("无效的团队进行复效-验证")
    @pytest.mark.dependency(name='test_003', depends=['test_001', 'test_002'])
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_003(self):
        info("团队出单权管理页")
        self.MGIM.into_page()
        info("查询团队名称：{}".format(Test_SALES_YLTD_002.msg["group_name"]))
        self.MGIM.query(group_name=Test_SALES_YLTD_002.msg["group_name"])
        # self.MGIM.query("ui测试-002")
        text = self.MGIM.get_cell_text_by_head("团队状态",0)
        self.MGIM.assertEqual("判断团队状态是否有效", text, "有效")
        process = self.MGIM.get_cell_text_by_head("终止流程", 0)
        self.MGIM.assertEqual("判断最后一栏没有终止流程按钮", process, "")

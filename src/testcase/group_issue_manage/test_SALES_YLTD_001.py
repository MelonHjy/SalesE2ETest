#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:47
# @Author: fyl
# @File : test_SALES_YLTD_001.py    团队出单权管理>>新增团队
import allure
import pytest

from src.page.group_issue_manage.group_declare import GroupDeclare
from src.page.group_issue_manage.main_group_issue_manage import MainGroupIssueManage
from src.utils.log import info


@allure.feature("团队出单权管理>>新增团队")
class Test_SALES_YLTD_001():
    MGIM = MainGroupIssueManage()
    GD = GroupDeclare()

    data = [("ui测试-001", "32000000--中国人民财产保险股份有限公司江苏省分公司", "营销团队", "其他--营销", "2020-09-30")]

    @allure.story("团队申报")
    @pytest.mark.parametrize("group_name,com_code,group_type,business_name,build_date", data)
    @pytest.mark.usefixtures("login_jiangsu_p_fun")
    def test_001(self, group_name, com_code, group_type, business_name, build_date):
        info("进入团队出单权管理页")
        self.MGIM.into_page()
        info("进入新增团队页")
        self.MGIM.click_btn("新增团队")
        self.MGIM.switch_max_window()
        # self.MGIM.open_url("http://10.10.1.104:8001/sales/group/addOrUpdateGroup.do?status=add")
        info("团队申报页")
        self.GD.assertEqual("判断页面标题", self.GD.get_head_text(), "团队申报")
        info("团队名称：{}".format(group_name))
        self.GD.input_group_name(group_name)
        info("上级机构：{}".format(com_code))
        self.GD.code_select(self.GD.com_code, com_code)
        info("团队属性：{}".format(group_type))
        self.GD.select(self.GD.grouptype1, group_type)
        info("团队主营业务分类：{}".format(business_name))
        self.GD.code_select(self.GD.business_name, business_name)
        info("团队组建如期：{}".format(build_date))
        self.GD.pick_date_old(self.GD.img_Btn, build_date)
        info("保存并提交")
        self.GD.click(self.GD.submit_btn)

#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 2:14
# @Author: fyl
# @File : group_declare.py  团队申报
import allure

from src.page.group_issue_manage.main_group_issue_page.group_issue_manage_common import GroupIssueManageCommon


class GroupDeclare(GroupIssueManageCommon):
    case = "//*[@class='case']"
    group_name = "//*[@id='groupName']"  # 团队名称
    com_code = "//*[@id='comCode']"  # 上级机构
    grouptype1 = "//*[@id='grouptype1']"  # 团队属性
    business_name = "//*[@id='businessName']"  # 团队主营业务分类
    img_Btn = "//*[@id='imgBtn']"  # 团队组建日期
    submit_btn = "*[@id='buttonA']"  # 保存并提交

    @allure.step("输入团队名:{group_name}")
    def input_group_name(self, group_name):
        self.send_keys(self.get_element_xpath(self.group_name), group_name)

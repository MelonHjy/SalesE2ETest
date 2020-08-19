#  -*- coding:utf-8 -*-
# @Time : 2020/8/18 1:14
# @Author: fyl
# @File : group_view.py 团队查看
from src.page.group_issue_manage.main_group_issue_page.group_issue_manage_common import GroupIssueManageCommon


class GroupView(GroupIssueManageCommon):

    group_type = "//*[@id='saGroup.grouptype']" # 团队类型
    business_name = "//*[@id='businessName']"   # 团队主营业务分类
    business_focus = "//*[@id='businessFocus']" # 业务发展重点
    business_desc = "//*[@id='businessDesc']"   # 业务发展重点描述
    build_date = "//div[@id='container']/table/tbody/tr[4]/td[4]"   # 团队组建日期

    def get_group_type(self):
        return self.get_text(self.get_element_xpath(self.group_type))

    def get_business_focus(self):
        return self.get_text(self.get_element_xpath(self.business_focus))

    def get_build_date(self):
        return self.get_text(self.get_element_xpath(self.build_date))

    def get_business_name(self):
        return self.get_attribute(self.get_element_xpath(self.business_name),'value')

    def get_business_desc(self):
        return self.get_attribute(self.get_element_xpath(self.business_desc),'value')
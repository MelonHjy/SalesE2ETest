#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 2:14
# @Author: fyl
# @File : group_declare.py  团队申报
import allure

from src.page.process_page import ProcessPage


class GroupDeclare(ProcessPage):
    case = "//*[@class='case']"
    group_name = "//*[@id='groupName']"  # 团队名称
    com_code = "//*[@id='comCode']"  # 上级机构
    grouptype1 = "//*[@id='grouptype1']"  # 团队属性
    business_name = "//*[@id='businessName']"  # 团队主营业务分类
    img_Btn = "//*[@id='imgBtn']"  # 团队组建日期
    submit_btn = "*[@id='buttonA']"  # 保存并提交
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def get_head_text(self):
        return self.get_text(self.get_element_xpath(self.case))

    @allure.step("输入团队名:{group_name}")
    def input_group_name(self, group_name):
        self.send_keys(self.get_element_xpath(self.group_name), group_name)

#  -*- coding:utf-8 -*-
# @Time : 2020/8/27 16:11
# @Author: fyl
# @File : commission_edit.py
from src.page.agency_module.agency_module_page.common_page import CommonPage


class CommissionEdit(CommonPage):
    rule_name = "//*[@name='rulename']"
    commission = "//*[@name='feeRangeHistoryList[0].maxrate']"
    submit = "//*[contains(@value,'提交审核')]"

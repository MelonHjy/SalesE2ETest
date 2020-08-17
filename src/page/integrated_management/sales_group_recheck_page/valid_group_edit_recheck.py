#  -*- coding:utf-8 -*-
# @Time : 2020/8/17 19:06
# @Author: fyl
# @File : valid_group_edit_recheck.py
from src.page.integrated_management.sales_group_recheck_page.sales_group_recheck_common import SalesGroupRecheckCommon


class ValidGroupEditRecheck(SalesGroupRecheckCommon):

    submit_btn = "//*[@id='addFarm']"  # 非重要信息审核按钮
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
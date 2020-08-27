#  -*- coding:utf-8 -*-
# @Time : 2020/8/27 16:57
# @Author: fyl
# @File : commission_approval.py    佣金配置修改审核
from src.page.agency_module.agency_module_page.common_page import CommonPage


class CommissionApproval(CommonPage):
    check_pass = "//*[@id='checkPass']"
    reason = "//*[@id='saDFeeRangeHistory.auditnotion']"
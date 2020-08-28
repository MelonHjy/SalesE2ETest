#  -*- coding:utf-8 -*-
# @Time : 2020/8/20 14:16
# @Author: fyl
# @File : new_agency_org.py  中介机构合同续签
from config.global_var import sleep
from src.page.agency_module.agency_module_page.common_page import CommonPage


class AgencyContractRenew(CommonPage):

    imgBtn1 = "//*[@id='imgBtn{}']"  # 合同日期控件
    renew_submit = "//*[@id='renewSubmit']"  # 保存并提交
    name = "//*[@id='Name']"  # 账号名


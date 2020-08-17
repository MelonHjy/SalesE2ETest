#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 19:17
# @Author: fyl
# @File : sales_group_recheck.py
from src.page.process_page import ProcessPage


class SalesGroupRecheck(ProcessPage):

    recheck_btn = "//*[@id='toHRFarm']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功


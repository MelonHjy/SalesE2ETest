# -*- coding:utf-8 -*-
# @Time : 2020/6/30 15:01
# @Author: zyb
# @File : appointment_and_dismissal.py 营销团队经理聘任与解聘
import allure

from config.global_var import sleep
from src.page.base_page import BasePage


class DeputyRecheck(BasePage):
    # frame
    frame_id = 'main'
    iframe = "//iframe[@name='page']"
    #复核按钮
    recheck = "//input[@id='success']"
    # 提交任务的iframe
    # submit_iframe = "//div[@id='submitDlg']/iframe[@name='submitFrame']"
    # submit_iframe = "//div[@id='submitDlg']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功
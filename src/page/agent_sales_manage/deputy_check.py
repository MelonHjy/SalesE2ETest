# -*- coding:utf-8 -*-
# @Time : 2020/6/30 15:01
# @Author: zyb
# @File : appointment_and_dismissal.py 营销团队经理聘任与解聘
import allure

from config.global_var import sleep
from src.page.base_page import BasePage


class DeputyCheck(BasePage):
    # frame
    frame_id = 'main'
    # 销售团队经理聘任与解聘
    xstdjlpryjp = "//input[@value='营销团队经理聘任与解聘']"
    # iframe->营销团队经理聘任与解聘
    iframe = "//iframe[@name='page']"
    #注销按钮
    dismiss = "//input[@id='dismiss']"
    # 提交任务的iframe
    submit_iframe = "//iframe[@name='submitFrame']"
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功
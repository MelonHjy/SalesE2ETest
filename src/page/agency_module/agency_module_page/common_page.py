#  -*- coding:utf-8 -*-
# @Time : 2020/8/24 16:29
# @Author: fyl
# @File : common_page.py
from src.page.process_page import ProcessPage


class CommonPage(ProcessPage):
    case = "//*[@class='case']"
    pass_check = "//*[@id='passCheck']"
    submit_frame = "//iframe[@name='submitFrame']"  # 提示聘任的提示框iframe
    save_success = "//body/table/tbody/tr/td[2]"    # 保存成功

    def get_head_text(self):
        return self.get_text(
            self.get_element_xpath(self.case))


#  -*- coding:utf-8 -*-
# @Time : 2020/7/21 17:16
# @Author: fyl
# @File : dismissal_manager.py
from src.page.process_page import ProcessPage
from src.page.table_page import TablePage


class DismissalManager(TablePage, ProcessPage):
    prepare_save_btn = "//input[@id='preparesavedeputy2']"  # 解聘保存
    prepare_save_close_btn = "//input[@class='button_ty']"  # 解聘保存后关闭按钮
    save_submit_btn = "//input[@id='savedeputy2']"
    submit_iframe = "//iframe[@name='submitFrame']"  # 提交任务的iframe
    submit_close_btn = "//table/tbody/tr[2]/td/input"  # 提交任务后的关闭按钮

    def select_by_user_code(self, user_code):
        """
        选择需要解聘的员工并返回归属团队代码
        """
        list = self.get_cell_text_by_head('内部流转码')
        index = list.index(user_code)
        self.click(self.get_radio_by_head(index, '选择'))
        return self.get_cell_text_by_head("归属团队代码", index)

    def prepare_save(self):
        """
        解聘保存
        """
        self.click(self.wait_until_el_xpath(self.prepare_save_btn))
        self.choose_ok_on_alert()

    def prepare_save_close(self):
        """
        解聘保存后关闭窗口
        """
        self.click(self.wait_until_el_xpath(self.prepare_save_close_btn))

    def save_submit(self):
        """
        解聘保存并提交
        """
        self.click(self.wait_until_el_xpath(self.save_submit_btn))
        self.choose_ok_on_alert()

    def switch_iframe_reason(self, textarea="", ):
        """
        切换iframe并填写审核人，提交任务并关闭窗口
        """
        self.submit_interaction(textarea=textarea, iframe_xpath=self.submit_iframe)
        self.click(self.wait_until_el_xpath(self.submit_close_btn))

#  -*- coding:utf-8 -*-
# @Time : 2020/7/24 10:35
# @Author: fyl
# @File : process_page.py
from src.page.base_page import BasePage
from src.utils.log import info


class ProcessPage(BasePage):

    # ------------------------  流程流转元素 ------------------------#

    now_node = "//*[contains(text(), '当前环节')]/../td[2]"
    textarea = "//textarea"
    submit = "//*[@value='提交任务']"
    state = "//option[contains(text(), '通过')]/.."
    next = "//option[contains(text(), '打回')]/.."

    def submit_interaction(self, iframe_xpath, check_state="", next_node="", textarea=""):
        """
        下拉菜单、打回岗位（关键字通过）、审核意见、失败原因
        iframe:frame的name属性值
        check_state:是否通过
        next_node：打回
        textarea：文本框
        """
        self.select_frame_id(self.wait_until_el_xpath(iframe_xpath))
        text = self.get_text(self.wait_until_el_xpath(self.now_node))
        info("当前环节：{}".format(text))
        if self.is_element_exist(self.state) and check_state != "":
            self.select(self.state, check_state)
            info("选择：{}".format(check_state))
        if self.is_element_exist(self.next) and next_node != "":
            self.select(self.next, next_node)
            info("选择：{}".format(next_node))
        # textarea输入框
        if self.is_element_exist(self.textarea):
            self.send_keys(self.wait_until_el_xpath(self.textarea), textarea)
            info("textarea：{}".format(textarea))
        self.click(self.wait_until_el_xpath(self.submit))
        info("提交任务")

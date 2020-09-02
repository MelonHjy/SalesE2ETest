# -*- coding: utf-8 -*-#
import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from config.global_var import *
from src.utils.driver_util import set_wait
from src.utils.except_util import catch_except
from src.utils.high_light_element import high_light
from src.utils.log import *


class BasePage:
    # ------------------------  菜单 ------------------------#
    frame_id = 'main'
    iframe_page = "page"
    module_menu = "//a[contains(text(), '{}')]/.."  # 模块
    zk_menu = "//div[@id='{0}']/div/div/div/div/table/tbody/tr/td[2]/a[text()='{1}']/../../td[1]"  # 展开菜单

    # menu = "//a[text()='{}']"  # 选择菜单名
    menu = "//div[@id='{0}']/div/div/div/div/div/div/table/tbody/tr/td[3]/a[text()='{1}']"
    menu_list = "//*[@id='{}']"

    # ------------------------  日期控件 ------------------------#
    # 新日期控件
    year_input_new = "//div[@class='menuSel YMenu']/following-sibling::input"
    month_input_new = "//div[@class='menuSel MMenu']/following-sibling::input"
    month_select = "//div[@class='menuSel MMenu']/table/tbody/tr/td[text()='{0}']"
    day_select_new = "//table[@class='WdayTable']/tbody/tr/td[text()='{0}']"
    date_iframe = "//div[@skin='default']/iframe"
    Month = {1: '一月', 2: '二月', 3: '三月', 4: '四月', 5: '五月', 6: '六月', 7: '七月', 8: '八月', 9: '九月', 10: '十月', 11: '十一',
             12: '十二'}

    # 旧日期控件
    year_select_old = "//select[@id='tbSelYear']"
    month_select_old = "//select[@id='tbSelMonth']"
    day_select_old = "//font[@id='cellText' and text()='{0}']"

    # ------------------------  常用操作封装 ------------------------#

    @allure.step("{module_menu}->{zk_menu}->{menu}")
    def to_main_page(self, module_menu, zk_menu, menu):
        """
        选择菜单进入功能页面
        module_menu：模块名
        zk_menu：需要展开菜单的菜单名
        menu：最终菜单名
        """
        # 取消main页面的onbeforeunload
        self.execute_script("window.onbeforeunload = null;")

        self.select_frame_id(self.frame_id)
        _module_menu = self.wait_until_el_xpath(self.module_menu.format(module_menu))
        self.click(_module_menu)
        sleep(2)
        menu_list_id = self.get_attribute(_module_menu, 'onmouseover').split("'")[1]
        # _menu_list = self.menu_list.format(menu_list_id)
        script = "window.parent.document.getElementById('{0}').contentWindow.document.getElementById('{1}').style.visibility='{2}';"
        visible_script = script.format(self.frame_id, menu_list_id, 'visible')
        hidden_script = script.format(self.frame_id, menu_list_id, 'hidden')
        self.execute_script(visible_script)
        # self.execute_script("arguments[0].style.visibility='visible';", self.wait_until_el_xpath(_menu_list))

        if not self.is_element_exist(self.menu.format(menu_list_id, menu)):
            self.click(self.wait_until_el_xpath(self.zk_menu.format(menu_list_id, zk_menu)))
        sleep(2)
        self.execute_script(visible_script)
        # self.execute_script("arguments[0].style.visibility='visible';", self.wait_until_el_xpath(_menu_list))

        self.click(self.wait_until_el_xpath(self.menu.format(menu_list_id, menu)))
        self.execute_script(hidden_script)
        # self.execute_script("arguments[0].style.visibility='hidden';", self.wait_until_el_xpath(_menu_list))
        self.select_frame_id(self.iframe_page)

    def back_to_page(self):
        self.switch_to_window()
        self.select_frame_id(self.frame_id)
        self.select_frame_id(self.iframe_page)

    # 页面切换
    def switch_to_first_iFrame(self, first_iFrame_id):
        """
        切换第一层iFrame
        first_iFrame_id：第一层iframe的id
        """
        self.switch_to_default_content()
        self.select_frame_id(first_iFrame_id)

    handles = []

    def switch_to_window(self, num=-1):
        time.sleep(4)
        # if not self.handles:
        # current = g.driver.current_window_handle
        new = []
        for i in range(5):
            new = self.get_handles()
            print(new)
        info('3333333333333')
        self.handles = self.update_handles(self.handles, new)
        info('4444444444444')
        self.switch_to_win(self.handles[num])

    def update_handles(self, old, new):
        a = []
        for i in old:
            for j in new:
                if i == j:
                    a.append(i)
                    new.remove(j)
                    continue
        a.extend(new)
        return a

    def code_select(self, xpath, text):
        '''
        xpath:要双击组件的xpath
        text:要选择的文本值
        '''

        self.double_click(self.wait_until_el_xpath(xpath))
        sleep(2)
        info('aaaaaaaaaaaaa0')
        self.switch_to_window()
        info('aaaaaaaaaaaaa1')
        # 取消选择页面的onbeforeunload
        self.execute_script("window.onbeforeunload = null;")
        info('aaaaaaaaaaaaa2')
        option = self.wait_until_el_xpath("//select/option[contains(@value,'{0}')]".format(text.split('--')[0]))
        info('aaaaaaaaaaaaa3')
        self.click(option)
        info('aaaaaaaaaaaaa4')
        confirm = self.wait_until_el_xpath("//input[@value='确定']")
        self.click(confirm)
        sleep(2)
        self.switch_to_window()


    def code_select_input(self, xpath, text):
        '''
        双击选择框，使用输出实现
        xpath:要双击组件的xpath
        text:要选择的文本值
        '''
        self.send_keys(self.wait_until_el_xpath(xpath), text.split('--')[0])
        sleep(2)

    def js_set_value(self, xpath, value):
        """
        通过js设置标签内value的值
        """
        self.execute_script_s("arguments[0].setAttribute('value',arguments[1]);",
                              self.get_element_xpath(xpath), value)

    def js_group(self, group_code_xpath, group_name_xpath, org, group_code_hold_xpath=None, group_code_hold=None):
        """
        一组双击组件选择的步骤
        group_code_xpath:机构代码xpath
        group_name_xpath：机构名称的xpath
        org：机构值
        group_code_hold_xpath：机构隐藏域xpath
        group_code_hold：机构隐藏域的值
        """
        self.js_set_value(group_code_xpath, org.split('--')[0])
        self.js_set_value(group_name_xpath, org.split('--')[1])
        if group_code_hold:
            self.js_set_value(group_code_hold_xpath, group_code_hold)

    @catch_except
    def select(self, xpath, text):
        '''
        针对select-option组件
        xpath:
        '''
        select_ele = Select(g.driver.find_element_by_xpath(xpath))
        select_ele.select_by_visible_text(text)
        sleep(1)

    @catch_except
    def select_by_value(self, xpath, text):
        '''
        针对select-option组件
        xpath:
        '''
        select_ele = Select(g.driver.find_element_by_xpath(xpath))
        select_ele.select_by_value(text)
        sleep(1)

    # 身份证倒数第二位，奇数为男，偶数为女
    def get_sex_by_idCard(self, idCard):
        return '男' if int(idCard[-2]) % 2 == 1 else '女'

    def get_birthday_by_idCard(self, idCard):
        return idCard[6:14]

    def pick_date_simple(self, xpath, date):
        el = self.wait_until_el_xpath(xpath)
        self.execute_script_s("arguments[0].removeAttribute(arguments[1]);",
                              el, 'readOnly')
        sleep(1)
        self.execute_script("arguments[0].focus();", el)
        self.send_keys(el, date)

    def pick_date_new(self, xpath, date):
        self.click(self.wait_until_el_xpath(xpath))

        iframe = g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.date_iframe)))
        self.select_frame_id(iframe)
        year, month, day = date.split('-')
        # d = self.wait_until_el_xpath("//div[@class='WdateDiv']")
        # 选择年
        y = self.wait_until_el_xpath(self.year_input_new)
        self.click(y)
        y.send_keys(Keys.BACK_SPACE)
        self.send_keys(y, str(int(year)))
        # 选择月
        self.click(self.wait_until_el_xpath(self.month_input_new))
        self.click(self.wait_until_el_xpath(self.month_select.format(self.Month.get(int(month)))))
        # 选择日
        days = self.wait_until_els_xpath(self.day_select_new.format(int(day)))
        day_select = days[1] if len(days) > 1 and int(day) in range(23, 32) else days[0]
        self.click(day_select)

        self.switch_to_default_content()

    def pick_date_old(self, xpath, date):
        el = self.wait_until_el_xpath(xpath)
        self.click(el)

        year, month, day = date.split('-')
        # 选择月
        self.select_by_value(self.month_select_old, str(int(month)))
        # 选择年
        self.select_by_value(self.year_select_old, year)
        # 选择日
        days = self.wait_until_els_xpath(self.day_select_old.format(int(day)))
        day_select = days[1] if len(days) > 1 and int(day) in range(23, 32) else days[0]
        self.click(day_select)

    # ------------------------  同名api ------------------------#

    @catch_except
    def click(self, el):
        """
        单击
        param el:元素
        """
        sleep(0.5)
        el.click()

    @catch_except
    def wait_until_el_xpath(self, xpath):
        """
        显示等待定位单个元素
        xpath：
        return:el
        """
        el = g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        high_light(element=el)
        sleep(0.5)
        return el

    @catch_except
    def wait_until_els_xpath(self, xpath):
        """
        显示等待定位多个元素
        xpath：
        return:el列表
        """
        return g.wait.until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))

    def close_browser(self):
        """
        关闭浏览器
        """
        sleep(0.5)
        g.driver.quit()
        try:
            if self.alert_is_present():
                self.choose_ok_on_alert()
        except Exception as e:
            pass

    @catch_except
    def close_tab(self):
        """
        关闭浏览器
        """
        sleep(0.5)
        g.driver.close()

    @catch_except
    def choose_ok_on_alert(self):
        """
        获取alert弹框并点击确定
        xpath：
        """
        sleep(3)
        alter = g.driver.switch_to.alert
        sleep(3)
        alter.accept()
        sleep(1)

    @catch_except
    def get_alert_text(self):
        """
        获取alert弹框并的文本信息
        """
        sleep(2)
        text = g.driver.switch_to.alert.text
        return text

    @catch_except
    def claer(self, el):
        el.clear()

    @catch_except
    def send_keys(self, el, value, clear=True):
        """
        向el元素填写文本
        el:元素
        value：文本值
        """
        if clear:
            el.clear()
        el.send_keys(value)

    @set_wait(1)
    def is_element_exist(self, xpath):
        """
        判断元素是否存在
        xpath:
        """
        try:
            el = g.wait.until(
                expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
            high_light(element=el)
            return True
        except BaseException:
            return False

    @catch_except
    def get_text(self, el):
        """
        获取元素文本信息
        el:元素
        """
        return el.text

    @catch_except
    def get_element_xpath(self, xpath):
        """
        定位单个元素（无显示等待）
        xpath:
        """
        el = g.driver.find_element_by_xpath(xpath)
        high_light(element=el)
        return el

    @catch_except
    def right_click(self, xpath):
        """
        右击
        xpath:
        """
        right_click = g.driver.find_element_by_xpath(xpath)
        high_light(element=right_click)
        ActionChains(g.driver).context_click(right_click).perform()

    @catch_except
    def open_url(self, url):
        """
        打开url
        url:
        """
        g.driver.get(url)
        handles = g.driver.window_handles
        g.driver.switch_to.window(handles[-1])

    @catch_except
    def double_click(self, double_click_el):
        """
        双击元素
        double_click_el:元素
        """
        ActionChains(g.driver).double_click(double_click_el).perform()

    @catch_except
    def move_to_el(self, el):
        """
        移动到指定元素位置
        el:元素
        """
        webdriver.ActionChains(g.driver).move_to_element(el).perform()
        # webdriver.ActionChains(g.driver).click_and_hold(el).perform()
        sleep(1)

    @catch_except
    def switch_to_default_content(self):
        """
        切换到主页面
        """
        g.driver.switch_to.default_content()

    @catch_except
    def select_frame_id(self, id):
        """
        切换到指定id的frame上
        id：
        """
        g.driver.switch_to.frame(id)

    @catch_except
    def switch_parent_frame(self):
        g.driver.switch_to.parent_frame()

    @catch_except
    def maximize_window(self):
        """
        窗口最大化
        """
        g.driver.maximize_window()

    @catch_except
    def execute_script(self, js, *el):
        """
        通过js操作元素
        el：
        """
        g.driver.execute_script(js, *el)

    @catch_except
    def execute_script_s(self, js, el, value):
        """
        通过js改变元素属性，多用于style里面的值
        el：元素
        value：需要修改的值
        """
        g.driver.execute_script(js, el, value)

    @catch_except
    def get_select(self, el):
        """
        获取下拉框对象
        el：元素
        """
        return Select(el)

    @catch_except
    def get_attribute(self, el, att_name):
        """
        获取元素的属性值
        el：元素
        att_name：属性名
        """
        return el.get_attribute(att_name)

    @catch_except
    def get_handles(self):
        """
        获取所有窗口的句柄
        return：句柄列表
        """
        return g.driver.window_handles

    @catch_except
    def switch_to_win(self, handle):
        """
        切换指定句柄的窗口
        """
        g.driver.switch_to.window(handle)

    def alert_is_present(self):
        """
        判断是否存在提示框
        """
        try:
            sleep(1)
            alert = g.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    # ------------------------  assert api ------------------------#

    # 断言方法
    def assertEqual(self, message, actual, expect):
        pytest.assume(actual == expect)
        info('message-->{0},actual-->{1},expect-->{2},result-->{3}'.format(message, actual, expect, actual == expect))

    def assertResult(self, message, result):
        pytest.assume(result)
        info('message-->{0},result-->{1}'.format(message, result))

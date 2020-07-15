# -*- coding: utf-8 -*-#
import pytest
from selenium import webdriver
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

    # 三农模块
    snmk = "//li[@class='m1_4']/a[text()='三农模块']"
    # 经营机构模块
    jyjg = "//li[@class='m1_4']/a[text()='经营机构']"
    # 直销渠道模块
    zxqd = "//li[@class='m1_4']/a[text()='直销渠道']"
    # 个代渠道模块
    gdqd = "//li[@class='m1_4']/a[text()='个代渠道']"
    # 农村保险事业部模块
    ncbxsyb = "//li[@class='m1_7']/a[text()='农村保险事业部']"
    # 登录日志查询模块
    dlrzcx = "//li[@class='m1_6']/a[text()='登录日志查询']"
    # 经代渠道模块
    jdqd = "//li[@class='m1_4']/a[text()='经代渠道']"
    # 银保渠道模块
    ybqd = "//li[@class='m1_4']/a[text()='银保渠道']"
    # 车商渠道模块
    csqd = "//li[@class='m1_4']/a[text()='车商渠道']"
    # 综合管理模块
    zhgl = "//li[@class='m1_4']/a[text()='综合管理']"
    # --------------展开------------#
    # 销售团队展开
    xstdzk = "//td[@id='ygtvt135']"
    # 销售人员展开
    xsryzk = "//td[@id='ygtvt460']"
    # --------------子菜单----------#
    # 代理制销售人员代码管理
    dlzxsrydmgl = "//a[@id='ygtvlabelel461']"

    # ------------------------  页面元素 ------------------------#

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

    # 页面切换
    # 进入第一层iFrame
    def switch_to_first_iFrame(self, first_iFrame_id):
        self.switch_to_default_content()
        self.select_frame_id(first_iFrame_id)

    handles = []

    def switch_to_window(self, num=-1):
        time.sleep(2)
        # if not self.handles:
            # current = g.driver.current_window_handle
        new = []
        for i in range(5):
            new = self.get_handles()
            print(new)
        self.handles = self.update_handles(self.handles, new)
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
        self.switch_to_window()
        option = self.wait_until_el_xpath("//select/option[contains(@value,'{0}')]".format(text.split('--')[0]))
        self.click(option)
        confirm = self.wait_until_el_xpath("//input[@value='确定']")
        self.click(confirm)
        self.switch_to_window()

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
        sleep(0.5)
        el.click()

    @catch_except
    def wait_until_el_xpath(self, xpath):
        el = g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        high_light(element=el)
        sleep(0.5)
        return el

    @catch_except
    def wait_until_els_xpath(self, xpath):
        return g.wait.until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))

    @catch_except
    def close_browser(self):
        sleep(0.5)
        g.driver.quit()

    @catch_except
    def choose_ok_on_alert(self):
        sleep(3)
        alter = g.driver.switch_to.alert
        sleep(3)
        alter.accept()
        sleep(1)

    @catch_except
    def send_keys(self, el, value):
        el.clear()
        el.send_keys(value)

    @set_wait(1)
    def is_element_exist(self, xpath):
        try:
            el = g.wait.until(
                expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
            high_light(element=el)
            return True
        except BaseException:
            return False

    @catch_except
    def get_text(self, el):
        return el.text

    @catch_except
    def get_element_xpath(self, xpath):
        el = g.driver.find_element_by_xpath(xpath)
        high_light(element=el)
        return el

    @catch_except
    def right_click(self, xpath):
        right_click = g.driver.find_element_by_xpath(xpath)
        high_light(element=right_click)
        ActionChains(g.driver).context_click(right_click).perform()

    @catch_except
    def is_selected(self, xpath):
        el = g.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))).is_selected()
        high_light(element=el)
        return el

    @catch_except
    def open_url(self, url):
        g.driver.get(url)
        handles = g.driver.window_handles
        g.driver.switch_to.window(handles[-1])

    @catch_except
    def double_click(self, double_click_el):
        ActionChains(g.driver).double_click(double_click_el).perform()

    @catch_except
    def move_to_el(self, el):
        webdriver.ActionChains(g.driver).move_to_element(el).perform()
        # webdriver.ActionChains(g.driver).click_and_hold(el).perform()
        sleep(1)

    @catch_except
    def active_el(self):
        return g.driver.switch_to.active_element

    @catch_except
    def switch_to_default_content(self):
        g.driver.switch_to.default_content()

    @catch_except
    def select_frame_id(self, id):
        g.driver.switch_to.frame(id)

    @catch_except
    def maximize_window(self):
        g.driver.maximize_window()

    @catch_except
    def current_window(self):
        g.driver.current_window_handle()

    @catch_except
    def execute_script(self, js, ele):
        g.driver.execute_script(js, ele)

    @catch_except
    def execute_script_s(self, js, ele, value):
        g.driver.execute_script(js, ele, value)

    @catch_except
    def get_select(self, el):
        return Select(el)

    @catch_except
    def get_attribute(self, el, att_name):
        return el.get_attribute(att_name)

    @catch_except
    def get_handles(self):
        return g.driver.window_handles

    @catch_except
    def switch_to_win(self, handle):
        g.driver.switch_to.window(handle)

    # ------------------------  assert api ------------------------#

    # 断言方法
    def assertEqual(self, message, actual, expect):
        pytest.assume(actual == expect)
        info('message-->{0},actual-->{1},expect-->{2},result-->{3}'.format(message, actual, expect,actual == expect))

    def assertResult(self, message, result):
        pytest.assume(result)
        info('message-->{0},result-->{1}'.format(message, result))

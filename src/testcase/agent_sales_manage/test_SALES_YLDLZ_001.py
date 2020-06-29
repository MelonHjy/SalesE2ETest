# -*- coding:utf-8 -*-
#@Time : 2020/6/28 17:22
#@Author: fyl
#@File : test_SALES_YLDLZ_001.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.page.base_page import BasePage
from src.utils.create_dir import create_download_dir
from src.utils.driver_util import *
from src.utils.high_light_element import high_light


class Test_YLDLZ_001():
    def test_YLDLZ_001(self):
        #g.downloadDir = create_download_dir()
        g.config = get_config()
        url = g.config['DEFAULT']['url']
        browser = g.config['DEFAULT']['browser']
        g.driver = get_browser(browser, g.downloadDir)
        g.wait = WebDriverWait(g.driver, 50)
        g.driver.maximize_window()
        info("进入%s", url)
        BasePage().open_url(url)
        username = BasePage().wait_until_el_xpath("//input[@id='username1']")
        password = BasePage().wait_until_el_xpath("//input[@id='password1']")
        login = BasePage().wait_until_el_xpath("//input[@id='button']")
        BasePage().click(login)
        # jyjg = BasePage().wait_until_el_xpath("//a[text()='经营机构']")
        list = g.wait.until(
            expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'm1_4')))
        #jyjg = g.driver.find_element_by_link_text('经营机构')
        print(len(list))
        BasePage().move_to_el(list[1])
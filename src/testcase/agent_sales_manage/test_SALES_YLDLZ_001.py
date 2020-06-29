# -*- coding:utf-8 -*-
#@Time : 2020/6/28 17:22
#@Author: fyl
#@File : test_SALES_YLDLZ_001.py

from src.page.base_page import BasePage
from src.utils.create_dir import create_download_dir
from src.utils.driver_util import *
from src.utils.high_light_element import high_light


class Test_YLDLZ_001():
    def test_YLDLZ_001(self):
        g.downloadDir = create_download_dir()
        g.config = get_config()
        url = g.config['DEFAULT']['url']
        browser = g.config['DEFAULT']['browser']
        g.driver = get_browser(browser, g.downloadDir)
        g.wait = WebDriverWait(g.driver, 20)
        g.driver.maximize_window()
        info("进入%s", url)
        BasePage().open_url(url)
        sleep(30)
        username = BasePage().wait_until_el_xpath("//input[@id='username1']")
        BasePage().send_keys(username,"A320101044")
        password = BasePage().wait_until_el_xpath("//input[@id='password1']")
        BasePage().send_keys(password,"sales202006")
        login = BasePage().wait_until_el_xpath("//input[@id='button']")
        high_light(login)
        BasePage().click(login)
        BasePage().move_to_el(BasePage().wait_until_el_xpath("//li[@class='m1_4']/a[text()='经营机构']"))
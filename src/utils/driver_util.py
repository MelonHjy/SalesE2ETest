# -*- coding: utf-8 -*-#
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from functools import wraps

from selenium.webdriver.support.wait import WebDriverWait
from src.utils.log import *
import configparser
import win32api
import win32con

BROWSER_PATH_DIC = {
    "chrome": r".\driver\chromedriver.exe",
    "firefox": r".\driver\geckodriver",
    "ie": r".\driver\IEDriverServer"
}


def logout(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        driver = func(*args, **kwargs)
        # 注销登录
        driver.delete_all_cookies()
        try:
            js = 'window.localStorage.setItem("token","")'
            js2 = 'window.localStorage.setItem("Authorization","")'
            driver.execute_script(js)
            driver.execute_script(js2)
        except Exception as e:
            info('No localStorage')
        finally:
            return driver

    return decorated


def set_wait(timeout):
    '''临时修改全局的等待时间，函数执行后，设回原值

    :param timeout: 等待时间
    '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global_time = g.wait._timeout
            g.wait = WebDriverWait(g.driver, timeout)
            func1 = func(*args, **kwargs)
            g.wait = WebDriverWait(g.driver, global_time)
            return func1

        return wrapper

    return decorator


def get_config():
    config = configparser.ConfigParser()
    config.read(r'config\config.ini')
    return config


@logout
def get_browser(browser="chrome", download_location=None, headless=False):
    if browser == "chrome":
        chrome_options = Options()
        if download_location:
            prefs = {'download.default_directory': download_location,
                     'download.prompt_for_download': False,
                     'download.directory_upgrade': True,
                     'safebrowsing.enabled': False,
                     'safebrowsing.disable_download_protection': True}
            chrome_options.add_experimental_option('prefs', prefs)
        if headless:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=BROWSER_PATH_DIC[browser], options=chrome_options)
        if headless:
            enable_download_in_headless_chrome(driver, download_location)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=BROWSER_PATH_DIC[browser])
    elif browser == "ie":
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                                  'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\3',
                                  0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, '2500', 0, win32con.REG_DWORD, 0x3)
        caps = DesiredCapabilities.INTERNETEXPLORER
        caps['ignoreProtectedModeSettings'] = True
        # caps['nativeEvents'] = False
        # caps['unexpectedAlertBehaviour'] = "accept"
        # caps['disable-popup-blocking'] = True
        # caps['enablePersistentHover'] = True
        # caps['ignoreZoomSetting'] = True
        driver = webdriver.Ie(executable_path=BROWSER_PATH_DIC[browser], capabilities=caps)
    else:
        raise NameError("Not found {} browser, You can enter 'ie', 'firefox', 'chrome'.".format(browser))

    return driver


# 获取指定端口的浏览器
@logout
def get_fixed_browser(browser="chrome", ip="127.0.0.1", port="9222"):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", ip + ':' + port)
        driver = webdriver.Chrome(executable_path=BROWSER_PATH_DIC[browser], chrome_options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=BROWSER_PATH_DIC[browser])
    elif browser == "ie":
        driver = webdriver.Ie(executable_path=BROWSER_PATH_DIC[browser])
    else:
        raise NameError("Not found {} browser, You can enter 'ie', 'firefox', 'chrome'.".format(browser))
    return driver


def enable_download_in_headless_chrome(driver, download_dir):
    """
    there is currently a "feature" in chrome where
    headless does not allow file download: https://bugs.chromium.org/p/chromium/issues/detail?id=696481
    This method is a hacky work-around until the official chromedriver support for this.
    Requires chrome version 62.0.3196.0 or above.
    """

    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)
    print("response from browser:")
    for key in command_result:
        print("result:" + key + ":" + str(command_result[key]))



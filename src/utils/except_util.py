# -*- encoding: utf-8 -*-
import codecs
import traceback

import allure
from selenium.common.exceptions import TimeoutException

from config.global_var import *
from functools import wraps
from datetime import datetime

from src.utils.common_util import task_kill, close_ie
from src.utils.log import info


def get_screenshot(filename):
    now = datetime.now().strftime('%H%M%S%f')  # 时间戳
    filename = now + filename + ".png"  # 拼接文件名 时间戳+文件名+.png
    filepath = os.path.join(r".\report\allure-results\screenshot", filename)
    try:
        g.driver.get_screenshot_as_file(filepath)
        with open(filepath, 'rb') as f:
            file = f.read()
            allure.attach(file, "截图", allure.attachment_type.PNG)
    except Exception as e:
        info("截图时出错：%s" % e)


def catch_except(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            get_screenshot("异常")
            sleep(2)
            raise e

    return wrapper


def close(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TimeoutException as e:
            info('TimeoutError')
            choose_ok_on_alert()
            info("hhahahaha1231231231h")
            traceback.format_exc()
            close_ie()
        except Exception as e:
            info(e)
            info("hhahahahah")
            choose_ok_on_alert()
            info('Exceptionbbbb')
            traceback.format_exc()
            close_ie()

    return wrapper


def choose_ok_on_alert():
    sleep(3)
    alter = g.driver.switch_to.alert
    sleep(3)
    alter.accept()
    sleep(1)


def save_page():
    file_name = g.reportDir + "{}.html".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    page_source = g.driver.page_source

    f = None
    try:
        f = codecs.open(file_name, 'w', 'utf-8')
        f.write(page_source)
    except Exception as e:
        raise e
    finally:
        f.close()
    with open(file_name, mode='rb') as f:
        file = f.read()
    with allure.step('报错页面：'):
        allure.attach(file, "", allure.attachment_type.TEXT)

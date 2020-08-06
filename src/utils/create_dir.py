# -*- coding: utf-8 -*-#
import os
from datetime import datetime

from config.global_var import g


def create_report_dir():
    screenshot_dir = "/report"  # 当前目录下的report文件夹；或设置其他目录
    return create_dir(screenshot_dir)


def create_log_dir():
    screenshot_dir = "/logs"
    return create_dir(screenshot_dir)


def create_download_dir():
    screenshot_dir = "/download"
    return create_dir(screenshot_dir)


def create_dir(base):
    base_dir = g.root_path + base
    if not os.path.exists(base_dir):  # 不存在则创建该目录
        os.mkdir(base_dir)

    now_date = datetime.now().strftime('%Y%m%d-%H%M%S%f')  # 当日日期+时间戳
    today_dir = base_dir + '/' + now_date  # 当前日期文件夹
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)  # 不存在则创建
    return today_dir


if __name__ == '__main__':
    print(create_log_dir())

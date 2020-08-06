# -*- coding: utf-8 -*-#
import os
import time


def sleep(s):
    if s > 0:
        time.sleep(s)


class g:
    driver = None
    wait = None
    logger = None
    reportDir = None
    downloadDir = None
    timeout = 60
    config = None
    UserType = None
    db = None
    # 项目根目录
    root_path = os.path.abspath('.').replace('\\', '/')
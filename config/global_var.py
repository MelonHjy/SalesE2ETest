# -*- coding: utf-8 -*-#
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
    timeout = 20
    config = None
    UserType = None
    db = None

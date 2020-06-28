# -*- coding: utf-8 -*-#
from config.global_var import g


def high_light(element):
    g.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                            element, "border:2px solid red;")


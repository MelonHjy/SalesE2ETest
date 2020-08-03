# -*- coding: utf-8 -*-#
import json
import os

from src.utils.common_util import DecoratorType


def data_reader(filename, decorator_type=DecoratorType.parametrize):
    base_path = os.path.dirname(__file__)
    path = base_path.replace('\\src\\utils', '\\data\\' + filename)
    path = path.replace(r'/src/utils', '/data/' + filename)
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        if DecoratorType.parametrize == decorator_type:
            return list(map(dict_to_tuple, data))
        if DecoratorType.fixture == decorator_type:
            return data
        else:
            raise TypeError('Wrong DecoratorType:"%s"' % decorator_type)


def dict_to_tuple(dic):
    return tuple(dic.values())


if __name__ == '__main__':
    d = data_reader("agent_sales_manage/test_SPE_001.json", DecoratorType.fixture)
    print(d)

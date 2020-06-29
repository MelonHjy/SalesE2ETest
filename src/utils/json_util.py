# -*- coding: utf-8 -*-#
import json
import os


def data_reader(filename):
    # path='../csv_function'+filename
    base_path = os.path.dirname(__file__)
    path = base_path.replace('\\src\\utils', '\\data\\' + filename)
    path = path.replace(r'/src/utils', '/data/' + filename)
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def dict_to_tuple(dic):
    return tuple(dic.values())


def json_dict_to_tuple(data):
    return list(map(dict_to_tuple, data))


if __name__ == '__main__':
    d = data_reader("specialist/test_SPE_001.json")
    print(json_dict_to_tuple(d))
    print(tuple({"123": "aaa", "1323": "aaa"}.values()))
# -*- coding: utf-8 -*-#
import csv
import os

from src.utils.common_util import DecoratorType


def data_reader(filename, decorator_type=DecoratorType.parametrize):
    base_path = os.path.dirname(__file__)
    path = base_path.replace('\\src\\utils', '\\data\\' + filename)
    path = path.replace(r'/src/utils', '/data/' + filename)
    with open(path, encoding='utf-8') as file:
        # csv.reader返回一个迭代器，因其惰性计算没法获取长度，使用next()获取下一个值
        table = csv.reader(file)
        # 获取第一行的值，csv表头
        heads = next(table)
        if DecoratorType.parametrize == decorator_type:
            return [tuple(rows) for rows in table]
        if DecoratorType.fixture == decorator_type:
            return [{heads[i]: rows[i] for i in range(heads.__len__())} for rows in table]
        else:
            raise TypeError('Wrong DecoratorType:"%s"' % decorator_type)


if __name__ == '__main__':
    data = data_reader("agent_sales_manage/004_data.csv")
    # data = data_reader("agent_sales_manage/004_data.csv", DecoratorType.fixture)
    print(data)

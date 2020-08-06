# -*- coding: utf-8 -*-#
import csv

from config.global_var import g
from src.utils.common_util import DecoratorType


def data_reader(filename, decorator_type=DecoratorType.parametrize):
    path = g.root_path + '/data/' + filename
    path = 'C:/Users/Sino-PC201911/Desktop/SalesE2ETest/data/agent_sales_manage/014_data.csv'
    with open(path, encoding='utf-8') as file:
        # csv.reader返回一个迭代器，因其惰性计算没法获取长度，使用next()获取下一个值
        table = csv.reader(file)
        # 获取第一行的值，csv表头
        heads = next(table)
        if DecoratorType.parametrize == decorator_type:
            return [rows[0] if rows.__len__() == 1 else tuple(rows) for rows in table]
            # return [tuple(rows) for rows in table]
        if DecoratorType.fixture == decorator_type:
            return [{heads[i]: rows[i] for i in range(heads.__len__())} for rows in table]
        else:
            raise TypeError('Wrong DecoratorType:"%s"' % decorator_type)


if __name__ == '__main__':
    data = data_reader("agent_sales_manage/014_data.csv")
    # data = data_reader("agent_sales_manage/004_data.csv", DecoratorType.fixture)
    print(data)

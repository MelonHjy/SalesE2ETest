# -*- coding: utf-8 -*-#
import csv
import os
import random

from config.global_var import g
from src.utils.common_util import DecoratorType
from src.utils.create_identity import IdNumber


def data_reader(filename, decorator_type=DecoratorType.parametrize, ignore_heads=True):
    if not os.path.exists(filename):
        filename = g.root_path + '/data/{}/{}'.format(g.config['DEFAULT']['datafile'], filename)  # + filename    #
    with open(filename, encoding='utf-8') as file:
        # csv.reader返回一个迭代器，因其惰性计算没法获取长度，使用next()获取下一个值
        table = csv.reader(file)

        # 获取第一行的值，csv表头
        if ignore_heads:
            heads = next(table)
        if DecoratorType.parametrize == decorator_type:
            return [rows[0].strip() if rows.__len__() == 1 else tuple([row.strip() for row in rows]) for rows in table]
            # return [tuple(rows) for rows in table]
        if DecoratorType.fixture == decorator_type:
            return [{heads[i].strip(): rows[i].strip() for i in range(heads.__len__())} for rows in table]
        else:
            raise TypeError('Wrong DecoratorType:"%s"' % decorator_type)


def data_edit(data,file_name, edit_data_dict, row=1):
    """
    file_name:文件名
    edit_data_dict:[("需修改的列名","值")]
    row:需修改的行
    """
    list_data = list(data[row])
    for data_tuple in edit_data_dict:
        list_data[data[0].index(data_tuple[0])] = data_tuple[1]
    data[row] = tuple(list_data)
    with open(file_name, 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in data:
            writer.writerow(i)


def by_col_get_calue(data, file_name, col_name, row=None):
    if row:
        list_data = list(data[row])
        return list_data[data[0].index(col_name)]
    else:
        value = []
        j = 0
        for i in data:
            if j != 0:
                list_data = list(i)
                value.append(list_data[data[0].index(col_name)])
            j = j + 1
        return value


if __name__ == '__main__':
    # data = data_reader("agent_sales_manage/014_data.csv")
    data = data_reader("C:/Users/Sino-PC201911/Desktop/SalesE2ETest/data/group_issue_manage/test_SALES_YLTD_001.csv",
                       ignore_heads=False)
    # data = data_reader("agent_sales_manage/004_data.csv", DecoratorType.fixture)
    # print(data)
    old_id = by_col_get_calue(data, "/data/default/agent_sales_manage/test_001.csv", "idCard", 1)
    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
    new_id = IdNumber.generate_id(random_sex)  # 随机生成身份证号
    # print(id)
    edit_data_dict = [("idCard",new_id),("old_id",old_id)]
    data_edit(data, "/data/default/agent_sales_manage/test_001.csv", edit_data_dict)
    # aa = by_col_get_calue("D:/env/pycharm/PycharmProjects/SalesE2ETest/data/agent_sales_manage/test_001.csv",
    #                       "userName", 1)
    # print(aa)

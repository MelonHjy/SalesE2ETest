# -*- coding: utf-8 -*-#
import csv
import json
import os


def data_reader(filename):
    # path='../csv_function'+filename
    list = []
    base_path = os.path.dirname(__file__)
    path = base_path.replace('\\src\\utils', '\\data\\' + filename)
    path = path.replace(r'/src/utils', '/data/' + filename)
    with open(path) as file:
        table = csv.reader(file)
        for rows in table:
            list.append(rows)
        return list


if __name__ == '__main__':
    csv = data_reader("user.csv")
    print(csv)

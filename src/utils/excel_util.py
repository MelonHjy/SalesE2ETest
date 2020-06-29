# -*- coding: utf-8 -*-#
import xlrd
from src.utils.log import *


class ExcelUtil(object):
    def __init__(self, abspath, page_num=0):
        # 读xls文件
        excel = xlrd.open_workbook(abspath)
        # 获取第page_num张表
        self.table = excel.sheet_by_index(page_num)
        self.heads = self.get_table_row_heads()

    def get_table_row_heads(self):
        return self.table.row_values(0)

    def get_table_rows(self):
        return self.table.nrows

    # 获取指定表头对应列数据(start with 1)
    def get_excel_data_by_head(self, head, start_rowx=1, end_rowx=2):
        return self.table.col_values(self.heads.index(head), start_rowx, end_rowx)

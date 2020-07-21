#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File       :   table_page.py
@Time       :   2020/7/17 16:02
@Author     :   Huang Jiayi
@Version    :   1.0
@Contact    :   huangjiayi@sinosoft.com.cn
@Desc       :   None
'''
import re

from src.page.base_page import BasePage
from src.utils.excel_util import ExcelUtil
from src.utils.log import info
from src.utils.driver_util import set_wait
from config.global_var import g
from time import sleep


class TablePage(BasePage):
    def __init__(self):
        self.excel = None
        self.set_table_num()

    def set_table_num(self, table_num=0):
        self.heads = []

        # 第几个表格,默认是0为第一个
        self.table_num = table_num
        # ------------------------  表格元素 ------------------------#
        # 表格第几行第几列
        # col 空、row 空
        self.table_all = "//td[contains(@id,'yui-dt" + str(table_num) + "')]"
        # col 空、row 非空
        self.table_row = "//td[contains(@id,'yui-dt" + str(table_num) + "-bdrow{0}')]"
        # col 非空、row 空
        self.table_col = "//td[contains(@id,'yui-dt" + str(
            table_num) + "') and substring(@id, string-length(@id)-string-length('cell{0}') +1) = 'cell{0}']"
        # col 非空、row 非空    /descendant-or-self::*
        self.table_row_col = "//td[@id='yui-dt" + str(table_num) + "-bdrow{0}-cell{1}']"

        # 表格头
        self.table_head = "//thead/tr[@id='yui-dt" + str(table_num) + "-hdrow0']/th/div/span"
        # 表格显示的行
        self.table_show_rows = "//table[@id='yui-dt-table" + str(table_num) + "']/tbody[2]/tr"
        # 表格 ‘无记录...’ 或 ‘数据加载中...’
        self.table_no_row = "//table[@id='yui-dt-table" + str(table_num) + "']/tbody[1]/tr/td"
        # 查询总记录数
        self.table_total = "//div[@id='content" + str(table_num) + "_navigation']"

    def get_cell_text_by_head(self, head, row=-1):
        """
        获取指定表头对应列、指定行的数据
        :param head: 表头文本值
        :param row: 第几行，默认为全部行
        :return: 默认返回对应的列的所有文本值（列表形式），指定行则返回对应行
        """
        heads = self.get_table_heads_text()
        if head not in heads:
            raise ValueError('{0} is not in {1}'.format(head, self.heads))
        return self.get_cell_text(row, self.heads.index(head))

    # 单选按钮
    def get_cell_radio(self, row, col):
        # 下标0为td标签，1为对应标签
        return self.get_cell(row, col, True)[1]

    # 按钮
    def get_cell_a(self, row, col):
        return self.get_cell(row, col, True)[1]

    # a标签
    def get_cell_button(self, row, col):
        return self.get_cell(row, col, True)[1]

    @set_wait(1)
    # 获取表格第几列第几行的值(row与col小于零时代表全部[若均小于0，默认以行为分隔]，获取第一行第一列使用row=0,col=0） 存在纯文本与有p标签的文本
    def get_cell_text(self, row=-1, col=-1, split_by_row=True):
        text = []
        cells = self.get_cell(row, col)
        if row < 0 and col < 0:     # return [[],[],[]]
            text = self.split_by(cells, self.heads.__len__(), split_by_row)
        elif row < 0 or col < 0:    # return []
            for cell in cells:
                text.append(self.get_inner_text(cell))
        else:   # return str
            text = self.get_inner_text(cells[0])
        return text

    def get_inner_text(self, el):
        try:
            inner_text = el.get_attribute('innerText')
        except Exception:
            inner_text = ""
        return inner_text.strip()

    def split_by(self, cells, col, split_by_row=True):
        '''
        根据行或列分隔元素
        :param cells: 初始元素列表
        :param col: 表格有多少列
        :param split_by_row: 是否根据行分隔
        :return: 返回多维列表
        '''
        num = len(cells) // col if split_by_row else col
        texts = [[] for i in range(num)]
        for i, cell in enumerate(cells, 0):
            if split_by_row:
                texts[i // col].append(self.get_inner_text(cell))
            else:
                texts[i % col].append(self.get_inner_text(cell))
        return texts

    # 获取表格第几列第几行的元素(row与col小于零时代表全部，获取第一行第一列使用row=0,col=0）
    def get_cell(self, row=-1, col=-1, special=False):
        if col >= 0 and row >= 0:
            xpath = self.table_row_col.format(row, col)
        elif col >= 0:
            xpath = self.table_col.format(col)
        elif row >= 0:
            xpath = self.table_row.format(row)
        else:
            xpath = self.table_all
        if special:
            xpath += "/descendant-or-self::*"
        return self.wait_until_els_xpath(xpath)

    # 获取表格头
    def get_table_heads_text(self):
        if not self.heads:
            heads_div = self.wait_until_els_xpath(self.table_head)
            self.heads.extend([head_div.get_attribute('innerText') for head_div in heads_div])
        return self.heads

    # 当前页面显示的行数
    def get_table_show_rows(self):
        if not self.show_rows:
            self.show_rows = self.wait_until_els_xpath(self.table_show_rows).__len__()
        return self.show_rows

    # 查询总记录数( example: [Page 1 / 3733]  [37323 Records]   )
    def get_table_rows(self):
        return int(re.match(".*?\\[(\\d+)", self.wait_until_el_xpath(self.table_total).text).group(1))

    def set_excel(self, abspath):
        self.excel = ExcelUtil(abspath)

    def assume_table_data(self, excel_head, html_head):
        # 检查对应列中，当前页面数据与表格数据是否一致
        excel_list = self.excel.get_excel_data_by_head(excel_head, end_rowx=self.get_table_show_rows() + 1)
        html_list = self.get_cell_text_by_head(html_head)
        info('excel-->{0}：{1}'.format(excel_head, excel_list))
        info('页面-->{0}：{1}'.format(html_head, html_list))
        self.assertEqual("判断当前页面数据与表格数据是否一致", excel_list, html_list)

    # excel_ignore 默认忽略excel表头的那一行
    def assume_table_num(self, excel_ignore=1):
        row1_num = self.excel.get_table_rows() - excel_ignore
        row2_num = self.get_table_rows()
        info('excel-->行数：' + str(row1_num))
        info('页面-->数据总计：' + str(row2_num))
        self.assertEqual("判断excel与页面的数据数是否一致", row1_num, row2_num)

    # 判断页面显示行数与导出行数是否一致
    def assume_table_html_num(self, excel_ignore=1):
        row1_num = self.excel.get_table_rows() - excel_ignore
        row2_num = self.get_table_show_rows()
        info('excel-->行数：' + str(row1_num))
        info('页面-->数据总计：' + str(row2_num))
        self.assertEqual("判断excel与页面显示的数据数量是否一致", row1_num, row2_num)

    # 使用JavaScript的scrollIntoView函数将被遮挡的元素滚动到屏幕上
    # scrollIntoView(true)表示将元素滚动屏幕中间
    # scrollIntoView(false)表示将元素滚动到屏幕底部
    # document.evaluate 函数，返回的是一个枚举集合(IE 使用document.selectNodes）
    def scroll_into_view(self, xpath, is_show=True):
        g.driver.excute_script(
            "document.evalute({0},document, null, XPathResult.ANY_TYPE, null).iterateNext().scrollIntoView(true);")
        sleep(1)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File       :   db_util.py
@Time       :   2020/6/30 13:44
@Author     :   Huang Jiayi
@Version    :   1.0
@Contact    :   huangjiayi@sinosoft.com.cn
@Desc       :   None
'''

import random
import jaydebeapi


class DBUtils:
    __limit = 100

    def __init__(self, url, user, password):
        self.conn = self.get_connection(url, user, password)

    def get_connection(self, url, user, password):
        return jaydebeapi.connect('com.informix.jdbc.IfxDriver', url, [user, password], '../../config/ifxjdbc.jar')

    def close_connection(self):
        try:
            self.conn.close()
        except BaseException as e:
            raise

    @staticmethod
    def random_choice(results, num=1):
        data = []
        for i in range(num):
            choice = random.choices(results)[0]
            data.append(choice)
            results.remove(choice)
        return data

    def select(self, sql, args=None, limit=__limit):
        '''
        查询
        :param sql:sql语句  "select * from hd_t_vprpdcompany where comcode='?'"
        :param args:参数（数据类型为元组）   ('37010000',)
        :param limit: 只取limit前的数据，默认为__limit
        :return: 查询的结果
        '''
        cur = self.conn.cursor()
        cur.execute(sql, args)
        results = cur.fetchmany(limit) if limit else cur.fetchall()  # fetchmany()获取最多指定数量的记录
        cur.close()
        return results

    def excute(self, sql, args):
        '''
        增删改
        :param sql:sql语句   "inserst into hd_t_vprpdcompany set(usercode,username) values(?,?)"
        :param args:参数（数据类型为元组）  ('37010000','haha')
        :return: 影响的行数
        '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, args)
            rowcount = cur.rowcount
            self.conn.commit()
            cur.close()
        except BaseException as e:
            raise
        return rowcount


if __name__ == '__main__':
    url = 'jdbc:informix-sqli://10.10.68.24:10001/salesdbcs:informixserver=test1;NEWLOCALE=zh_CN,zh_CN;NEWCODESET=gb18030,8859-1,819;'
    user = 'xsglifx1'
    password = 'u^6m.8LA0'
    db = DBUtils(url, user, password)
    try:
        sql = "select * from SaUUser"
        data = db.select(sql)
        data = db.random_choice(data, 3)
        for d in data:
            print(d)
    finally:
        db.close_connection()

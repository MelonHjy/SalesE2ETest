#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File       :   db_util.py
@Time       :   2020/6/18 17:54
@Author     :   Huang Jiayi
@Version    :   1.0
@Contact    :   huangjiayi@sinosoft.com.cn
@Desc       :   None
'''
from functools import wraps

import psycopg2
import random


def tuple_to_dict(tp):
    return {'v' + str(i): tp[i] for i in range(tp.__len__())}


def tuple_to_dict_by_keys(tp, keys):
    '''

    :param tp: (1,'aa')
    :param keys: ('v0','v1')
    :return: {'v0':1,'v1':'aa'}
    '''
    return {keys[i]: tp[i] for i in range(tp.__len__())}


def return_dict(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return list(map(tuple_to_dict, data))
        # return list(map(tuple_to_dict_by_keys, data, [('code', 'name')] * data.__len__()))

    return wapper


class DBUtils:
    __limit = 100

    def __init__(self, database, user, password, host, port):
        self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    # @return_dict
    def random_choice(self, results, num=1):
        data = []
        for i in range(num):
            choice = random.choices(results)[0]
            data.append(choice)
            results.remove(choice)
        return data

    def select(self, sql, args, limit=__limit):
        '''
        查询
        :param sql:sql语句
        :param args:参数（数据类型为元组）
        :param limit: 只取limit前的数据，默认为__limit
        :return: 查询的结果
        '''
        cur = self.conn.cursor()
        cur.execute(sql, args)
        # cur.execute("select * from hd_t_vprpdcompany where comcode='?'", ('37010000',))
        results = cur.fetchmany(limit) if limit else cur.fetchall()  # fetchmany()获取最多指定数量的记录
        cur.close()
        return results

    def excute(self, sql, args):
        '''
        增删改
        :param sql:sql语句
        :param args:参数（数据类型为元组）
        :return: 影响的行数
        '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, args)
            # cur.execute("inserst into hd_t_vprpdcompany set(usercode,username) values(?,?)", ('37010000','haha'))
            rowcount = cur.rowcount
            self.conn.commit()
            cur.close()
        except BaseException as e:
            raise
        return rowcount


if __name__ == '__main__':
    db = DBUtils(database='postgres', user='specialist', password='specialist@123', host='10.156.129.97', port='5432')
    # 是专员
    sql = "select hs.usercode,hs.username from hd_t_commissioner hc RIGHT JOIN hd_t_sauuser hs on hc.usercode = hs.usercode where hs.validstatus = '1' and flag='1' " \
          "AND hs.comcode in (select comCode from hd_t_vprpdcompany where validStatus='1' and upperpath like concat('%%',%s,'%%'))"
    # 不是专员
    sql2 = "select hs.usercode,hs.username from hd_t_commissioner hc RIGHT JOIN hd_t_sauuser hs on hc.usercode = hs.usercode where hs.validstatus = '1' and (flag is null or flag='2') " \
           "AND hs.comcode in (select comCode from hd_t_vprpdcompany where validStatus='1' and upperpath like concat('%%',%s,'%%'))"
    data = db.select(sql2, ('37010000',))
    data = db.random_choice(data, 3)
    print(data)
    db.conn.close()

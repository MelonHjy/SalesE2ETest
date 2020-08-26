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

from config.global_var import g
from src.utils.log import info


class DBUtils:
    __limit = 100
    test_name = None

    def __init__(self, url, user, password):
        jar_path = g.root_path + '/config/ifxjdbc.jar'
        self.conn = jaydebeapi.connect('com.informix.jdbc.IfxDriver', url, [user, password], jar_path)
        info('连接conn id：%s' % (id(self.conn)))
        self.execute("SET LOCK MODE TO WAIT 30")

    def close_connection(self):
        try:
            info('%s关闭conn id：%s' % (self.test_name, id(self.conn)))
            self.conn.close()
        except BaseException as e:
            info('关闭连接错误信息:%s' % e)
            # raise

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
        info('%s执行select语句conn id：%s' % (self.test_name, id(self.conn)))
        cur = self.conn.cursor()
        cur.execute(sql, args)
        results = cur.fetchmany(limit) if limit else cur.fetchall()  # fetchmany()获取最多指定数量的记录
        cur.close()
        return results

    def execute(self, sql, args=None):
        '''
        增删改
        :param sql:sql语句   "insert into hd_t_vprpdcompany set(usercode,username) values(?,?)" args为空时直接执行语句
        :param args:参数（数据类型为元组）  ('37010000','haha')
        :return: 影响的行数
        '''
        try:
            info('%s执行execute语句conn id：%s' % (self.test_name, id(self.conn)))
            cur = self.conn.cursor()
            if args:
                cur.execute(sql, args)
            else:
                cur.execute(sql)
            rowcount = cur.rowcount
            # self.conn.commit()
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
        #         # 增删改示例
        #         sql = '''
        # delete from saucontract where usercode = '83258551';
        # /*插入合同信息*/
        # insert into saucontract (agentarea, agentenddate, agentid, agentno, agentstartdate, batchno, checkstatus, comfeedate, contractno, contractaddress, contractcount, contractenddate, contractstartdate, creator, credentialenddate, credentialid, credentialno, credentstartdate, effecttime, effectivedate, failuretime, flag, guarantoraddress, guarantorcardnum, guarantorname, guarantorphone, inputtime, lastcontractid, remark, ruleno, updatetime, updator, usercode, userid, validstatus, ucontractid) values ('', '', 1000000002071305, '123456', '2019-01-01', '', 'a', 0, '320000110200146', '', 1, '2022-08-03', '2020-08-06', 'A320000135', '', 1000000002071436, '654321', '2019-01-01', '', '', '', '', '', '', '', '', '2020-08-06 09:44:30', '', '', 'RULE20120000000000001', '', '', '83258551', 1000000002297783, '1', 1000000001904324);
        # '''
        #         data = db.execute(sql)
        #         print(data)

        # 查示例
        sql2 = "select msgid,groupCode,groupName,groupType,comCode,optUser from saugroupbackmsg where groupid in (select groupid from saugroup where groupname='ui测试-001');"
        data2 = db.select(sql2)
        # data2 = db.random_choice(data2, 3)
        for d in data2:
            print(d)
    finally:
        db.close_connection()

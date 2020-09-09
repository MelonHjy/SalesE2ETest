/* 删除人员清分表数据*/
-- delete from sauusersyn where usercode = '83258561';
delete from sadaccount where accountid=1000000001354600;
/*插入账户信息*/
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354600, '曹庚珐ui测试', '交通银行', '1112223334123', '', '2', '2', 'BOCOM       ', '1200', '天津市_天津市', '301110000115', '1', '440106199004106870', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-07-28 14:29:56', '%Y-%m-%d %H:%M:%S'), '0         ', null, null, TO_DATE('2020-07-28 13:45:00', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-07 11:07:43', '%Y-%m-%d %H:%M:%S'));
delete from sainterfaceinfo where businessno in ('83258561','1000000001354600');


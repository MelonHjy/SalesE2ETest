delete from saaagentresult where agentcode in(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介01');
delete from sainterfaceinfo where businessno in(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介01');
delete from sainterfaceinfo where businessno in(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介01');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111111');
delete from saaagentcontracthis where acontractid in(select acontractid from saacontract where agentname='ui测试-中介01');
delete from sabpmmain where businessno in(select contractno from saacontract where agentname='ui测试-中介01');
delete from saaagentcontract where acontractid in(select acontractid from saacontract where agentname='ui测试-中介01');
delete from saacontractresult where agentname='ui测试-中介01';
delete from saacontracthis where agentname='ui测试-中介01';
delete from sadaccount where accountno='1111111';
delete from saaagenthis where agentname='ui测试-中介01';
delete from saacontract where agentname='ui测试-中介01';

delete from saaagentresult where agentcode in(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-经代渠道');
delete from sainterfaceinfo where businessno in(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-经代渠道');
delete from sainterfaceinfo where businessno in(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-经代渠道');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111113');
delete from saaagentcontract where acontractid in(select acontractid from saacontract where agentname='ui测试-经代渠道');
delete from saaagentcontracthis where acontractid in(select acontractid from saacontract where agentname='ui测试-经代渠道');
delete from sabpmmain where businessno in(select contractno from saacontract where agentname='ui测试-经代渠道');
delete from saacontractresult where agentname='ui测试-经代渠道';
delete from saacontracthis where agentname='ui测试-经代渠道';
delete from sadaccount where accountno='1111113';
delete from saaagenthis where agentname='ui测试-经代渠道';
delete from saacontract where agentname='ui测试-经代渠道';

delete from saaagentresult where agentcode in(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-银保渠道');
delete from sainterfaceinfo where businessno in(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-银保渠道');
delete from sainterfaceinfo where businessno in(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-银保渠道');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111113');
delete from saaagentcontract where acontractid in(select acontractid from saacontract where agentname='ui测试-银保渠道');
delete from saaagentcontracthis where acontractid in(select acontractid from saacontract where agentname='ui测试-银保渠道');
delete from sabpmmain where businessno in(select contractno from saacontract where agentname='ui测试-银保渠道');
delete from saacontractresult where agentname='ui测试-银保渠道';
delete from saacontracthis where agentname='ui测试-银保渠道';
delete from sadaccount where accountno='1111113';
delete from saaagenthis where agentname='ui测试-银保渠道';
delete from saacontract where agentname='ui测试-银保渠道';

delete from saaagentresult where agentcode in(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-车商渠道');
delete from sainterfaceinfo where businessno in(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-车商渠道');
delete from sainterfaceinfo where businessno in(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-车商渠道');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='111111111111');
delete from saaagentcontract where acontractid in(select acontractid from saacontract where agentname='ui测试-车商渠道');
delete from saaagentcontracthis where acontractid in(select acontractid from saacontract where agentname='ui测试-车商渠道');
delete from sabpmmain where businessno in(select contractno from saacontract where agentname='ui测试-车商渠道');
delete from saacontractresult where agentname='ui测试-车商渠道';
delete from saacontracthis where agentname='ui测试-车商渠道';
delete from sadaccount where accountno='111111111111';
delete from saaagenthis where agentname='ui测试-车商渠道';
delete from saacontract where agentname='ui测试-车商渠道';

INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100025936, '32003J200040', 'ui测试-中介01', '3200', null, TO_DATE('2020-08-24 14:34:36', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-24 14:34:37', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-24 14:34:37', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontract (agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000545311, 1000000000196232, 1000000000072491, '32003J200040', 'RULE20133200000000001', null, '32990091', 'ui测试-中介01', 'P8THLLKR-X', TO_DATE('2020-08-21 09:44:01', '%Y-%m-%d %H:%M:%S'), null, '1', '1', null, '', TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontracthis (id, acontracthisid, agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001766968, 1000000000607305, 1000000000545311, 1000000000196232, 1000000000072491, '32003J200040', 'RULE20133200000000001', null, '32990091', 'ui测试-中介01', 'P8THLLKR-X', TO_DATE('2020-08-21 09:44:01', '%Y-%m-%d %H:%M:%S'), null, '1', '1', null, '', TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003330993, 1000000000034430, null, '32993J220082100       ', '2 ', 10, 0, TO_DATE('2020-08-21 09:41:33', '%Y-%m-%d %H:%M:%S'), '1', '32000000  ', null, '          ', 'A320000135      ', null, null, null, null, null, null, TO_DATE('2020-08-21 09:41:33', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'B', null, TO_DATE('2020-08-21 09:41:29', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:41:29', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003330994, 1000000000034430, null, '32993J220082100       ', '2 ', 11, 1, TO_DATE('2020-08-21 09:41:33', '%Y-%m-%d %H:%M:%S'), '1', null, null, '          ', 'A320000135      ', null, 10, null, '32000000  ', 'A320000135', null, TO_DATE('2020-08-21 09:44:01', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'C', 'ui测试', TO_DATE('2020-08-21 09:41:29', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:44:18', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontract (acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, creator, updator, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000196232, 'ui测试-中介01', '32993J220082100', '3J2', TO_DATE('2020-08-04', '%Y-%m-%d'), TO_DATE('2023-08-30', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '          ', '1', null, '操作员：A320000135手动终止流程。', TO_DATE('2020-08-21 09:41:29', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-25 10:08:28', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontractresult (contractresultid, agentname, acontractid, contractno, orgcode, permitno, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000162097, 'ui测试-中介01', 1000000000196232, '32993J220082100', null, null, '11', TO_DATE('2020-08-21 09:44:01', '%Y-%m-%d %H:%M:%S'), null, null, 'A320000135', '1         ', null, null, TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontracthis (id, acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, effecttime, failuretime, creator, updator, businessflag, updatetime, checkuser, checktime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000607305, 1000000000196232, 'ui测试-中介01', '32993J220082100', '3J2', TO_DATE('2020-08-04', '%Y-%m-%d'), TO_DATE('2023-08-30', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, null, null, 'A320000135', 'A320000135', 'A', TO_DATE('2020-08-21 09:44:01', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-21 09:44:01', '%Y-%m-%d %H:%M:%S'), '          ', '1', null, null, TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001353514, '赵建平', '中国邮政储蓄银行', '1111111', '', '2', '1', 'PSBC        ', '4312', '湖南省_怀化市', '403568200111', '1', '433030197310172418', '1', '0', '0', '', '43122900', null, null, '0         ', null, null, TO_DATE('2019-11-04 18:58:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2019-11-04 18:58:28', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000306122, '李娟', '建设银行', '1111111', '', '2', '1', 'CCB         ', '6206', '甘肃省_武威市', '105828000029', '1', '622322198912042624', '1', '0', '0', '', '62232200', '10074306  ', TO_DATE('2013-03-15 15:47:46', '%Y-%m-%d %H:%M:%S'), '0         ', null, null, TO_DATE('2013-01-12 22:24:38', '%Y-%m-%d %H:%M:%S'), TO_DATE('2013-03-15 15:50:28', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000531572, '中国工商银行股份有限公司恩施分行', '工商银行', '1111111', '', '1', '3', 'ICBC        ', '4228', '湖北省_恩施土家族苗族自治州', '102541705043', '2', '88301425-3', '1', '2', '2', '', '42280098', null, null, '1         ', null, null, TO_DATE('2013-11-18 11:52:26', '%Y-%m-%d %H:%M:%S'), TO_DATE('2014-11-25 10:47:05', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354794, 'ui测试-中介01', '交通银行', '1111111', '', '1', '1', 'BOCOM       ', '6540', '新疆维吾尔自治区_伊犁哈萨克自治州', '301898000032', '2', 'P8THLLKR-X', '1', '2', '2', '', '32990091', null, null, '1         ', null, null, TO_DATE('2020-08-21 09:41:06', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 09:43:59', '%Y-%m-%d %H:%M:%S'));

INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100025937, '320021101770', 'ui测试-经代渠道', '3200', null, TO_DATE('2020-08-24 16:14:25', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-24 16:14:25', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-24 16:14:25', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontract (agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000545313, 1000000000196234, 1000000000072493, '320021101770', 'RULE20120000000000001', null, '32990091', 'ui测试-经代渠道', 'P0P3IIZC-9', TO_DATE('2020-08-21 13:47:53', '%Y-%m-%d %H:%M:%S'), null, '1', '1', '1', '', TO_DATE('2020-08-21 11:21:17', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontracthis (id, acontracthisid, agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001766971, 1000000000607308, 1000000000545313, 1000000000196234, 1000000000072493, '320021101770', 'RULE20120000000000001', null, '32990091', 'ui测试-经代渠道', 'P0P3IIZC-9', TO_DATE('2020-08-21 13:47:53', '%Y-%m-%d %H:%M:%S'), null, '1', '1', null, '', TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003331015, 1000000000034440, null, '329921120082100       ', '2 ', 16, 0, TO_DATE('2020-08-21 11:21:22', '%Y-%m-%d %H:%M:%S'), '1', '32000000  ', null, '          ', 'A320000135      ', null, null, null, null, null, null, TO_DATE('2020-08-21 11:21:22', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'B', null, TO_DATE('2020-08-21 11:21:18', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 11:21:18', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003331016, 1000000000034440, null, '329921120082100       ', '2 ', 17, 1, TO_DATE('2020-08-21 11:21:22', '%Y-%m-%d %H:%M:%S'), '1', null, null, '          ', 'A320000135      ', null, 16, null, '32000000  ', 'A320000135', null, TO_DATE('2020-08-21 13:47:52', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'C', 'ui测试', TO_DATE('2020-08-21 11:21:18', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:48:10', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontract (acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, creator, updator, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000196234, 'ui测试-经代渠道', '329921120082100', '211', TO_DATE('2020-08-21', '%Y-%m-%d'), TO_DATE('2024-08-22', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, 'A320000135', null, '          ', '1', null, null, TO_DATE('2020-08-21 11:21:17', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontractresult (contractresultid, agentname, acontractid, contractno, orgcode, permitno, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000162100, 'ui测试-经代渠道', 1000000000196234, '329921120082100', null, null, '11', TO_DATE('2020-08-21 13:47:53', '%Y-%m-%d %H:%M:%S'), null, null, 'A320000135', '1         ', null, null, TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontracthis (id, acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, effecttime, failuretime, creator, updator, businessflag, updatetime, checkuser, checktime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000607308, 1000000000196234, 'ui测试-经代渠道', '329921120082100', '211', TO_DATE('2020-08-21', '%Y-%m-%d'), TO_DATE('2024-08-22', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, null, null, 'A320000135', 'A320000135', 'A', TO_DATE('2020-08-21 13:47:53', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-21 13:47:53', '%Y-%m-%d %H:%M:%S'), '          ', '1', null, null, TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354799, 'ui测试-经代渠道', '交通银行', '1111113', '', '1', '1', 'BOCOM       ', '6540', '新疆维吾尔自治区_伊犁哈萨克自治州', '301898000032', '2', 'P0P3IIZC-9', '1', '2', '2', '', '32990091', null, null, '1         ', null, null, TO_DATE('2020-08-21 11:21:11', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 13:47:50', '%Y-%m-%d %H:%M:%S'));

INSERT INTO saaagentcontract (agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000545315, 1000000000196236, 1000000000072494, '32003J300157', 'RULE20120000000000001', null, '32000000', 'ui测试-银保渠道', 'VKN75WVK-2', TO_DATE('2020-08-21 14:38:36', '%Y-%m-%d %H:%M:%S'), null, '1', '1', '1', '', TO_DATE('2020-08-21 14:36:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:37:37', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontracthis (id, acontracthisid, agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001766973, 1000000000607310, 1000000000545315, 1000000000196236, 1000000000072494, '32003J300157', 'RULE20120000000000001', null, '32000000', 'ui测试-银保渠道', 'VKN75WVK-2', TO_DATE('2020-08-21 14:38:36', '%Y-%m-%d %H:%M:%S'), null, '1', '1', null, '', TO_DATE('2020-08-21 14:37:36', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:37:36', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003331037, 1000000000034447, null, '329930020082100       ', '2 ', 22, 0, TO_DATE('2020-08-21 14:38:00', '%Y-%m-%d %H:%M:%S'), '1', '32000000  ', null, '          ', 'A320000135      ', null, null, null, null, null, null, TO_DATE('2020-08-21 14:38:00', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'B', null, TO_DATE('2020-08-21 14:36:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:36:58', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003331038, 1000000000034447, null, '329930020082100       ', '2 ', 23, 1, TO_DATE('2020-08-21 14:38:00', '%Y-%m-%d %H:%M:%S'), '1', null, null, '          ', 'A320000135      ', null, 22, null, '32000000  ', 'A320000135', null, TO_DATE('2020-08-21 14:38:29', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'C', 'ui测试', TO_DATE('2020-08-21 14:36:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:38:16', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontract (acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, creator, updator, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000196236, 'ui测试-银保渠道', '329930020082100', '300', TO_DATE('2020-08-21', '%Y-%m-%d'), TO_DATE('2024-08-28', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, 'A320000135', null, '          ', '1', null, null, TO_DATE('2020-08-21 14:36:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:37:36', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontractresult (contractresultid, agentname, acontractid, contractno, orgcode, permitno, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000162102, 'ui测试-银保渠道', 1000000000196236, '329930020082100', null, null, '11', TO_DATE('2020-08-21 14:38:32', '%Y-%m-%d %H:%M:%S'), null, null, 'A320000135', '1         ', null, null, TO_DATE('2020-08-21 14:37:35', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:37:35', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontracthis (id, acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, effecttime, failuretime, creator, updator, businessflag, updatetime, checkuser, checktime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000607310, 1000000000196236, 'ui测试-银保渠道', '329930020082100', '300', TO_DATE('2020-08-21', '%Y-%m-%d'), TO_DATE('2024-08-28', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, null, null, 'A320000135', 'A320000135', 'A', TO_DATE('2020-08-21 14:38:32', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-21 14:38:32', '%Y-%m-%d %H:%M:%S'), '          ', '1', null, null, TO_DATE('2020-08-21 14:37:36', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:37:36', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354801, 'ui测试-银保渠道', '交通银行', '1111113', '', '1', '1', 'BOCOM       ', '6540', '新疆维吾尔自治区_伊犁哈萨克自治州', '301898000032', '2', 'VKN75WVK-2', '1', '2', '2', '', '32000000', null, null, '1         ', null, null, TO_DATE('2020-08-21 14:35:25', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:37:47', '%Y-%m-%d %H:%M:%S'));

INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100000835, '32003L100007', '太原车商', '3200', '11', TO_DATE('2013-11-02 11:40:58', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000120', '1         ', null, null, TO_DATE('2013-11-02 10:40:09', '%Y-%m-%d %H:%M:%S'), TO_DATE('2013-11-02 10:40:09', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100003008, '32003L100007', 'asdasd', '3200', '11', TO_DATE('2014-03-04 16:29:57', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2014-03-04 16:08:38', '%Y-%m-%d %H:%M:%S'), TO_DATE('2014-03-04 16:08:38', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100003009, '32003L100007', 'asdasd', '3200', '21', TO_DATE('2014-03-04 16:32:48', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2014-03-04 16:11:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2014-03-04 16:11:28', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100003010, '32003L100007', 'asdasd', '3200', '21', TO_DATE('2014-03-04 16:38:43', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2014-03-04 16:26:10', '%Y-%m-%d %H:%M:%S'), TO_DATE('2014-03-04 16:26:10', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100004852, '32003L100007', 'asdasd', null, '31', TO_DATE('2015-01-14 09:55:13', '%Y-%m-%d %H:%M:%S'), '渠道码到期自动注销', 'A320000135', '00000000  ', '1         ', null, null, TO_DATE('2015-01-14 09:13:32', '%Y-%m-%d %H:%M:%S'), TO_DATE('2015-01-14 09:13:32', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100009600, '32003L100007', '测试breaking', '3200', '11', TO_DATE('2019-03-04 10:12:01', '%Y-%m-%d %H:%M:%S'), '123123', 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2019-03-04 10:08:11', '%Y-%m-%d %H:%M:%S'), TO_DATE('2019-03-04 10:08:11', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100009601, '32003L100007', '测试breaking', '3200', null, TO_DATE('2019-03-04 10:48:18', '%Y-%m-%d %H:%M:%S'), 'ty', 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2019-03-04 10:44:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2019-03-04 10:44:28', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100009670, '32003L100007', '测试breaking', null, '31', TO_DATE('2019-04-01 02:00:03', '%Y-%m-%d %H:%M:%S'), '渠道码到期自动注销', 'A320000135', '00000000  ', '1         ', null, null, TO_DATE('2019-03-31 23:50:11', '%Y-%m-%d %H:%M:%S'), TO_DATE('2019-03-31 23:50:11', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100025852, '32003L100007', 'ui测试-车商渠道', '3200', '21', TO_DATE('2020-08-21 14:57:54', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-21 14:56:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:56:58', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentresult (agentresultid, agentcode, agentname, comcode, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1100025853, '32003L100007', 'ui测试-车商渠道', '3200', '21', TO_DATE('2020-08-21 15:05:33', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-21 15:04:37', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 15:04:37', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontract (agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000545317, 1000000000196238, 1000000000072495, '32003L100007', 'RULE20120000000000001', null, '32990091', 'ui测试-车商渠道', 'EVDBPQOH-8 ', TO_DATE('2020-08-21 14:57:58', '%Y-%m-%d %H:%M:%S'), null, '1', '1', '1', '', TO_DATE('2020-08-21 14:55:37', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:57:00', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagentcontracthis (id, acontracthisid, agentcontractid, acontractid, agentid, agentcode, ruleno, batchno, comcode, secondname, orgcode, effecttime, failuretime, validstatus, deleteflag, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001766975, 1000000000607312, 1000000000545317, 1000000000196238, 1000000000072495, '32003L100007', 'RULE20120000000000001', null, '32990091', 'ui测试-车商渠道', 'EVDBPQOH-8 ', TO_DATE('2020-08-21 14:57:58', '%Y-%m-%d %H:%M:%S'), null, '1', '1', null, '', TO_DATE('2020-08-21 14:56:59', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:56:59', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003331053, 1000000000034454, null, '329930020082102       ', '2 ', 28, 0, TO_DATE('2020-08-21 14:56:39', '%Y-%m-%d %H:%M:%S'), '1', '32000000  ', null, '          ', 'A320000135      ', null, null, null, null, null, null, TO_DATE('2020-08-21 14:56:39', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'B', null, TO_DATE('2020-08-21 14:55:37', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:55:37', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sabpmmain (id, processid, taskid, businessno, businesstype, nodeid, businessnodeid, indate, state, comcode, handlerrole, usercode, handleruser, mobile, prepnodeid, preptaskid, prepcomcode, prepuser, pendingdate, outdate, acceptdate, acceptflag, valid, transactnodeid, cancelstate, canceldate, resumedate, canceluser, makecom, businessstatus, reason, inserttimeforhis, operatetimeforhis) VALUES (1000000003331054, 1000000000034454, null, '329930020082102       ', '2 ', 29, 1, TO_DATE('2020-08-21 14:56:39', '%Y-%m-%d %H:%M:%S'), '1', null, null, '          ', 'A320000135      ', null, 28, null, '32000000  ', 'A320000135', null, TO_DATE('2020-08-21 14:57:47', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '32000000', 'C', 'ui测试', TO_DATE('2020-08-21 14:55:37', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:57:38', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontract (acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, creator, updator, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000196238, 'ui测试-车商渠道', '329930020082102', '300', TO_DATE('2020-08-21', '%Y-%m-%d'), TO_DATE('2024-12-26', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, 'A320000135', null, '          ', '1', null, null, TO_DATE('2020-08-21 14:55:37', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:56:59', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontractresult (contractresultid, agentname, acontractid, contractno, orgcode, permitno, ispass, resultdate, reason, operateorcode, checkcode, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000162104, 'ui测试-车商渠道', 1000000000196238, '329930020082102', null, null, '11', TO_DATE('2020-08-21 14:57:50', '%Y-%m-%d %H:%M:%S'), null, null, 'A320000135', '1         ', null, null, TO_DATE('2020-08-21 14:56:57', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:56:57', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saacontracthis (id, acontractid, agentname, contractno, contracttype, startdate, enddate, comcode, orgcode, permitno, permitenddate, agentreferee, agentcontact, signusercode, channelusercode, agentphoneno, agentaddress, premiumtarget, createdate, lastcontractid, effecttime, failuretime, creator, updator, businessflag, updatetime, checkuser, checktime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000607312, 1000000000196238, 'ui测试-车商渠道', '329930020082102', '300', TO_DATE('2020-08-21', '%Y-%m-%d'), TO_DATE('2024-12-26', '%Y-%m-%d'), '32990091', null, null, null, '', '', null, null, '', '', null, TO_DATE('2020-08-21', '%Y-%m-%d'), null, null, null, 'A320000135', 'A320000135', 'A', TO_DATE('2020-08-21 14:57:50', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-21 14:57:50', '%Y-%m-%d %H:%M:%S'), '          ', '1', null, null, TO_DATE('2020-08-21 14:56:57', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:56:57', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001023331, '郑斯杰', '工商银行', '111111111111', '18606991583', '2', '1', 'ICBC        ', '3501', '福建省_福州市', '102391051207', '1', '350181199306141530', '1', '0', '0', '', '35118100', null, null, '0         ', null, null, TO_DATE('2017-08-31 16:54:09', '%Y-%m-%d %H:%M:%S'), TO_DATE('2017-10-31 16:08:45', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001223148, '辉南县农村信用合作联社营业部营业室', '农村信用社', '111111111111', '', '1', '3', 'RCU         ', '2205', '吉林省_通化市', '402245205088', '2', '59295539-5', '1', '2', '2', '', '22052300', null, null, '1         ', null, null, TO_DATE('2018-11-16 17:15:18', '%Y-%m-%d %H:%M:%S'), TO_DATE('2018-11-19 10:48:57', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354803, 'ui测试-车商渠道', '交通银行', '111111111111', '', '1', '1', 'BOCOM       ', '6540', '新疆维吾尔自治区_伊犁哈萨克自治州', '301898000032', '2', 'EVDBPQOH-8', '1', '2', '2', '', '32990091', null, null, '1         ', null, null, TO_DATE('2020-08-21 14:55:26', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 14:57:06', '%Y-%m-%d %H:%M:%S'));

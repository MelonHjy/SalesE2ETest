delete from sauuser where usercode = '83258604';
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002300817, '83258604  ', '唐澜品ui测试', 'C0        ', null, '420103199306120050', '01', '0', '1', '13333333333       ', null, '32990000', '1130B910000000000000', null, '32000000  ', '32990000', 'Y', 'P   ', '    ', null, null, null, '', '1', 'e         ', '', '0', '0         ', '          ', '', 'ok', TO_DATE('2020-08-10 11:09:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:52:42', '%Y-%m-%d %H:%M:%S'));

delete from sadaccount where accountid='1000000001354681';
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354681, '唐澜品ui测试', '中国农业银行股份有限公司', '4234567891011', '', '2', '1', 'ABC         ', '6590', '新疆维吾尔自治区_省直辖行政单位', '103885871592', '1', '420103199306120050', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-08-11 16:12:22', '%Y-%m-%d %H:%M:%S'), '0         ', null, null, TO_DATE('2020-08-10 11:09:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:52:43', '%Y-%m-%d %H:%M:%S'));

delete from sauusersub where userid='1000000002300817';
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001014013, 1000000002300817, '唐澜品ui测试', '01', TO_DATE('1993-06-12', '%Y-%m-%d'), '1', '01', '21', '', '', '      ', null, '', TO_DATE('2019-07-29', '%Y-%m-%d'), '0         ', null, null, null, '1', '', ' ', 'A320000135', TO_DATE('2020-08-10 11:09:28', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 16:12:22', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 16:13:53', '%Y-%m-%d %H:%M:%S'), null, '0         ', '', TO_DATE('2020-08-10 11:09:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:52:42', '%Y-%m-%d %H:%M:%S'));

delete from prpdsellerno where sellercode='83258604';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769438, '654321', '83258604  ', '唐澜品ui测试', '420103199306120050  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国农业银行股份有限公司', 'ABC         ', '1', '6590', '103885871592', '唐澜品ui测试', 'A', '420103199306120050', '13333333333', '4234567891011', null, null, null, '32000000', '0', null, null);

delete from	sadqualify where usercode = '83258604';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071469, '2', 1000000002300817, '83258604  ', null, null, 'Agent     ', 'A', '123456', TO_DATE('2018-08-05', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '0         ', null, null, TO_DATE('2020-08-10 11:09:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:52:42', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071470, '2', 1000000002300817, '83258604  ', null, null, 'Marketing ', ' ', '654321', TO_DATE('2018-08-06', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '0         ', null, null, TO_DATE('2020-08-10 11:09:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:52:43', '%Y-%m-%d %H:%M:%S'));

delete from sauuserrank where usercode = '83258604';
INSERT INTO sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182981, 1000000002300817, '83258604  ', '唐澜品ui测试', TO_DATE('2019-07-29', '%Y-%m-%d'), TO_DATE('2019-07-29', '%Y-%m-%d'), TO_DATE('2020-08-11', '%Y-%m-%d'), '32990000', '1130B910000000000000', null, null, null, null, null, '1', 'e', 'A320000135', TO_DATE('2020-08-11 16:13:59', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '0', null, '9', null, '人员界面手动注销', TO_DATE('2020-08-10 11:10:04', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:52:44', '%Y-%m-%d %H:%M:%S'));

delete from saucontract where usercode = '83258604';

delete from scmssalesinfosyn where usercode = '83258604';
INSERT INTO scmssalesinfosyn (id, usercode, groupusercode, procode, inductiondate, demissiondate, businessflag, synstatus, hbsynstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000766848, '83258604  ', '1132064100', '32000000  ', TO_DATE('2020-08-11', '%Y-%m-%d'), TO_DATE('2020-08-11', '%Y-%m-%d'), 'D', '0', '0', null, TO_DATE('2020-08-10 11:10:03', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 18:53:02', '%Y-%m-%d %H:%M:%S'));

delete from saugroupjob where usercode = '83258604';
delete from sabpmmain where businessno='83258604';
delete from sadqualifyhis where usercode = '83258604';
delete from saucontracthis  where usercode = '83258604';
delete from prpdsellernohis where sellercode='83258604';
delete from sauuserhistory where usercode = '83258604';
delete from saugroupjobhistory where usercode = '83258604';
delete from sauuserrankhis where usercode = '83258604';
delete from sainterfaceinfo where businessno in ('83258604','1000000001354681','1000000002300817');
delete from sauusersyn where usercode = '83258604';



-- SELECT * from sauuser where usercode = '83258604';
-- SELECT * from sadaccount where accountid='1000000001354681';
-- SELECT * from sauusersub where userid='1000000002300817';
-- SELECT * from prpdsellerno where sellercode='83258604';
-- SELECT * from sadqualify where usercode = '83258604';
-- SELECT * from sauuserrank where usercode = '83258604';
-- SELECT * from saucontract where usercode = '83258604';
-- SELECT * from scmssalesinfosyn where usercode = '83258604';
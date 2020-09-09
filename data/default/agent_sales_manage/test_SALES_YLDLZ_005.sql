
delete from sadaccount where accountid='1000000001354587';
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354587, '沈豪学ui测试', '中国工商银行股份有限公司', '111516512226', '', '2', '2', 'ICBC        ', '6528', '新疆维吾尔自治区_巴音郭楞蒙古自治州', '102888000030', '1', '440115199103253426', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-07-22 14:06:06', '%Y-%m-%d %H:%M:%S'), '1         ', null, null, TO_DATE('2020-07-21 16:54:27', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-07-22 14:06:11', '%Y-%m-%d %H:%M:%S'));

delete from sauusersub where userid='1000000002297787';
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001013931, 1000000002297787, '沈豪学ui测试', '99', TO_DATE('1991-03-25', '%Y-%m-%d'), '1', '01', '90', '', '', '      ', null, '', TO_DATE('2020-07-08', '%Y-%m-%d'), '0         ', null, null, null, '0', '', ' ', 'A320000135', TO_DATE('2020-07-21 16:54:22', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-07-22 14:06:06', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-07-22 10:49:13', '%Y-%m-%d %H:%M:%S'), null, '1         ', null, TO_DATE('2020-07-21 16:54:27', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 15:39:14', '%Y-%m-%d %H:%M:%S'));

delete from prpdsellerno where sellercode='83258554';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769356, '654321', '83258554  ', '沈豪学ui测试', '440115199103253426  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国工商银行股份有限公司', 'ICBC        ', '1', '6528', '102888000030', '沈豪学ui测试', 'A', '440115199103253426', '13311212125', '111516512226', null, null, null, '32000000', '1', null, null);

delete from	sadqualify where usercode = '83258554';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071311, '2', 1000000002297787, '83258554  ', null, null, 'Agent     ', 'B', '123456', TO_DATE('2019-01-01', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-07-21 16:54:27', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-07-22 13:38:17', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071312, '2', 1000000002297787, '83258554  ', null, null, 'Marketing ', ' ', '654321', TO_DATE('2019-02-02', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-07-21 16:54:27', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-07-22 13:38:17', '%Y-%m-%d %H:%M:%S'));

delete from sauuserrank where usercode = '83258554';
INSERT INTO sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182927, 1000000002297787, '83258554  ', '沈豪学ui测试', TO_DATE('2020-07-08', '%Y-%m-%d'), TO_DATE('2020-07-08', '%Y-%m-%d'), null, '32990038', '1130B9100000000HSK7C', null, null, null, null, null, '1', 'e', 'A320000135', TO_DATE('2020-07-22 10:49:17', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '1', null, '1', null, '人员新增同时增加职级。', TO_DATE('2020-07-22 10:49:21', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-07-22 10:49:21', '%Y-%m-%d %H:%M:%S'));

delete from saucontract where usercode = '83258554';
INSERT INTO saucontract (ucontractid, userid, ruleno, batchno, usercode, contractcount, contractno, contractstartdate, contractenddate, agentid, agentno, agentstartdate, agentenddate, credentialid, credentialno, credentstartdate, credentialenddate, effectivedate, contractaddress, guarantorname, guarantorcardnum, guarantoraddress, guarantorphone, comfeedate, agentarea, lastcontractid, effecttime, failuretime, creator, inputtime, updator, updatetime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001904219, 1000000002297787, 'RULE20120000000000001', null, '83258554  ', 1, '320000110200095     ', TO_DATE('2020-07-08', '%Y-%m-%d'), TO_DATE('2022-07-08', '%Y-%m-%d'), 1000000002071311, '123456                        ', TO_DATE('2019-01-01', '%Y-%m-%d'), null, 1000000002071312, '654321                        ', TO_DATE('2019-02-02', '%Y-%m-%d'), null, null, null, null, null, null, null, 0, null, null, TO_DATE('2020-07-22 10:49:15', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', TO_DATE('2020-07-21 16:54:25', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-07-21 17:02:52', '%Y-%m-%d %H:%M:%S'), '          ', '1         ', null, null, TO_DATE('2020-07-21 16:54:27', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-07-22 13:38:21', '%Y-%m-%d %H:%M:%S'));

delete from scmssalesinfosyn where usercode = '83258554';
INSERT INTO scmssalesinfosyn (id, usercode, groupusercode, procode, inductiondate, demissiondate, businessflag, synstatus, hbsynstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000766797, '83258554  ', '1132064046', '32000000  ', TO_DATE('2020-07-08', '%Y-%m-%d'), null, 'A', '1', '1', null, TO_DATE('2020-07-22 10:49:17', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-07-22 11:00:51', '%Y-%m-%d %H:%M:%S'));

delete from saugroupjob where usercode = '83258554';
insert into saugroupjob (groupcode, groupid, groupname, jobflag, pk_deptdoc, remark, roletype, usercode, username, validstatus, groupjobid) values ('1130B9100000000HSK7C', 1100000000560961, '测试0506营销', '0', '32990038', '', '1', '83258554', '沈豪学ui测试', '1', 1000001000000144);

delete from sauuser where usercode = '83258554';
/*插入基本信息*/
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002297787, '83258554  ', '沈豪学ui测试', 'C0        ', null, '440115199103253426', '11', '0', ' ', '13311212125       ', null, '32990038', '1130B9100000000HSK7C', null, '32000000  ', '32990038', 'Y', 'P   ', '    ', null, null, null, '', '0', '          ', '', '0', '1         ', '          ', '', 'ui测试', TO_DATE('2020-07-21 16:54:24', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 15:39:14', '%Y-%m-%d %H:%M:%S'));

delete from sabpmmain where businessno='83258554';
delete from sadqualifyhis where usercode = '83258554';
delete from saucontracthis  where usercode = '83258554';
delete from prpdsellernohis where sellercode='83258554';
delete from sauuserhistory where usercode = '83258554';
delete from saugroupjobhistory where usercode = '83258554';
delete from sauuserrankhis where usercode = '83258554';
delete from sainterfaceinfo where businessno in ('83258554','1000000001354587','1000000002297787');
delete from sauusersyn where usercode = '83258554';



-- SELECT * from sauuser where usercode = '83258554';
-- SELECT * from sadaccount where accountid='1000000001354587';
-- SELECT * from sauusersub where userid='1000000002297787';
-- SELECT * from prpdsellerno where sellercode='83258554';
-- SELECT * from sadqualify where usercode = '83258554';
-- SELECT * from sauuserrank where usercode = '83258554';
-- SELECT * from saucontract where usercode = '83258554';
-- SELECT * from scmssalesinfosyn where usercode = '83258554';
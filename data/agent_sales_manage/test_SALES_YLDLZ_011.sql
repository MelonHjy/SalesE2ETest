delete from sadaccount where accountid='1000000001354639';
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354639, '魏麟润ui测试', '中国工商银行股份有限公司', '119922292249', '', '2', '2', 'ICBC        ', '6528', '新疆维吾尔自治区_巴音郭楞蒙古自治州', '102888000030', '1', '430121198108207147', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-08-11 15:40:30', '%Y-%m-%d %H:%M:%S'), '1         ', null, null, TO_DATE('2020-07-30 10:45:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:43:05', '%Y-%m-%d %H:%M:%S'));

delete from sauusersub where userid='1000000002297848';
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001013977, 1000000002297848, '魏麟润ui测试', '01', TO_DATE('1981-08-20', '%Y-%m-%d'), '1', '03', '14', '', '', '      ', null, '', TO_DATE('2020-07-08', '%Y-%m-%d'), '0         ', '', null, null, '', '', ' ', 'A320000135', TO_DATE('2020-07-30 10:45:37', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 15:40:30', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-03 14:10:02', '%Y-%m-%d %H:%M:%S'), null, '1         ', '', TO_DATE('2020-07-30 10:45:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:40:37', '%Y-%m-%d %H:%M:%S'));

delete from prpdsellerno where sellercode='83258580';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769402, '654321', '83258580  ', '魏麟润ui测试', '430121198108207147  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国工商银行股份有限公司', 'ICBC        ', '1', '6528', '102888000030', '魏麟润ui测试', 'A', '430121198108207147', '13111111111       ', '119922292249', null, null, null, '32000000', '1', null, null);

delete from	sadqualify where usercode = '83258580';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071392, '2', 1000000002297848, '83258580  ', null, null, 'Agent     ', 'B', '123456', TO_DATE('2019-01-01', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-07-30 10:45:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:43:05', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071393, '2', 1000000002297848, '83258580  ', null, null, 'Marketing ', ' ', '654321', TO_DATE('2019-02-02', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-07-30 10:45:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:43:06', '%Y-%m-%d %H:%M:%S'));

delete from sauuserrank where usercode = '83258580';
INSERT INTO sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182954, 1000000002297848, '83258580  ', '魏麟润ui测试', TO_DATE('2020-07-08', '%Y-%m-%d'), TO_DATE('2020-07-08', '%Y-%m-%d'), null, '32990038', '1130B9100000000HSK7C', null, null, null, null, null, '1', 'e', 'A320000135', TO_DATE('2020-08-03 14:10:02', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '1', null, '1', null, '人员界面修改同时修改职级信息！！', TO_DATE('2020-08-03 14:09:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:43:01', '%Y-%m-%d %H:%M:%S'));

delete from saucontract where usercode = '83258580';
INSERT INTO saucontract (ucontractid, userid, ruleno, batchno, usercode, contractcount, contractno, contractstartdate, contractenddate, agentid, agentno, agentstartdate, agentenddate, credentialid, credentialno, credentstartdate, credentialenddate, effectivedate, contractaddress, guarantorname, guarantorcardnum, guarantoraddress, guarantorphone, comfeedate, agentarea, lastcontractid, effecttime, failuretime, creator, inputtime, updator, updatetime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001904270, 1000000002297848, 'RULE20120000000000001', null, '83258580  ', 1, '320000110200119     ', TO_DATE('2020-07-08', '%Y-%m-%d'), TO_DATE('2022-07-08', '%Y-%m-%d'), 1000000002071392, '123456                        ', TO_DATE('2019-01-01', '%Y-%m-%d'), null, 1000000002071393, '654321                        ', TO_DATE('2019-02-02', '%Y-%m-%d'), null, null, null, null, null, null, null, 0, null, null, TO_DATE('2020-08-03 14:10:02', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', TO_DATE('2020-07-30 10:45:38', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 15:43:02', '%Y-%m-%d %H:%M:%S'), '          ', '1         ', null, null, TO_DATE('2020-07-30 10:45:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:43:05', '%Y-%m-%d %H:%M:%S'));

delete from scmssalesinfosyn where usercode = '83258580';
INSERT INTO scmssalesinfosyn (id, usercode, groupusercode, procode, inductiondate, demissiondate, businessflag, synstatus, hbsynstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000766823, '83258580  ', '1132064075', '32000000  ', TO_DATE('2020-07-08', '%Y-%m-%d'), null, 'U', '1', '1', null, TO_DATE('2020-08-03 14:09:57', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:45:45', '%Y-%m-%d %H:%M:%S'));

delete from sauuser where usercode = '83258580';
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002297848, '83258580  ', '魏麟润ui测试', 'C0        ', null, '430121198108207147', '01', '1', '2', '13111111111       ', null, '32990038', '1130B9100000000HSK7C', null, '32000000  ', '32990038', 'N', 'P   ', '    ', null, null, null, '', '0', '          ', '', '0', '1         ', '          ', '', '123', TO_DATE('2020-07-30 10:45:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 15:43:01', '%Y-%m-%d %H:%M:%S'));

delete from sabpmmain where businessno='83258580';
delete from sadqualifyhis where usercode = '83258580';
delete from saucontracthis  where usercode = '83258580';
delete from prpdsellernohis where sellercode='83258580';
delete from sauuserhistory where usercode = '83258580';
delete from sauuserrankhis where usercode = '83258580';
delete from sainterfaceinfo where businessno in ('83258580','1000000002297848','1000000001354639');
delete from sauusersyn where usercode = '83258580';


-- SELECT * from sauuser where usercode = '83258580';
-- SELECT * from sadaccount where accountid='1000000001354639';
-- SELECT * from sauusersub where userid='1000000002297848';
-- SELECT * from prpdsellerno where sellercode='83258580';
-- SELECT * from sadqualify where usercode = '83258580';
-- SELECT * from sauuserrank where usercode = '83258580';
-- SELECT * from saucontract where usercode = '83258580';
-- SELECT * from scmssalesinfosyn where usercode = '83258580';
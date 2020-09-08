/*合同信息表*/
delete from saucontract where usercode = '83258549';
INSERT INTO saucontract (ucontractid, userid, ruleno, batchno, usercode, contractcount, contractno, contractstartdate, contractenddate, agentid, agentno, agentstartdate, agentenddate, credentialid, credentialno, credentstartdate, credentialenddate, effectivedate, contractaddress, guarantorname, guarantorcardnum, guarantoraddress, guarantorphone, comfeedate, agentarea, lastcontractid, effecttime, failuretime, creator, inputtime, updator, updatetime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001904342, 1000000002297781, 'RULE20120000000000001', null, '83258549  ', 2, '320000110200153     ', TO_DATE('2019-07-29', '%Y-%m-%d'), TO_DATE('2021-08-11', '%Y-%m-%d'), 1000000002071301, '123456                        ', TO_DATE('2019-01-01', '%Y-%m-%d'), null, 1000000002071302, '654321                        ', TO_DATE('2019-02-02', '%Y-%m-%d'), null, null, null, null, null, null, null, 0, null, null, TO_DATE('2020-08-07 16:33:34', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', TO_DATE('2020-08-07 16:33:12', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 10:26:07', '%Y-%m-%d %H:%M:%S'), '          ', '1         ', null, null, TO_DATE('2020-08-07 16:33:13', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:26:10', '%Y-%m-%d %H:%M:%S'));
/*资质表*/
delete from	sadqualify where usercode = '83258549';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071301, '2', 1000000002297781, '83258549  ', null, null, 'Agent     ', 'B', '123456', TO_DATE('2019-01-01', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-07-20 16:03:45', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:26:11', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071302, '2', 1000000002297781, '83258549  ', null, null, 'Marketing ', ' ', '654321', TO_DATE('2019-02-02', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-07-20 16:03:45', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:26:11', '%Y-%m-%d %H:%M:%S'));
/*职业证号表*/
delete from prpdsellerno where sellercode='83258549';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769351, '654321', '83258549  ', '曹栋牡ui测试', '430104198111197334  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国工商银行股份有限公司', 'ICBC        ', '1', '6528', '102888000030', '曹栋牡ui测试', 'A', '430104198111197334', '13311212122       ', '111222333447', null, null, null, '32000000', '1', null, null);
/*佣金系统营销员信息推送表*/
delete from scmssalesinfosyn where usercode = '83258549';
INSERT INTO scmssalesinfosyn (id, usercode, groupusercode, procode, inductiondate, demissiondate, businessflag, synstatus, hbsynstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000766795, '83258549  ', '1132064044', '32000000  ', TO_DATE('2019-07-29', '%Y-%m-%d'), null, 'U', '1', '1', null, TO_DATE('2020-07-22 10:14:58', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:30:44', '%Y-%m-%d %H:%M:%S'));

/*人员职级表*/
delete from sauuserrank where usercode = '83258549';
INSERT INTO sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182925, 1000000002297781, '83258549  ', '曹栋牡ui测试', TO_DATE('2019-07-29', '%Y-%m-%d'), null, TO_DATE('2020-08-07', '%Y-%m-%d'), '32990046', '1130B8100000000HT1XL', null, null, null, null, null, '1', 'a', 'A320000135', TO_DATE('2020-08-07 16:33:34', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-07-29 14:12:18', '%Y-%m-%d %H:%M:%S'), '1', '', '', 'ui测试', null, null, '1', null, '1', null, '人员界面修改同时修改职级信息！！', TO_DATE('2020-07-22 10:15:02', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:26:06', '%Y-%m-%d %H:%M:%S'));

/*职业证号表*/
delete from prpdsellerno where sellercode='83258549';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769351, '654321', '83258549  ', '曹栋牡ui测试', '430104198111197334  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国工商银行股份有限公司', 'ICBC        ', '1', '6528', '102888000030', '曹栋牡ui测试', 'A', '430104198111197334', '13311212122       ', '111222333447', null, null, null, '32000000', '1', null, null);

/*账户信息表*/
delete from sadaccount where accountid='1000000001354582';
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354582, '曹栋牡ui测试', '中国工商银行股份有限公司', '111222333447', '', '2', '2', 'ICBC        ', '6528', '新疆维吾尔自治区_巴音郭楞蒙古自治州', '102888000030', '1', '430104198111197334', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-08-11 10:23:22', '%Y-%m-%d %H:%M:%S'), '1         ', null, null, TO_DATE('2020-07-20 16:03:45', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:26:10', '%Y-%m-%d %H:%M:%S'));

/*主表*/
delete from sauuser where usercode = '83258549';
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002297781, '83258549  ', '曹栋牡ui测试', 'C0        ', null, '430104198111197334', '11', '0', '1', '13311212122       ', null, '32990046', '1130B8100000000HT1XL', null, '32000000  ', '32990046', 'Y', 'P   ', '    ', null, null, null, '', '1', '          ', '', '0', '1         ', '          ', '', '123456', TO_DATE('2020-07-20 16:03:42', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 10:26:06', '%Y-%m-%d %H:%M:%S'));


delete from sabpmmain where businessno='83258549';
delete from sadqualifyhis where usercode = '83258549';
delete from saucontracthis  where usercode = '83258549';
delete from prpdsellernohis where sellercode='83258549';
delete from sauuserhistory where usercode = '83258549';
delete from sauuserrankhis where usercode = '83258549';
-- delete from sauusersyn where usercode = '83258549';
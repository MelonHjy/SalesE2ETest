delete from sauuser where usercode = '83258600';
/*插入基本信息*/
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002300813, '83258600  ', '甘景媛ui测试', 'C0        ', null, '210101198503281148', '01', '0', '2', '13222222222       ', null, '32990000', '1130B910000000000000', null, '32000000  ', '32990000', 'Y', 'P   ', '    ', null, null, null, '', '0', '          ', '', '0', '1         ', '          ', '', 'ui测试', TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:25:33', '%Y-%m-%d %H:%M:%S'));

delete from sadaccount where accountid='1000000001354677';
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354677, '甘景媛ui测试', '中国建设银行股份有限公司', '3234567891011', '', '2', '1', 'CCB         ', '1100', '北京市_北京市', '105100001052', '1', '210101198503281148', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-08-10 11:23:46', '%Y-%m-%d %H:%M:%S'), '1         ', null, null, TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:25:35', '%Y-%m-%d %H:%M:%S'));

delete from sauusersub where userid='1000000002300813';
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001014009, 1000000002300813, '甘景媛ui测试', '01', TO_DATE('1985-03-28', '%Y-%m-%d'), '1', '01', '17', '', '', '      ', null, '', TO_DATE('2019-08-05', '%Y-%m-%d'), '0         ', null, null, null, '0', '', ' ', 'A320000135', TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-10 11:23:46', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-07 14:01:01', '%Y-%m-%d %H:%M:%S'), null, '1         ', null, TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:25:26', '%Y-%m-%d %H:%M:%S'));

delete from prpdsellerno where sellercode='83258600';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769434, '654321', '83258600  ', '甘景媛ui测试', '210101198503281148  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国建设银行股份有限公司', 'CCB         ', '1', '1100', '105100001052', '甘景媛ui测试', 'A', '210101198503281148', '13222222222       ', '3234567891011', null, null, null, '32000000', '1', null, null);

delete from	sadqualify where usercode = '83258600';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071463, '2', 1000000002300813, '83258600  ', null, null, 'Agent     ', 'A', '123456', TO_DATE('2018-08-06', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:25:35', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071464, '2', 1000000002300813, '83258600  ', null, null, 'Marketing ', ' ', '654321', TO_DATE('2018-08-28', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:25:35', '%Y-%m-%d %H:%M:%S'));

delete from sauuserrank where usercode = '83258600';
INSERT INTO sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182979, 1000000002300813, '83258600  ', '甘景媛ui测试', TO_DATE('2019-08-05', '%Y-%m-%d'), null, null, '32990000', '1130B910000000000000', null, null, null, null, null, '1', 'e', 'A320000135', TO_DATE('2020-08-07 14:01:01', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-10 14:17:38', '%Y-%m-%d %H:%M:%S'), '1', '', '', 'ui测试', null, null, '1', null, '1', null, '手动定级为营销团队经理审核通过！！', TO_DATE('2020-08-07 14:01:03', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 14:17:38', '%Y-%m-%d %H:%M:%S'));

delete from saucontract where usercode = '83258600';
INSERT INTO saucontract (ucontractid, userid, ruleno, batchno, usercode, contractcount, contractno, contractstartdate, contractenddate, agentid, agentno, agentstartdate, agentenddate, credentialid, credentialno, credentstartdate, credentialenddate, effectivedate, contractaddress, guarantorname, guarantorcardnum, guarantoraddress, guarantorphone, comfeedate, agentarea, lastcontractid, effecttime, failuretime, creator, inputtime, updator, updatetime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001904340, 1000000002300813, 'RULE20120000000000001', null, '83258600  ', 1, '320000110200151     ', TO_DATE('2019-08-05', '%Y-%m-%d'), TO_DATE('2021-08-17', '%Y-%m-%d'), 1000000002071463, '123456                        ', TO_DATE('2018-08-06', '%Y-%m-%d'), null, 1000000002071464, '654321                        ', TO_DATE('2018-08-28', '%Y-%m-%d'), null, null, null, null, null, null, null, 0, null, null, TO_DATE('2020-08-07 14:01:01', '%Y-%m-%d %H:%M:%S'), null, 'A320000135', TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-10 11:25:31', '%Y-%m-%d %H:%M:%S'), '          ', '1         ', null, null, TO_DATE('2020-08-07 10:55:47', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:25:35', '%Y-%m-%d %H:%M:%S'));

delete from scmssalesinfosyn where usercode = '83258600';
INSERT INTO scmssalesinfosyn (id, usercode, groupusercode, procode, inductiondate, demissiondate, businessflag, synstatus, hbsynstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000766845, '83258600  ', '1132064099', '32000000  ', TO_DATE('2019-08-05', '%Y-%m-%d'), null, 'U', '1', '1', null, TO_DATE('2020-08-07 14:01:02', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 11:30:45', '%Y-%m-%d %H:%M:%S'));

delete from sabpmmain where businessno='83258600';
delete from sadqualifyhis where usercode = '83258600';
delete from saucontracthis  where usercode = '83258600';
delete from prpdsellernohis where sellercode='83258600';
delete from sauuserhistory where usercode = '83258600';
delete from saugroupjobhistory where usercode = '83258600';
delete from sauuserrankhis where usercode = '83258600';
delete from sainterfaceinfo where businessno in ('83258600','1000000001354677','1000000002300813');
delete from saugroupjob where usercode = '83258600';
delete from sauusersyn where usercode = '83258600';


-- SELECT * from sauuser where usercode = '83258600';
-- SELECT * from sadaccount where accountid='1000000001354677';
-- SELECT * from sauusersub where userid='1000000002300813';
-- SELECT * from prpdsellerno where sellercode='83258600';
-- SELECT * from sadqualify where usercode = '83258600';
-- SELECT * from sauuserrank where usercode = '83258600';
-- SELECT * from saucontract where usercode = '83258600';
-- SELECT * from scmssalesinfosyn where usercode = '83258600';
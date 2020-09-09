delete from sabpmmain where businessno='83258605';
delete from sauuserhistory where usercode ='83258605';
delete from sadqualifyhis where usercode='83258605';
delete from saucontracthis where usercode='83258605';
delete from prpdsellernohis where SellerCode='83258605';
delete from sauuserrankhis where usercode='83258605';
-- delete from sauusersyn where usercode = '83258605';
delete from sainterfaceinfo where businessno=('83258605');

/*合同信息表*/
delete from saucontract where usercode='83258605';
INSERT INTO saucontract (ucontractid, userid, ruleno, batchno, usercode, contractcount, contractno, contractstartdate, contractenddate, agentid, agentno, agentstartdate, agentenddate, credentialid, credentialno, credentstartdate, credentialenddate, effectivedate, contractaddress, guarantorname, guarantorcardnum, guarantoraddress, guarantorphone, comfeedate, agentarea, lastcontractid, effecttime, failuretime, creator, inputtime, updator, updatetime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001904349, 1000000002300818, 'RULE20120000000000001', null, '83258605  ', 1, '320000110200156     ', TO_DATE('2019-08-14', '%Y-%m-%d'), TO_DATE('2021-08-25', '%Y-%m-%d'), 1000000002071471, '123456                        ', TO_DATE('2018-08-06', '%Y-%m-%d'), null, 1000000002071472, '654321                        ', TO_DATE('2018-08-06', '%Y-%m-%d'), null, null, null, null, null, null, null, 0, null, null, TO_DATE('2020-08-10 16:47:27', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-10 16:51:02', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), null, null, '          ', '0         ', null, null, TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:21:45', '%Y-%m-%d %H:%M:%S'));

/*人员基本信息附表*/
delete from sauusersub where UserID =(select userid from sauuser where usercode='83258605');
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001014014, 1000000002300818, '施仪仪ui测试', '01', TO_DATE('2000-03-02', '%Y-%m-%d'), '1', '01', '21', '', '', '      ', null, '', TO_DATE('2019-08-14', '%Y-%m-%d'), '0         ', null, null, null, '0', '', ' ', 'A320000135', TO_DATE('2020-08-10 15:56:04', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 16:21:30', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-11 16:22:48', '%Y-%m-%d %H:%M:%S'), null, '1         ', 'ui测试', TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:22:58', '%Y-%m-%d %H:%M:%S'));

/*人员职级表*/
delete from Sauuserrank where usercode='83258605';
INSERT INTO Sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182982, 1000000002300818, '83258605  ', '施仪仪ui测试', TO_DATE('2019-08-14', '%Y-%m-%d'), TO_DATE('2019-08-14', '%Y-%m-%d'), null, '32990000', '1130B910000000000000', null, null, null, null, null, '1', 'a', 'A320000135', TO_DATE('2020-08-11 16:22:54', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '1', null, '1', null, '失效后复效。', TO_DATE('2020-08-10 16:47:28', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:22:54', '%Y-%m-%d %H:%M:%S'));

delete from sadqualify where usercode='83258605';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071471, '2', 1000000002300818, '83258605  ', null, null, 'Agent     ', 'A', '123456', TO_DATE('2018-08-06', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:22:53', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071472, '2', 1000000002300818, '83258605  ', null, null, 'Marketing ', ' ', '654321', TO_DATE('2018-08-06', '%Y-%m-%d'), null, 'A320000135', 'A320000135', '1         ', null, null, TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:22:53', '%Y-%m-%d %H:%M:%S'));

delete from prpdsellerno where SellerCode='83258605';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769439, '654321', '83258605  ', '施仪仪ui测试', '410104200003025785  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国建设银行股份有限公司', 'CCB         ', '1', '6531', '105894000051', '施仪仪ui测试', 'A', '410104200003025785', '13444444444', '123123123123123', null, null, null, '32000000', '1', null, null);

delete from sadaccount where IdentifyNumber='410104200003025785';
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354682, '施仪仪ui测试', '中国建设银行股份有限公司', '123123123123123', '', '2', '1', 'CCB         ', '6531', '新疆维吾尔自治区_喀什地区', '105894000051', '1', '410104200003025785', '1', '0', '0', '', '32000000', 'A320000135', TO_DATE('2020-08-11 16:21:30', '%Y-%m-%d %H:%M:%S'), '1         ', null, null, TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:22:58', '%Y-%m-%d %H:%M:%S'));

delete from sauuserhistory where usercode='83258605';
INSERT INTO sauuserhistory (historyid, updatetime, operator, userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, businessflag, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis, squadid, squadvalidstatus) VALUES (1109503922, null, null, 1000000002300818, '83258605  ', '施仪仪ui测试', 'C0        ', null, '410104200003025785', '01', '0', '2', '13444444444       ', null, '32990000', '1130B910000000000000', null, '32000000  ', '32990000', 'Y', 'P   ', '    ', null, null, null, '', 'D', '0', '          ', '', '0', '1         ', '          ', '', '和', TO_DATE('2020-08-11 16:21:39', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:23:10', '%Y-%m-%d %H:%M:%S'), null, null);

delete from sauuser where usercode='83258605';
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002300818, '83258605  ', '施仪仪ui测试', 'C0        ', null, '410104200003025785', '01', '0', '2', '13444444444       ', null, '32990000', '1130B910000000000000', null, '32000000  ', '32990000', 'Y', 'P   ', '    ', null, null, null, '', '0', 'e ', '', '0', '0         ', '          ', '', 'ui测试', TO_DATE('2020-08-10 15:56:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-11 16:22:49', '%Y-%m-%d %H:%M:%S'));


-- 查询
-- select * from sabpmmain where businessno='83258605';
-- select * from sauuserhistory where usercode ='83258605'
-- select * from sadqualifyhis where usercode='83258605'
-- select * from SaUContractHis where UserCode='83258605'
-- select * from prpdsellernohis where SellerCode='83258605'
-- select * from sauuserrankhis where usercode='83258605'
-- select * from saucontract where usercode ='83258605'
-- select * from sauusersub where UserID =(select userid from sauuser where usercode='83258605  ')
-- select * from  Sauuserrank where usercode='83258605'
-- select * from sadqualify where usercode='83258605';
-- select * from prpdsellerno where SellerCode='83258605';
-- select * from sauuser where  usercode ='83258605'
-- select * from sadaccount where IdentifyNumber='410104200003025785'
-- select * from sauuserhistory where usercode='83258555  ';
-- select * from sauuserhistory where usercode='83258605  ';
-- select * from sabpmmain where businessno='83258605  ';
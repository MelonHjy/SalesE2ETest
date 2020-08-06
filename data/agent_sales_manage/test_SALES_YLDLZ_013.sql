--数据准备
--1、清理数据并准备数据
--step1.删除sauuser和sauusersub表数据并插入准备数据
delete sauuser where usercode ='83258491';
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002297685, '83258491  ', '测试专职经理', 'C0        ', null, '420101200009101737', '01', '0', '1', '13232245654       ', null, '32012207', '1131V51000000000R42X', null, '32012200  ', '32012207', 'Y', 'P   ', '    ', null, null, null, '', '1', '          ', '', '0', '1         ', '          ', '', '不同意', TO_DATE('2020-06-18 14:52:04', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-06 14:19:46', '%Y-%m-%d %H:%M:%S'));
delete sauusersub where userid ='1000000002297685';
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001013849, 1000000002297685, '测试专职经理', '02', TO_DATE('2000-09-10', '%Y-%m-%d'), '2', '03', '11', '3', '333', '333232', null, '6530@163.com', TO_DATE('2020-06-18', '%Y-%m-%d'), '2         ', null, null, null, '', '', ' ', 'A320101030', TO_DATE('2020-06-18 14:51:59', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-06 14:08:32', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-06 14:09:29', '%Y-%m-%d %H:%M:%S'), null, '1         ', null, TO_DATE('2020-06-18 14:52:11', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-06 14:19:46', '%Y-%m-%d %H:%M:%S'));

--插入附表数据
--step2删除并插入资格证和执业证sadqualify
delete sadqualify where usercode = '83258491';
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071144, '2', 1000000002297685, '83258491  ', null, null, 'Agent     ', 'A', '322676237887376', TO_DATE('2020-06-01', '%Y-%m-%d'), null, 'A320101030', 'A320101030', '0         ', null, null, TO_DATE('2020-06-18 14:52:11', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:22', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadqualify (qualifyid, isprivate, userid, usercode, agentid, agentcode, qualifytype, agenttype, qualifyno, qualifystartdate, qualifyenddate, creator, updator, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002071145, '2', 1000000002297685, '83258491  ', null, null, 'Marketing ', ' ', '2662662873372', TO_DATE('2020-06-01', '%Y-%m-%d'), null, 'A320101030', 'A320101030', '0         ', null, null, TO_DATE('2020-06-18 14:52:11', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:23', '%Y-%m-%d %H:%M:%S'));

--step3清理合同、账户、职级主表和历史信息，并插入合同、账户、职级信息
delete saucontract where usercode = '83258491';
delete sadaccount where accountid=1000000001354474;
delete sauuserrank where usercode = '83258491';
delete sauuserrankhis where usercode = '83258491';
delete SaUContractHis where usercode =  '83258491';
delete sadqualifyhis where usercode = '83258491';
delete prpdsellernohis where  sellercode = '83258491';


INSERT INTO saucontract (ucontractid, userid, ruleno, batchno, usercode, contractcount, contractno, contractstartdate, contractenddate, agentid, agentno, agentstartdate, agentenddate, credentialid, credentialno, credentstartdate, credentialenddate, effectivedate, contractaddress, guarantorname, guarantorcardnum, guarantoraddress, guarantorphone, comfeedate, agentarea, lastcontractid, effecttime, failuretime, creator, inputtime, updator, updatetime, checkstatus, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001904135, 1000000002297685, 'RULE20203201000000080', null, '83258491  ', 1, '320122110200004     ', TO_DATE('2020-06-18', '%Y-%m-%d'), TO_DATE('2023-05-29', '%Y-%m-%d'), 1000000002071144, '322676237887376               ', TO_DATE('2020-06-01', '%Y-%m-%d'), null, 1000000002071145, '2662662873372                 ', TO_DATE('2020-06-01', '%Y-%m-%d'), null, null, null, null, null, null, null, 0, null, null, TO_DATE('2020-06-18 15:03:08', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:21', '%Y-%m-%d %H:%M:%S'), 'A320101030', TO_DATE('2020-06-18 14:52:09', '%Y-%m-%d %H:%M:%S'), 'A320101030', TO_DATE('2020-06-18 15:13:52', '%Y-%m-%d %H:%M:%S'), '          ', '0         ', null, null, TO_DATE('2020-06-18 14:52:12', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:23', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sadaccount (accountid, payeename, bankname, accountno, telephone, isprivate, cardtype, bankcode, bankareacode, bankareaname, cnaps, identifytype, identifynumber, pressing, sendsms, sendmail, email, comcode, updator, updatetime, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000001354474, '测试专职经理', '中国农业银行股份有限公司', '443323232387487378', '', '2', '1', 'ABC         ', '1100', '北京市_北京市', '103100011215', '1', '420101200009101737', '1', '0', '0', '', '32012200', 'A320101030', TO_DATE('2020-06-18 15:08:57', '%Y-%m-%d %H:%M:%S'), '0         ', null, null, TO_DATE('2020-06-18 14:52:12', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:23', '%Y-%m-%d %H:%M:%S'));
INSERT INTO sauuserrank (userrankid, userid, usercode, username, entrydate, effectdate, demissiondate, comcode, groupcode, perrpremium, perspremium, grouprpremium, groupsize, groupgrownsize, crossinteractrate, userrank, operatercode, operatedate, auditusercode, audittime, auditstatus, filecode, filename, operationreason, operationday, extendtime, validstatus, flag, renew, symbol, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000002182880, 1000000002297685, '83258491  ', '测试专职经理', TO_DATE('2020-06-18', '%Y-%m-%d'), TO_DATE('2020-06-18', '%Y-%m-%d'), TO_DATE('2020-08-05', '%Y-%m-%d'), '32012207', '1131V51000000000R42X', null, null, null, null, null, '1', 'e', 'A320000135', TO_DATE('2020-06-18 15:03:09', '%Y-%m-%d %H:%M:%S'), null, null, '1', null, null, null, null, null, '0', null, '9', null, '人员界面手动注销', TO_DATE('2020-06-18 15:03:15', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:24', '%Y-%m-%d %H:%M:%S'));

--step4 职业证号表prpdsellerno删除并插入
delete prpdsellerno  where sellercode = '83258491';
INSERT INTO prpdsellerno (id, sellerno, sellercode, sellername, identifynumber, sellernotime, sellertype, businessnature, agentcode, agentname, bankname, bankcode, companyflag, localflag, unionpayno, accountname, certitype, certino, phoneno, payaccount, salary, lastpremium, pretarget, comcode, validstatus, remark, flag) VALUES (1000000000769270, '2662662873372', '83258491  ', '测试专职经理', '420101200009101737  ', null, 'C22 ', '1', '000011000001', '保险营销员', '中国农业银行股份有限公司', 'ABC         ', '1', '1100', '103100011215', '测试专职经理', 'A', '420101200009101737', '13232245654       ', '443323232387487378', null, null, null, '32012200', '0', null, null);

--step5删除SaUGroupJobHistory团队职位轨迹表数据
delete saugroupjobhistory where usercode = '83258491';

--step6团队职位表删除并插入
delete saugroupjob where usercode = '83258491';
INSERT INTO saugroupjob (groupjobid, groupid, pk_deptdoc, groupcode, groupname, usercode, username, roletype, jobflag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000001000000094, 1000000000056060, '32012207', '1131V51000000000R42X', '南京市浦口支公司营销业务部', '83258491', '测试专职经理', '1', '0', '0', null, TO_DATE('2020-06-18 15:03:50', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-05 14:09:39', '%Y-%m-%d %H:%M:%S'));
--step7 清空佣金系统营销员信息推送表
delete scmssalesinfosyn where usercode = '83258491';
--step8 清空人员清分表数据
delete sauusersyn where usercode =  '83258491';
--step9.删除主表信息sabpmmain
delete sabpmmain where businessno = '83258491';
--step10.删除人员修改历史表数据
delete sauuserhistory where usercode = '83258491';




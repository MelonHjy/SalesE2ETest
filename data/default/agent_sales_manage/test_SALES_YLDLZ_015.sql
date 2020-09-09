delete from sabpmmain where businessno='32748460';
delete from sauuserhistory where UserCode='32748460';
delete from sadqualifyhis where usercode='32748460';
delete from prpdsellernohis where SellerCode='32748460';
delete from sadqualify where UserCode='32748460';
delete from sadaccount  where IdentifyNumber='320123195508160214';
delete from saucontract where UserCode='32748460';
delete from sainterfaceinfo where businessno in('32748460','1000000000028821');
delete from scmssalesinfosyn where usercode='32748460';
delete from sauuserrank where usercode='32748460';
delete from sauuserrankhis where usercode='32748460';
delete from sauusersyn where usercode='32748460';
delete from saucontracthis where usercode='32748460';
delete from prpdsellerno where SellerCode='32748460';

delete from sauusersub where userid=(select userid from sauuser where identifynumber='320123195508160214');
INSERT INTO sauusersub (usersubid, userid, username, nation, birthday, marriage, visage, culture, nativeplace, address, postcode, phone, email, piccdate, unitlevel, position, effectdate, levelcode, rolecode, peopleid, peoplecheck, creator, inputtime, updator, updatetime, auditinguser, auditingdate, flag, validstatus, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000362688, 1000000000028821, '王先福', '01', TO_DATE('1955-08-16', '%Y-%m-%d'), '1', '01', '21', '', '', '      ', null, '', TO_DATE('2019-08-06', '%Y-%m-%d'), '0         ', null, null, null, '', '', ' ', null, null, 'A320000135', TO_DATE('2020-08-12 11:27:28', '%Y-%m-%d %H:%M:%S'), 'A320000135', TO_DATE('2020-08-12 11:29:10', '%Y-%m-%d %H:%M:%S'), null, '0         ', '', TO_DATE('2014-11-28 15:13:23', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-12 11:29:18', '%Y-%m-%d %H:%M:%S'));

delete from sauuser where usercode='32748460';
INSERT INTO sauuser (userid, usercode, username, usertype, userclass, identifynumber, identifytype, disability, sex, mobile, groupid, pk_deptdoc, groupcode, comflag, comcode, makecom, tradetype, firomjob, secomjob, omjobeffctdate, fulltime, failtime, dismissreason, deleteflag, checkstatus, refereecode, onlineincreaseflag, validstatus, flag, message, remark, inserttimeforhis, operatetimeforhis) VALUES (1000000000028821, '32748460  ', '王先福', 'B0        ', '1', '320123195508160214', '01', null, '1', '13913351960       ', null,  null, null, 0,  null,  null, null, null, null, null, null, null, '已辞职', '0', 'e         ', null, null, '0         ', null, null, '人员转制-（团队成员出单权赋予）-ui测试', TO_DATE('2012-06-21 16:37:40', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-12 11:29:10', '%Y-%m-%d %H:%M:%S'));


-- select * from sabpmmain where businessno=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sauuserhistory where IdentifyNumber='320123195508160214'
-- select * from sadqualifyhis where businessno=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from prpdsellernohis where IdentifyNumber='320123195508160214'
-- select * from sadqualify where UserCode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sadaccount  where IdentifyNumber='320123195508160214'
-- select * from saucontract where UserCode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sainterfaceinfo where businessno in('32748460','1000000000028821')
-- select * from scmssalesinfosyn where usercode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sauuserrank where usercode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sauuserrankhis where usercode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sauusersyn where usercode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from saucontracthis where usercode=(select usercode from sauuser where identifynumber='320123195508160214')
-- select * from sauusersub where userid=(select userid from sauuser where identifynumber='320123195508160214')
-- select * from prpdsellerno where identifynumber='320123195508160214'
-- select * from sauuser where identifynumber='320123195508160214'
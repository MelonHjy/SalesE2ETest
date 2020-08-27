--个代
delete from saaagenttyperesult where agenttype='21300L';
INSERT INTO saaagenttyperesult (id, agenttype, agenttypename, operatetime, operateorcode, approvetime, approvercode, reason, agenttypestatus, flag) VALUES (1000000000007806, '21300L', '个代ui测试-011', TO_DATE('2020-08-25', '%Y-%m-%d'), 'A320000135', TO_DATE('2020-08-25', '%Y-%m-%d'), 'A000008254', 'ui测试-个代渠道码作废数据', '1 ', null);
delete from sapagenttype where NEWAGENTTYPE='21300L';
INSERT INTO sapagenttype (agenttypename, NEWAGENTTYPE,operatetimeforhis,validstatus, agenttypecode) values ('个代ui测试-011','21300L',TO_DATE('2020-08-25 16:21:37', '%Y-%m-%d %H:%M:%S'),'1','21300L      ');
delete from saaagenttype where newAgentType='21300L';
insert into saaagenttype (agenttypename, flag, newAgentType, remark, validstatus, agenttypecode) values ('个代ui测试-011', '', '21300L      ', '', '1', '21300L      ');

--经商
delete from saaagenttyperesult where agenttype='2111CM';
delete from sapagenttype where NEWAGENTTYPE='2111CM';
delete from saaagenttype where newAgentType='2111CM';
INSERT INTO saaagenttyperesult (id, agenttype, agenttypename, operatetime, operateorcode, approvetime, approvercode, reason, agenttypestatus, flag) VALUES (1000000000007893, '2111CM', '经代ui测试-011', TO_DATE('2020-08-27', '%Y-%m-%d'), 'A320000135', TO_DATE('2020-08-27', '%Y-%m-%d'), 'A000008254', 'ui测试-渠道类型码作废数据', '1 ', null);
INSERT INTO sapagenttype (agenttypecode, agenttypename, newagenttype, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES ('2111CM      ', '经代ui测试-011', '2111CM      ', '1', null, null, TO_DATE('2020-08-27 13:51:05', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-27 13:51:36', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagenttype (agenttypecode, agenttypename, newagenttype, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES ('2111CM      ', '经代ui测试-011', '2111CM      ', '1', '4N        ', null, TO_DATE('2020-08-27 13:51:36', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-27 13:51:36', '%Y-%m-%d %H:%M:%S'));

--银保
delete from saaagenttyperesult where agenttype='2111CL';
delete from sapagenttype where NEWAGENTTYPE='2111CL';
delete from saaagenttype where newAgentType='2111CL';
INSERT INTO saaagenttyperesult (id, agenttype, agenttypename, operatetime, operateorcode, approvetime, approvercode, reason, agenttypestatus, flag) VALUES (1000000000007884, '2111CL', '银保ui测试-011', TO_DATE('2020-08-27', '%Y-%m-%d'), 'A320000135', TO_DATE('2020-08-27', '%Y-%m-%d'), 'A000008254', 'ui测试-渠道类型码作废', '1 ', null);
INSERT INTO sapagenttype (agenttypecode, agenttypename, newagenttype, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES ('2111CL      ', '银保ui测试-011', '2111CL      ', '1', null, null, TO_DATE('2020-08-27 11:22:35', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-27 11:23:04', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagenttype (agenttypecode, agenttypename, newagenttype, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES ('2111CL      ', '银保ui测试-011', '2111CL      ', '1', '4N        ', null, TO_DATE('2020-08-27 11:23:04', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-27 11:23:04', '%Y-%m-%d %H:%M:%S'));

--车商
delete from saaagenttyperesult where agenttype='2111CK';
delete from sapagenttype where NEWAGENTTYPE='2111CK';
delete from saaagenttype where newAgentType='2111CK';
INSERT INTO saaagenttyperesult (id, agenttype, agenttypename, operatetime, operateorcode, approvetime, approvercode, reason, agenttypestatus, flag) VALUES (1000000000007882, '2111CK', '车商ui测试-011', TO_DATE('2020-08-27', '%Y-%m-%d'), 'A320000135', TO_DATE('2020-08-27', '%Y-%m-%d'), 'A000008254', 'ui测试-车商渠道类型码作废', '1 ', null);
INSERT INTO sapagenttype (agenttypecode, agenttypename, newagenttype, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES ('2111CK      ', '车商ui测试-011', '2111CK      ', '1', null, null, TO_DATE('2020-08-27 11:05:54', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-27 11:06:26', '%Y-%m-%d %H:%M:%S'));
INSERT INTO saaagenttype (agenttypecode, agenttypename, newagenttype, validstatus, flag, remark, inserttimeforhis, operatetimeforhis) VALUES ('2111CK      ', '车商ui测试-011', '2111CK      ', '1', '4N        ', null, TO_DATE('2020-08-27 11:06:26', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-27 11:06:26', '%Y-%m-%d %H:%M:%S'));

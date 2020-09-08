delete from saaagentresult where agentcode=(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介004');
delete from sainterfaceinfo where businessno=(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介银保004')
delete from sainterfaceinfo where businessno=(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介004');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111110');
delete from saaagentcontract where acontractid=(select acontractid from saacontract where agentname='ui测试-中介004');
delete from saaagentcontracthis where acontractid=(select acontractid from saacontract where agentname='ui测试-中介004');
delete from sabpmmain where businessno=(select contractno from saacontract where agentname='ui测试-中介004');
delete from saacontract where agentname='ui测试-中介004';
delete from saacontractresult where agentname='ui测试-中介004';
delete from saacontracthis where agentname='ui测试-中介004';
delete from sadaccount where accountno='1111110';
delete from saaagenthis where agentname='ui测试-中介01';
INSERT INTO saaagenthis (id, agentid, agentcode, agentname, agenttype, permitno, permitenddate, socicredcode, orgcode, contractno, linkername, postcode, address, phonenumber, faxnumber, upperagentcode, groupcode, comcode, creator, updator, checkstatus, validstatus, flag, taxpayertype, invoicetype, remark, businessflag, upduser, updcomcode, checkuser, checkcomcode, inserttimeforhis, operatetimeforhis) VALUES (1000000000111127, 1000000000072491, '32003J200040', 'ui测试-中介01', '3J2001', '123456', TO_DATE('2023-08-30', '%Y-%m-%d'), '', 'P8THLLKR-X ', null, '', '      ', '佛山市', '', '', '            ', '                    ', '32000000', 'A320000135', 'A320000135', '21        ', '0', null, ' ', ' ', null, 'U', 'A320000135', '32000000', null, null, TO_DATE('2020-08-21 10:49:01', '%Y-%m-%d %H:%M:%S'), TO_DATE('2020-08-21 10:49:01', '%Y-%m-%d %H:%M:%S'));



delete from saaagentresult where agentcode=(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介经代004');
delete from sainterfaceinfo where businessno=(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介经代004')
delete from sainterfaceinfo where businessno=(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介经代004');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111112');
delete from saaagentcontract where acontractid=(select acontractid from saacontract where agentname='ui测试-中介经代004');
delete from saaagentcontracthis where acontractid=(select acontractid from saacontract where agentname='ui测试-中介经代004');
delete from sabpmmain where businessno=(select contractno from saacontract where agentname='ui测试-中介经代004');
delete from saacontract where agentname='ui测试-中介经代004';
delete from saacontractresult where agentname='ui测试-中介经代004';
delete from saacontracthis where agentname='ui测试-中介经代004';
delete from sadaccount where accountno='1111112';


delete from saaagentresult where agentcode=(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介银保004');
delete from sainterfaceinfo where businessno=(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介银保004')
delete from sainterfaceinfo where businessno=(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介银保004');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111114');
delete from saaagentcontract where acontractid=(select acontractid from saacontract where agentname='ui测试-中介银保004');
delete from saaagentcontracthis where acontractid=(select acontractid from saacontract where agentname='ui测试-中介银保004');
delete from sabpmmain where businessno=(select contractno from saacontract where agentname='ui测试-中介银保004');
delete from saacontract where agentname='ui测试-中介银保004';
delete from saacontractresult where agentname='ui测试-中介银保004';
delete from saacontracthis where agentname='ui测试-中介银保004';
delete from sadaccount where accountno='1111114';



delete from saaagentresult where agentcode=(select a.agentcode from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介车商004-1');
delete from sainterfaceinfo where businessno=(select to_char(a.agentid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介银保004')
delete from sainterfaceinfo where businessno=(select to_char(a.acontractid) from saaagentcontract a,saacontract b where a.acontractid=b.acontractid and b.agentname='ui测试-中介车商004-1');
delete from sainterfaceinfo where businessno in(select to_char(accountid) from sadaccount where accountno='1111116');
delete from saaagentcontract where acontractid=(select acontractid from saacontract where agentname='ui测试-中介车商004-1');
delete from saaagentcontracthis where acontractid=(select acontractid from saacontract where agentname='ui测试-中介车商004-1');
delete from sabpmmain where businessno=(select contractno from saacontract where agentname='ui测试-中介车商004-1');
delete from saacontract where agentname='ui测试-中介车商004-1';
delete from saacontractresult where agentname='ui测试-中介车商004-1';
delete from saacontracthis where agentname='ui测试-中介车商004-1';
delete from sadaccount where accountno='1111116';




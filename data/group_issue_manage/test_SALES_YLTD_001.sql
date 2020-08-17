delete from sabpmmain where businessno=(select to_char(groupid) from saugroup where groupname='ui测试-001');
delete from saugroupbackmsg where groupid=(select groupid from saugroup where groupname='ui测试-001');
delete from saugrouphistory where groupid=(select groupid from saugroup where groupname='ui测试-001');
delete from packetinfo where id=(select a.id from saugroupbackmsg a,saugroup b where a.groupid=b.groupid and b.groupname='ui测试-001');
delete from sainterfaceinfo where businessno=(select to_char(groupid) from saugroup where groupname='ui测试-001');
delete from saugroup where groupname='ui测试-001';
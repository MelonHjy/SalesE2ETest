--数据准备
delete from sabpmmain where businessno = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete from saucontract where usercode =(select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete from sadqualify where usercode=(select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete from sadaccount where IdentifyNumber = '220101198208075298';
delete from prpdsellerno  where sellercode = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete from sauusersub where userid = (select userid from sauuser where IdentifyNumber ='220101198208075298');
delete from sauuser where IdentifyNumber ='220101198208075298';


--辅助查询sql

-- SELECT * FROM sabpmmain where businessno = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM saucontract where usercode =(select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sadqualify where usercode=(select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sadaccount where IdentifyNumber = '220101198208075298';
-- SELECT * FROM prpdsellerno  where sellercode = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sauusersub where userid = (select userid from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sauuser where IdentifyNumber ='220101198208075298';
-- SELECT * FROM  SaUCodeMap where  usercode =(select usercode from sauuser where IdentifyNumber ='220101198208075298');
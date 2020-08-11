--数据准备
delete sabpmmain where businessno = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete saucontract where usercode =(select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete sadqualify where usercode=(select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete sadaccount where IdentifyNumber = '220101198208075298';
delete prpdsellerno  where sellercode = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
delete sauusersub where userid = (select userid from sauuser where IdentifyNumber ='220101198208075298');
delete sauuser where IdentifyNumber ='220101198208075298';


--辅助查询sql

-- SELECT * FROM sabpmmain where businessno = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM saucontract where usercode =(select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sadqualify where usercode=(select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sadaccount where IdentifyNumber = '220101198208075298';
-- SELECT * FROM prpdsellerno  where sellercode = (select usercode from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sauusersub where userid = (select userid from sauuser where IdentifyNumber ='220101198208075298');
-- SELECT * FROM sauuser where IdentifyNumber ='220101198208075298';
-- SELECT * FROM  SaUCodeMap where  usercode =(select usercode from sauuser where IdentifyNumber ='220101198208075298');
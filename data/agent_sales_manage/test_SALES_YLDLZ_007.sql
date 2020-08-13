
/*复原*/
/*工作流业务关联主表sabpmmain*/
delete from sabpmmain where businessno=(select usercode from sauuser where identifynumber='370126198007046159');
delete from	sadqualify where usercode=(select usercode from sauuser where identifynumber='370126198007046159');
delete from sadaccount where IdentifyNumber='370126198007046159';
delete from sauusersub where userid=(select userid from sauuser where identifynumber='370126198007046159');
delete from saucontract where userid=(select userid from sauuser where identifynumber='370126198007046159');
delete from prpdsellerno where identifynumber='370126198007046159';
delete from sauuser where UserID=(select UserID from sauuser where identifynumber='370126198007046159');


-- select * from SaUUser where identifynumber='370126198007046159'
-- select * from sabpmmain where businessno=(select usercode from sauuser where identifynumber='370126198007046159')
-- select * from sadqualify where usercode=(select usercode from sauuser where identifynumber='370126198007046159')
-- select * from sadaccount where identifynumber='370126198007046159';
-- select * from sauusersub where userid=(select userid from sauuser where identifynumber='370126198007046159')
-- select * from saucontract where userid=(select userid from sauuser where identifynumber='370126198007046159')
-- select * from prpdsellerno where identifynumber='370126198007046159'
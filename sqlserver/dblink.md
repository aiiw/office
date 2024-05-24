

EXEC sp_addlinkedserver

@server='HR', --被访问的服务器别名

@srvproduct='', --SqlServer默认不需要写，或ORACLE

@provider='SQLOLEDB', --不同的库都是不一样的，OLE DB字符

@datasrc='192.168.0.181'--要访问的服务器

EXEC sp_addlinkedsrvlogin
'HR', --被访问的服务器别名（如果上面sp_addlinkedserver中使用别名JOY，则这里也是JOY）
'false',
NULL,
'sa', --帐号
'$u2930123WJ' --密码





```sql


select * from hr.T9IMS.dbo.E_employee x where x.Hiredate>='2021-01-04 00:00:00.000'

select count(1) from employee  --19016

select * from EMPLOYEE t

select id from EMPLOYEE
--Code	Name	HireDate	DepartmentCode	DepartmentName	CardNo
create table synlog
(id varchar(100),
syndate varchar(100))


insert into synlog
select code,getdate() from hr.T9IMS.dbo.E_employee x where x.Hiredate>='2021-01-04 00:00:00.000'
and x.code not in (select id from EMPLOYEE) 




insert into EMPLOYEE(id,empname,hiredate,departmentcode,jobid,stopsalaryflag,e8)
select code,name,hiredate,'011301' d,right(cardno,6) k,'0','y' s from hr.T9IMS.dbo.E_employee x where x.Hiredate>='2021-01-04 00:00:00.000'
and x.code not in (select id from EMPLOYEE) 



insert into boss_ManInfo(id,jobdate,Home55)
select code,hiredate,'y' from hr.T9IMS.dbo.E_employee x where x.Hiredate>='2021-01-04 00:00:00.000'
and x.code not in (select id from boss_ManInfo)

```
代码段:

```sql
declare  rz number(3,1);

begin

SELECT count(1) into rz
  FROM (SELECT BMBAENT,
               BMBASITE,
               LEVEL LV,
               BMBA001,
               BMBA003,
               BMBA005,
               BMBA006,
               BMBA007,
               BMBA011,
               BMBA012,
               BMBA010,
               CONNECT_BY_ROOT BMBA001 ROOT,
               SUBSTR(SYS_CONNECT_BY_PATH(B.BMBA003, ' > '), 4) TYPEPATH
          FROM BMBA_T B
         WHERE BMBAENT = 100
        CONNECT BY PRIOR BMBA003 = BMBA001
               AND BMBAENT = 100
               AND BMBASITE = 'W'
               AND BMBA005 < SYSDATE
               AND (BMBA006 >= SYSDATE OR BMBA006 IS NULL)
         START WITH BMBAENT = 100
                AND BMBASITE ='W'
                AND BMBA005 < SYSDATE
                AND (BMBA006 >= SYSDATE OR BMBA006 IS NULL)
                AND BMBA001 ='190202000697') T0
 where t0.bmba003 like '14%';

 dbms_output.put_line(rz);
  end; --注意各个分号~~
  
```



-------------------------------------------------------------------------------------

一个函数的例子

```sql
CREATE OR REPLACE FUNCTION getnum_by19to14(op varchar2,site varchar2) RETURN varchar2 as
  rz number(5,2);
begin


SELECT count(1) into rz
  FROM (SELECT BMBAENT,
               BMBASITE,
               LEVEL LV,
               BMBA001,
               BMBA003,
               BMBA005,
               BMBA006,
               BMBA007,
               BMBA011,
               BMBA012,
               BMBA010,
               CONNECT_BY_ROOT BMBA001 ROOT,
               SUBSTR(SYS_CONNECT_BY_PATH(B.BMBA003, ' > '), 4) TYPEPATH
          FROM BMBA_T B
         WHERE BMBAENT = 100
        CONNECT BY PRIOR BMBA003 = BMBA001
               AND BMBAENT = 100
               AND BMBASITE = site
               AND BMBA005 < SYSDATE
               AND (BMBA006 >= SYSDATE OR BMBA006 IS NULL)
         START WITH BMBAENT = 100
                AND BMBASITE =site
                AND BMBA005 < SYSDATE
                AND (BMBA006 >= SYSDATE OR BMBA006 IS NULL)
                AND BMBA001 =op) T0
 where t0.bmba003 like '14%';

  return rz;

end;
```







Oracle存储过程简单实例
/*不带任何参数存储过程(输出系统日期)*/
create or replace procedure output_date is
begin
dbms_output.put_line(sysdate);
end output_date;

/*带参数in和out的存储过程*/
create or replace procedure get_username(v_id in number,v_username out varchar2)
as
begin
  select username into v_username from tab_user where id = v_id; --变量赋值 
exception
when no_data_found then 
raise_application_error(-20001,'ID不存在!');
end get_username;
---------------------------------------------------
begin
dbms_output.put_line(dbms_random.value());
end;

---------------------------------------------
1、在sql的执行窗口：
begin
OUT_TIME();
end;
/

"call OUT_TIME(); "

2、在命令窗口中两种方式都可以调用
exec OUT_TIME(); --这样，相当于执行一个plsql块，即把”OUT_TIME()“看成plsql块调用。
call OUT_TIME(); --这样，相当于，但用一个方法“OUT_TIME()”，把“OUT_TIME()”看成一个方法
--------------------------------------------------------------------------------------------------------------------------------------------------------

declare 
n1 number(3):=1;
begin
    loop
      exit when n1=100;
    n1:=n1+1;
    dbms_output.put_line(sysdate);
    end loop;
end;

---------------------------------------------------------------------------------

改良的例子

declare 
n1 number(3):=1;
n2  number(3);
begin
    delete from ty;
    loop
      exit when n1=100;
    n1:=n1+1;
    insert into ty select 'select * from ' || n1  from dual;
    end loop;
end;


select 'select * from ' || '21212'  from dual;


----------------------------------------------------------------------------------------胡建明当时需要的工作经历，一个人一条

CREATE OR REPLACE FUNCTION getxx(vname varchar2,vcode varchar2) RETURN varchar2
as
str1 varchar(2000);
str2 varchar(8000);
users tempp%rowtype;
cursor boys_cur is select * from tempp where a=vname and b=vcode;
begin
    open boys_cur;
loop
fetch boys_cur into users;
exit when boys_cur%notfound;
--dbms_output.put_line(users.user_name||'  '||users.password);
--dbms_output.put_line(boys_cur%rowcount);
str1:=trim(users.c);
str2:=str2||str1;
end loop;
close boys_cur;
    return(str2);
  end;
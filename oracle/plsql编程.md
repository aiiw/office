块的结构和声明变量
模块的组成
DECLARE
变量声明部分，可以没有
Begin
逻辑处理执行部分，到 end 结束，必须有
EXCEPTION
错误处理部分，可以没有
End;
块是我们 PL/SQL 的基石，我们的程序都是通过块组成，没有名称的块叫匿名块，完成一定的功能。
为什么要使用 pl/sql
便于维护（模块化）
提高数据安全性和完整性（通过程序操作数据）
提高性能（编译好的）
简化代码（反复调用）

该实验的目的是掌握在 pl/sql 块中操作变量.
DECLARE
v_hiredate DATE;
v_deptno NUMBER(2) NOT NULL := 10;
v_location VARCHAR2(13) := 'Atlanta';
c_comm CONSTANT NUMBER := 1400;
v_valid BOOLEAN NOT NULL := TRUE;
Not null 一定要给初值
CONSTANT 也一定要给值
:= 为赋值，=为逻辑判断，判断是否相等。

 %TYPE 属性
声明一个变量和某列数据类型相同
声明一个变量和另外一个变量数据类型一致
减小程序的无效的可能性，可以不知道列的数据类型，定义一个与之相同的变量。
v_name emp.ename%TYPE;
v_balance NUMBER(7,2);
v_min_balance v_balance%TYPE := 10;


 取表中的数据
declare
v1 emp.ename%type;
v2 emp.sal%type;
begin
select ename,sal into v1,v2
from emp where empno=7900;
dbms_output.put_line(v1);
dbms_output.put_line(v2);
end;
/
一定要有 into
一次只能操作一行，操作多行得用循环
变量类型和个数要匹配



For 循环，pl/sql 中的最常见的循环，是和游标操作的绝配。方便而直观。
begin
for v1 in 1..9 loop
Insert into t1 values(v1);
end loop;
end;

For 循环
DECLARE
CURSOR c1 is select ename,sal from emp order by sal desc;
n1 number(2);
BEGIN
for v1 in c1 loop
dbms_output.put_line(v1.ename||' '||v1.sal);
n1:=c1%rowcount;
end loop;
dbms_output.put_line(n1);
END;
/
V1 的数据类型为 c1%rowtype,c1 自动 open,自动 fetch,自动 close，for 循环和游标的结合可以很方
便的处理游标内的每一行。




 函数
函数是有名称的 pl/sql 块
函数有返回值
在表达式中调用函数
存储在服务器端
CREATE OR REPLACE FUNCTION get_sal
 (v_id IN emp.empno%TYPE)
 RETURN NUMBER
 IS
 v_salary emp.sal%TYPE :=0;
 BEGIN
 SELECT sal INTO v_salary FROM emp WHERE empno = v_id;
 RETURN (v_salary);
 END get_sal;
/


验证现在数据库使用的参数文件类型,我们一定要知道我们使用的是什么类型的参数文件,涉及到我们如
何修改参数的手段.
select distinct ISSPECIFIED from v$spparameter;
如果含有 true 就是使用二进制参数文件 要使用命令
如果只有 false 就是使用的纯文本参数文件

 alter system set pga_aggregate_target=30m scope=memory;
只修改内存的值,不改变参数文件的设置,下回再次启动数据库时值还是老的,能修改的前提是该参数可以
动态修改,如果是静态参数只能使用下面的方法.

我们现在回想一下数据库启动的三个台阶,我们先读的是参数文件,参数文件可以有我们来编写.读完参数
文件后又读了控制文件,控制文件描述了数据文件和日志文件的信息,如果控制文件丢失可以重新建立,最
后是读数据文件.数据文件里才存放了我们的数据.数
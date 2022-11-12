merge into 是英文的一个短语，意思是汇入，合并。顾名思义，merge into是合并了insert和update操作，其执行效率要高于分别单独执行insert和update语句。

//创建表

create table YLB_TEST_001
(
 ID  NUMBER,
 NAME VARCHAR2(20)
)；

create table YLB_TEST_002
(
 ID  NUMBER,
 NAME VARCHAR2(20)
)；

//插入数据

 

insert into ylb_test_001 values(1,'Arlene');

 

insert into ylb_test_001 values(2,'Bobby');

 

insert into ylb_test_001 values(3,'Tommy');

 

insert into ylb_test_001 values(4,'Jackey');

insert into ylb_test_002 values(1,'Arlene001');

//执行sql

merge into ylb_test_002 a
using ylb_test_001 b
on (a.id=b.id)
when matched then
 update set a.name = b.name
when not matched then
 insert values (b.id,b.name);

结果：

 ![img](https://images0.cnblogs.com/blog/638509/201412/191647220018408.jpg)![img](https://images0.cnblogs.com/blog/638509/201412/191647331415345.jpg)

小提示：merge into 目标表  using 源表 on （匹配条件） when matched then 执行update 操作 或 delete操作  when not matched then 执行 insert 操作。

​      oracle不支持delete操作；

​      在SQL2008中，新增了一个关键字：Merge，这个和Oracle的Merge的用法差不多，只是新增了一个delete方法而已。

​     源表 匹配条件字段unique
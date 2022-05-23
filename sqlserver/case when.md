### case when

普通case函数

```sql
CASE  <表达式>
   WHEN <值1> THEN <操作>
   WHEN <值2> THEN <操作>
   ELSE <操作>
END 
```

搜索case函数

```sql
CASE
    WHEN <条件1> THEN <命令>
    WHEN <条件2> THEN <命令>
    ELSE commands
END
```



场景1：有分数score，score<60返回不及格，score>=60返回及格，score>=80返回优秀

```sql
SELECT
STUDENT_NAME,
(CASE WHEN score < 60 THEN '不及格'
WHEN score >= 60 AND score < 80 THEN '及格'
WHEN score >= 80 THEN '优秀'
ELSE '异常' END) AS REMARK
FROM
TABLE1
```



场景2:在where后面使用case when的说明,有如下两个例子

```sql
select *
from A, B
where
CASE
when A.id = 0 then B.name in ('aaa', 'bbb')
when A.id = 1 then B.name in ('bbb', 'ccc')
when A.id = 2 then B.name in ('ccc', 'ddd')
END
```

```sql
select *
from A, B
where B.name =
CASE
when A.id = 0 then 'aaa'
when A.id = 1 then 'bbb'
when A.id = 2 then 'ccc'
END
```

### 作用一: 结合分组统计数据

需求: 将下图的数据按照"洲"进行统计总人数

[![img](https://pic4.zhimg.com/80/v2-fe03099ffa77fbb9e99438a5aaa8591b_720w.jpg)](https://pic4.zhimg.com/80/v2-fe03099ffa77fbb9e99438a5aaa8591b_720w.jpg)

(一)方式一: 使用普通的case函数进行统计



```
  select (
  case name 
   when '中国' then '亚洲'
   when '日本' then '亚洲'
   when '美国' then '北美洲'
   when '加拿大' then '北美洲'
  else '其他' end
  ) 洲,
  sum(population) 总数 
  from t_country
  GROUP BY
  (
  case name 
   when '中国' then '亚洲'
   when '日本' then '亚洲'
   when '美国' then '北美洲'
   when '加拿大' then '北美洲'
  else '其他' end
  )
```

方式一统计结果

[![img](https://pic1.zhimg.com/80/v2-baf9927ad5c45e0fe9c46776fe753a38_720w.jpg)](https://pic1.zhimg.com/80/v2-baf9927ad5c45e0fe9c46776fe753a38_720w.jpg)

### 作用二: 分条件更新字段值

(一)需求: 将工资低于3000的员工涨幅工资20%,工资等于高于3000的员工涨幅8%,数据如下:

[![img](https://pic2.zhimg.com/80/v2-6680dacea0e566739b7e98f51daa3bad_720w.jpg)](https://pic2.zhimg.com/80/v2-6680dacea0e566739b7e98f51daa3bad_720w.jpg)

可能有人看到这个需求的第一反应,想直接可以直接通过如下两条update语句直接更新:



```
update t_salary set salary = salary + (salary * 0.2) where salary < 3000;
update t_salary set salary = salary + (salary * 0.08) where salary >= 3000;
```

但是,如果是这样执行的话实际上会存在问题,比如:原来工资在2900的员工,执行完第一条语句后工资会变成3480,此时,再执行第二条更新语句,因为满足工资大于三千,则又会去添加多8%的工资,这样明显就是不符合我们的需求的,所以,如果想完成这个需求,又不想写太复杂的sql,可以通过case函数完成这个功能。

(二)使用搜索的case函数进行分条件修改(此处不能使用简单case函数,因为简单case函数不能判断带范围的条件)



```
update t_salary
 set 
 salary = 
 (
  case 
   when salary < 3000 then salary + salary * 0.2
   when salary >= 3000 then salary + salary * 0.08
   else salary 
  end
 )
```

### 作用三: 检查表中字段值是否一致

(一)需求: 判断两个表中name字段值是否一致,并返回结果,数据如下:

[![img](https://pic3.zhimg.com/80/v2-923b53ab8b92ed9757c5b6814cfdd20a_720w.jpg)](https://pic3.zhimg.com/80/v2-923b53ab8b92ed9757c5b6814cfdd20a_720w.jpg)

 

(二)使用搜索的case函数进行分条件修改(此处不能使用简单case函数,因为简单case函数不能判断带范围的条件)



```
select name,
(
 case 
 when desciption in(select description from t_user2) then '一致'
 else '不一致'
 end
) 比较结果
from t_user1
```

(三)比较结果:

[![img](https://pic2.zhimg.com/80/v2-3dd9b8655e91165c38f4a292d0cf673d_720w.jpg)](https://pic2.zhimg.com/80/v2-3dd9b8655e91165c38f4a292d0cf673d_720w.jpg)

### 作用四: 行转列(重点-面试常见)

(一)需求: 将表中数据按照每个学生姓名 、科目、成绩进行排序,数据如下:

[![img](https://pic3.zhimg.com/80/v2-4d55326f4d0192c371f791437e4fe81e_720w.jpg)](https://pic3.zhimg.com/80/v2-4d55326f4d0192c371f791437e4fe81e_720w.jpg)

(二)使用case函数转换



```
// 使用普通case函数
SELECT NAME,
 max( CASE class WHEN '语文' THEN grade ELSE 0 END ) 语文,
 max( CASE class WHEN '数学' THEN grade ELSE 0 END ) 数学,
 max( CASE class WHEN '英语' THEN grade ELSE 0 END ) 英语 
FROM
 t_source 
GROUP BY
NAME

// 使用搜索case函数
SELECT NAME,
 max( CASE  WHEN class = '语文' THEN grade ELSE 0 END ) 语文,
 max( CASE  WHEN class =  '数学' THEN grade ELSE 0 END ) 数学,
 max( CASE  WHEN class = '英语' THEN grade ELSE 0 END ) 英语 
FROM
 t_source 
GROUP BY
NAME
```

(三)转换结果

[![img](https://pic2.zhimg.com/80/v2-0940c202a73c6664c60ffac08a9e2391_720w.jpg)](https://pic2.zhimg.com/80/v2-0940c202a73c6664c60ffac08a9e2391_720w.jpg)

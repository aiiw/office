```
 coalesce((select xccc280a
                  from xccc_t t
                 where t.xccc004 = extract(year from sysdate)
                   and t.xccc005 = extract(month from sysdate)
                   and t.xccc006 = sfdd001
                   and t.xccccomp = sfddsite),
                (select xccc280a
                   from xccc_t t
                  where t.xccc004 = extract(year from sysdate-30)
                    and t.xccc005 = extract(month from sysdate-30)
                    and t.xccc006 = sfdd001
                    and t.xccccomp = sfddsite)/*,
                (select xccc280a
                   from xccc_t t
                  where t.xccc004 = extract(year from sysdate-60)
                    and t.xccc005 = extract(month from sysdate-60)
                    and t.xccc006 = sfdd001
                    and t.xccccomp = sfddsite)*/) 单价,coalesce
```

```
COALESCE 是一个在 SQL 中常用的函数，用于返回参数列表中的第一个非空值。它的语法如下：

COALESCE(value1, value2, ...)
其中，value1, value2, ... 是要比较的值。

使用 COALESCE 函数时，它会逐个检查参数列表中的值，如果发现一个非空值，则返回该值；如果所有参数都是 NULL，则返回 NULL。

这在处理数据库查询结果时非常有用，因为有时候我们希望在某些字段为空时使用备用值。

例如，假设我们有一个员工表，其中包含员工的姓名和昵称。有些员工可能没有昵称，但我们希望在显示他们的昵称时，如果昵称为空，则显示他们的姓名。可以使用 COALESCE 函数来实现：

sql
SELECT COALESCE(nickname, name) AS display_name
FROM employees;
这将返回一个名为 display_name 的结果集，其中包含员工的昵称，如果昵称为空，则显示他们的姓名。

在不同的数据库管理系统中，COALESCE 函数可能有一些细微的差异，但通常的功能和用法都是相似的。
```


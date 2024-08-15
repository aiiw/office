```sql
let kksql="SELECT t3.xmdg058 AS code, MAX(t3.xmdgua017) AS description",
   " FROM xmdg_t t3 ",
  " WHERE t3.xmdg058 IN ( ",
          " SELECT t2.xmdgucdocno ",
           " FROM xmdfuc_t t1 ",
           " LEFT JOIN xmdguc_t t2 ",
            "   ON t1.xmdfuc003 = t2.xmdgucdocno ",
           " WHERE t1.xmdfucdocno = ? )",        
   " GROUP BY t3.xmdg058 ",
   " ORDER BY t3.xmdg058 "

PREPARE kkcur1 FROM kksql
DECLARE kkcur2 CURSOR FOR kkcur1
LET abc = ""

FOREACH kkcur2 USING g_xmdeuc_m.xmdeucdocno INTO code,description
IF cl_null(abc) then
  LET g_xmdeuc_m.l_xmdgua017 =code , ": " , description , "\n"
  LET abc = "true"
  ELSE
  LET g_xmdeuc_m.l_xmdgua017 = g_xmdeuc_m.l_xmdgua017 , code , ": " , description , "\n"
  END IF
  END FOREACH
```

另从资料加抄录

Locking CURSOR 用来更新

```
LET l_sql = 〞SELECT * FROM employee_file 〞, 
            〞 WHERE no = ? FOR UPDATE 〞

PREPARE emp_pre FROM l_sql
DECLARE emp_cl CURSOR FOR emp_pre
OPEN emp_cus USING l_no
FETCH emp_cus INTO l_emp.*  #只抓一筆資料lock
```

Non-Scrolling CURSOR 用来填充报表

```
LET l_sql = 〞SELECT * FROM employee_file 〞, 
            〞 WHERE 〞, l_str

PREPARE emp_pre FROM l_sql
DECLARE emp_cus CURSOR FOR emp_pre
FOREACH emp_cus INTO l_emp.* #循序抓資料
        IF l_emp.salary > 80000 THEN
           EXIT FOREACH
        END IF
END FOREACH         
```

Scrolling CURSOR

```
LET l_sql = 〞SELECT * FROM employee_file 〞, 
            〞 WHERE 〞, l_str

PREPARE emp_pre FROM l_sql
DECLARE emp_cus SCROLL CURSOR 
      [WITH HOLD] FOR emp_pre
OPEN emp_cus
FETCH FIRST emp_cus INTO l_emp.*  #抓第一筆

```


```sql
SELECT 
    CONVERT(VARCHAR(4), z.BeginDate, 120) AS 年份,
    MONTH(z.BeginDate) AS 月份,
    e.Code AS 员工工号,
    ycqts AS 应出勤天,
    CASE 
        WHEN e.Code IN ('11608', '11458', '11522') THEN cqts * (1 + 1/8) -- 对应特殊员工的实出勤天数进行特殊计算
        ELSE cqts 
    END AS 实出勤天,
    sjts AS 事假天,
    kgts AS 旷工天,
    _cdcs AS 迟到次数,
    ChiDao AS 迟到分数,
    _ztcs AS 早退次数,
    ZaoTui AS 早退分数,
    ISNULL(OT1, 0) + ISNULL(OT2, 0) + ISNULL(OT3, 0) AS 加班时数 
FROM 
    T_HR_WorkingTimeTotal k
LEFT JOIN 
    T_HR_Employee e ON k.EmpID = e.ID
LEFT JOIN 
    T_HR_Period z ON z.ID = k.MonthID
WHERE 
    CONVERT(VARCHAR(7), z.BeginDate, 120) = CONVERT(VARCHAR(7), DATEADD(MONTH, -1, GETDATE()), 120)
    AND e.PayTypeID = 1 --add 20240223 增加只过滤计时员工的考勤数据
```


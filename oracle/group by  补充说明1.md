一个错误的例子

```sql
select distinct temp1.sfcbdocno,
                                    
                                    case
                                      when temp1.ecaa002 = '装配站' then
                                       sum(nvl(temp1.num1, 0))
                                    end "装配站",
                                    case
                                      when temp1.ecaa002 = '砂光站' then
                                       sum(nvl(temp1.num1, 0))
                                    end "砂光站",
                                    case
                                      when temp1.ecaa002 = '抛光站' then
                                        sum(nvl(temp1.num1, 0))
                                    end "抛光站",
                                    case
                                      when temp1.ecaa002 = '复底站' then
                                        sum(nvl(temp1.num1, 0))
                                    end "复底站",
                                    case
                                      when temp1.ecaa002 = '拉伸站' then
                                        sum(nvl(temp1.num1, 0))
                                    end "拉伸站",
                                    case
                                      when temp1.ecaa002 = '开料站' then
                                       sum(nvl(temp1.num1, 0))
                                    end "开料站"
                    
                      from (select distinct b.sfcbdocno sfcbdocno,
                                            b.sfcb002 seq,
                                            b.sfcb003 sfcb003,
                                            b.sfcb033 num1,
                                            o.oocql004 oocql004,
                                            b.sfcb011 sfcb011,
                                            g.ecaa002 ecaa002,
                                            row_number() over(partition by b.sfcbdocno, g.ecaa002 order by b.sfcb002 desc) rn
                              from sfca_t a
                              left join sfcb_t b
                                on a.sfcadocno = b.sfcbdocno
                              left join sfaa_t t0
                                on t0.sfaadocno = a.sfcadocno
                            
                              left join oocql_t o
                                on b.sfcb003 = o.oocql002
                               and o.oocql001 = '221'
                               and o.oocql003 = 'zh_CN'
                               and o.oocqlent = '100'
                            
                              left join ecaa_t g
                                on g.ecaa001 = b.sfcb011
                               and g.ecaaent = b.sfcbent
                               and g.ecaasite = b.sfcbsite
                            
                             where 1 = 1
                                  
                                  --and a.sfcadocno = 'WKS40-20080502312'
                                  --and substr(a.sfcadocno,2,4)='LS05'
                               and a.sfca005 = '1' --and b.sfcb016 = 'Y' 暂时不加  去掉报工
                               and b.sfcb033 <> 0) temp1
                     where temp1.rn = 1 and temp1.sfcbdocno='WMS05-24061200265'
                     group by temp1.sfcbdocno
```

一个正确的例子,是这个字段开始就要使用聚合函数,如下:

```sql
select distinct temp1.sfcbdocno,
                
                SUM(CASE
                      WHEN temp1.ecaa002 = '装配站' THEN
                       NVL(temp1.num1, 0)
                      ELSE
                       0
                    END) AS "装配站",
                SUM(CASE
                      WHEN temp1.ecaa002 = '砂光站' THEN
                       NVL(temp1.num1, 0)
                      ELSE
                       0
                    END) AS "砂光站",
                SUM(CASE
                      WHEN temp1.ecaa002 = '抛光站' THEN
                       NVL(temp1.num1, 0)
                      ELSE
                       0
                    END) AS "抛光站",
                SUM(CASE
                      WHEN temp1.ecaa002 = '复底站' THEN
                       NVL(temp1.num1, 0)
                      ELSE
                       0
                    END) AS "复底站",
                SUM(CASE
                      WHEN temp1.ecaa002 = '拉伸站' THEN
                       NVL(temp1.num1, 0)
                      ELSE
                       0
                    END) AS "拉伸站",
                SUM(CASE
                      WHEN temp1.ecaa002 = '开料站' THEN
                       NVL(temp1.num1, 0)
                      ELSE
                       0
                    END) AS "开料站"

  from (select distinct b.sfcbdocno sfcbdocno,
                        b.sfcb002 seq,
                        b.sfcb003 sfcb003,
                        b.sfcb033 num1,
                        o.oocql004 oocql004,
                        b.sfcb011 sfcb011,
                        g.ecaa002 ecaa002,
                        row_number() over(partition by b.sfcbdocno, g.ecaa002 order by b.sfcb002 desc) rn
          from sfca_t a
          left join sfcb_t b
            on a.sfcadocno = b.sfcbdocno
          left join sfaa_t t0
            on t0.sfaadocno = a.sfcadocno
        
          left join oocql_t o
            on b.sfcb003 = o.oocql002
           and o.oocql001 = '221'
           and o.oocql003 = 'zh_CN'
           and o.oocqlent = '100'
        
          left join ecaa_t g
            on g.ecaa001 = b.sfcb011
           and g.ecaaent = b.sfcbent
           and g.ecaasite = b.sfcbsite
        
         where 1 = 1
              
              --and a.sfcadocno = 'WKS40-20080502312'
              --and substr(a.sfcadocno,2,4)='LS05'
           and a.sfca005 = '1' --and b.sfcb016 = 'Y' 暂时不加  去掉报工
           and b.sfcb033 <> 0) temp1
 where temp1.rn = 1
   and temp1.sfcbdocno = 'WMS05-24061200265'
 group by temp1.sfcbdocno

```


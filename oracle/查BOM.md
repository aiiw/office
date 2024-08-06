```
--1父3子
 select *
   from (
   select t.*,sys_connect_by_path(t.bmba003, '/') a from (select '190100002495' bmba003,'' bmba021,'' bmba001 from dual
   union
   select  t.*
           from vvtt t) t
           
          start with t.bmba001 is null
         CONNECT BY PRIOR t.bmba003 = t.bmba001) p
  where p.a like '/190100002495%'



select b.sfba005, decode(f.imaf013, 2, '自制', 1, '采购')
  from sfba_t b
  left join imaf_t f
    on b.sfba005 = f.imaf001
   and b.sfbaent = f.imafent
   and b.sfbasite = f.imafsite
 where b.sfbadocno = 'WKS40-20080502312'


select * from sfaa_t t where t.sfaa021='WKS40-20080502312' and t.sfaastus<>'X'

```

```
但是仍然核对不上,放弃
```


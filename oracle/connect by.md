```sql
select t.sfaa025 父单号,
       t.sfaadocno 单号,
       t.sfaa010 料号,
       (select i.imaal003 from imaal_t i where i.imaal001 = t.sfaa010) 名称,
       t.sfaa012 生产数量,
       level,
       sys_connect_by_path(t.sfaadocno, '\') as path,
       connect_by_root(t.sfaadocno)
  from sfaa_t t
 start with t.sfaadocno = 'DMS01-20061300098'
connect by t.sfaa025 = prior t.sfaadocno
--where t.sfaaua033='1200644'
;
select * from sfaa_t x where x.sfaadocno='DMS01-20061300098'

select p.*,level,sys_connect_by_path((select i.imaal003 from imaal_t i where i.imaal001 = p.z and  i.imaalent='72' and i.imaal002='zh_CN'),'--->') 名称 from (
select t.bmba001 f, t.bmba003 z
  from bmba_t t
union  
select '' f,'190100001907' t from dual) p
start with p.z='190100001907'
connect by prior p.z=p.f



select * from imaal_t i where

select b.bmba001 父节点,b.bmba003 子节点 from bmba_t b
start with b.bmba001='190100001907' and b.bmbasite='D' 
connect by prior b.bmba001=b.bmba003
```


```sql
update product_info t 
set (t.salename,t.xsqy)
=(select c.salename,c.xsqy from contract_erp c  where c.contractcode=t.contractid)
where t.contractid in(select c.contractcode from contract_erp c) and t.contractid is not null and t.salename is null;
```

### 一次导数据更新的过程

```sql
--一  创建临时表
create  table aimm21501_l
(liaohao varchar(100),cn varchar(100),sj varchar(100),sb varchar(100))

/*drop table aimm21501_l*/

--二 导入数据,这样导入会有很多空格,所有有第三步去空格
select t.*,t.rowid from aimm21501_l t

--三 去空格
create table aimm21502_l as
select distinct trim(a.liaohao) liaohao,trim(a.cn) cn,trim(a.sj) sj,trim(a.sb) sb from aimm21501_l a


--drop table aimm21502_l

select  t.liaohao from aimm21502_l t

/*select * from imae_t l where l.imaeent='100' and l.imaesite='W'
and l.imae001 not in 
(select trim(t.liaohao) from aimm21502 t  )*/

/*select distinct trim(t.liaohao) from aimm21502_l t
where t.liaohao not in (select ll.imae001 from imae_t ll where ll.imaesite='W' )
*/
--4 统计重复的数据
select *
  from aimm21502 mm
 where mm.liaohao in
       (select trim(m.liaohao) from aimm21502 m group by trim(m.liaohao) having count(1)>1)


;
--5更新数据
update imae_t ll
   set ll.imaeua001 =
       (select max(t.sj) from aimm21502_l t where ll.imae001 = t.liaohao),
       ll.imaeua002 =
       (select max(t.cn) from aimm21502_l t where ll.imae001 = t.liaohao),
       ll.imaeua003 =
       (select max(t.sb) from aimm21502_l t where ll.imae001 = t.liaohao)
 where ll.imaeent = '100'
   and ll.imaesite = 'W'
   and ll.imae001 in (select t.liaohao from aimm21502_l t)
--可以写简单点 set(a,b,c)=(select a,b,c from dual)
--6按工单更新设备信息
update sfaa_t sf
   set sf.sfaaua017 =
       (select max(ll.imaeua003)
          from imae_t ll
         where ll.imae001 = sf.sfaa010
           and ll.imaesite = 'W')
 where sf.sfaaua017 is null
   and sf.sfaadocno in ('WLS05-22042900014',
                        'WLS05-22042900034',
                        'WLS05-22051600106',
                        'WLS05-22052500013',
                        'WLS05-22052500014',
                        'WLS05-22052500015',
                        'WLS05-22052500023',
                        'WLS05-22052500052',
                        'WLS05-22052500053',
                        'WLS05-22052500054',
                        'WLS05-22052500058',
                        'WLS05-22052600002',
                        'WLS05-22052600003',
                        'WLS05-22052600004',
                        'WLS05-22052600023',
                        'WLS05-22052600030')




```


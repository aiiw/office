第一段  
 select t.xmdadocno,f.sfaadocno,t.xmda033,f.sfaaua033
     from xmda_t t
    inner join sfaa_t f
       on t.xmdaent = t.xmdaent
      and t.xmdasite = f.sfaasite
      and t.xmdadocno = f.sfaaua001
    where nvl(t.xmda033,1) <> nvl(f.sfaaua033,1) and f.sfaadocno='WLS02-21092900001'


oracle:  根据A表更新B表
    update sfaa_t f
       set f.sfaaua033 =
           (select t.xmda033
              from xmda_t t where t.xmdaent = t.xmdaent and t.xmdasite = f.sfaasite and t.xmdadocno = f.sfaaua001)
     where f.sfaadocno = 'WLS02-21092900001' --如果要两表过滤后的范围再更新则这里还有 in(第一段)


sqlserver:

--sqlserver做的比较好,from 后面的类似select段的from,然后在前面update 虚拟别名表.
update t1
set t1.HIREDATE=t2.HIREDATE  --CONVERT(datetime,'2020-04-01',23)
 ,t1.star=t2.STAR
, t1.htDate=t2.htDate
from employee t1,employee20200514 t2
where t1.ID=t2.ID
and 
t1.ID in ('45307',
'20018',
'20130',
'20120',
'21746',
'21871',
'22856',
'22858',
'23749',
'20200',
'20332',
'23093',
'23326',
'23711',
'22930',
'10044',
'22479',
'20997',
'21130',
'20008',
'30035',
'20568',
'21583',
'23723',
'20033')
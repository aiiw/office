with g as
(select '1' a ,'信息中心' b,'小红' c from dual
union all
select '1' a ,'信息中心' b,'小红' c from dual
union all
select '1' a ,'信息中心' b,'小明' c from dual
union all
select '2' a ,'信息中心' b,'小明' c from dual)
select g.b,g.c,count(distinct g.a) from g
group by g.b,g.c
having count(distinct g.a)>1

with g as
(select '1' a ,'信息中心' b,'小红' c from dual
union all
select '1' a ,'信息中心' b,'小红' c from dual
union all
select '1' a ,'信息中心' b,'小明' c from dual
union all
select '2' a ,'信息中心' b,'小明' c from dual)
select * from g





![image-20240806085112806](https://gitee.com/aiiw/images/raw/master/img/image-20240806085112806.png)
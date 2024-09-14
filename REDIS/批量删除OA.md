





1 连接 redis-cli -h localhost -p 6399 -a myoa888

![image-20240904170321171](https://gitee.com/aiiw/images/raw/master/img/image-20240904170321171.png)



![](https://gitee.com/aiiw/images/raw/master/img/image-20240904165419983.png)



2 实践

![image-20240904171957596](https://gitee.com/aiiw/images/raw/master/img/image-20240904171957596.png)

附脚本:

```
select -- count(1) CONCAT('Hello', ' ', 'World');
-- "message:msg:user:" || msg_id
CONCAT('del message:msg:user:',MSG_ID)
from message m 
left join td_user u1 on u1.UID=m.from_uid
left join td_user u2 on u2.UID=m.to_uid
left join department d1 on d1.DEPT_ID=u1.DEPT_ID
left join department d2 on d2.DEPT_ID=u2.DEPT_ID
where 1=1 
  and (m.FROM_UID='960' or m.TO_UID='960')
order by m.SEND_TIME

```


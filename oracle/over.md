# SQL数据库语言：rank() over,dense_rank() over,row_number() over的区别

1. 总结一下吧：
   rank() over进行排名的时候，得到的排名分数相同的时候会展示相同的排名，下面的排名会被位置人数占用

2. ![image-20220523115320319](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523115320319.png)

   dense_rank() over 进行排名的时候，得到的排名分数相同的时候会展示相同的排名，下面的排名会被位置人数不会占用

   ![image-20220523115408059](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523115408059.png)

   row_number() over: 这个函数不需要考虑是否并列，哪怕根据条件查询出来的数值相同也会进行连续排名。

   ![image-20220523115520704](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523115520704.png)

   通常成绩排名等使用rank()over配合null最后的last指定。 first_value() over()

![image-20220523115612738](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523115612738.png)



```sql
select distinct substr(m.imaa001, 1, 6),
       last_value(m.imaa001) over(partition by substr(m.imaa001, 1, 6) order by substr(m.imaa001, 1, 6) desc)
  from imaa_t m
  left join imaal_t l
    on m.imaa001 = l.imaal001
 where m.imaa001 like '1%'
    or m.imaa001 like '8%'
   and m.imaastus = 'Y'
```

![image-20220611085042904](https://gitee.com/aiiw/images/raw/master/img/image-20220611085042904.png)

![image-20220611085100321](https://gitee.com/aiiw/images/raw/master/img/image-20220611085100321.png)

![image-20220611085112800](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20220611085112800.png)

![image-20220611085131598](https://gitee.com/aiiw/images/raw/master/img/image-20220611085131598.png)

![image-20220611085149174](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20220611085149174.png)

**1.round函数(四舍五入）**

描述 : 传回一个数值，该数值是按照指定的小数位元数进行四舍五入运算的结果

参数:

number : 欲处理之数值

decimal_places : 四舍五入 , 小数取几位 ( 预设为 0 )

```
select round(123.456, 0) from dual； 返回123
select round(123.456, 1) from dual; 返回123.5
select round(-123.456, 2) from dual; 返回-123.46
```

**2.ceil和floor函数**

ceil和floor函数在一些业务数据的时候，有时还是很有用的。

ceil(n) 取大于等于数值n的最小整数；

floor(n)取小于等于数值n的最大整数

```
select ceil(1.5) a from dual; 返回2
select ceil(-1.5) a from dual; 返回-1
select floor(1.5) a from dual; 返回1
select floor(-1.5) a from dual; 返回-2
```

**3.trunc函数**

　　1）trunc函数处理数字

　　　　　　TRUNC（number[,decimals]）

　　　　　　其中：

　　　　　　number 待做截取处理的数值

　　　　　　decimals 指明需保留小数点后面的位数。可选项，忽略它则截去所有的小数部分。

　　　　　　trunc就是处理数字的显示位数，如果decimals为负数，就处理整数部分，处理完为0，-1就是各位为零，-2就到了十位，如果超过了 整数部分长度，则整个数字0；

　　2）处理日期　　　　

　　　　trunc函数返回以指定元元素格式截去一部分的日期值。

　　　　其具体的语法格式如下：

　　　　TRUNC（date,[fmt]）

　　　　其中：

　　　　date为必要参数，是输入的一个日期值

　　　　fmt参数可忽略，是日期格式，用以指定的元素格式来截去输入的日期值。忽略它则由最近的日期截去
　　　　下面是该函数的使用情况：

```
trunc(sysdate,'yyyy') --返回当年第一天.
trunc(sysdate,'mm') --返回当月第一天.
trunc(sysdate,'d') --返回当前星期的第一天.
selecttrunc(sysdate,'YYYY')from dual;
selecttrunc(sysdate,'MM')from dual;
selecttrunc(sysdate,'D')from dual;
```
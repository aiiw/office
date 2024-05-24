CONVERT(datetime,'2020-04-01',23)

```sql
select CONVERT(varchar(111),getdate(),23),'23'
union
select CONVERT(varchar(111),getdate(),111),'111'
union
select CONVERT(varchar(111),getdate(),112),'112'
结果：
2022/05/23	111
20220523	112
2022-05-23	23
```



| Style ID    | Style 格式                            |
| :---------- | ------------------------------------- |
| 100 或者 0  | mon dd yyyy hh:miAM （或者 PM）       |
| 101         | mm/dd/yy                              |
| 102         | yy.mm.dd                              |
| 103         | dd/mm/yy                              |
| 104         | dd.mm.yy                              |
| 105         | dd-mm-yy                              |
| 106         | dd mon yy                             |
| 107         | Mon dd, yy                            |
| 108         | hh:mm:ss                              |
| 109 或者 9  | mon dd yyyy hh:mi:ss:mmmAM（或者 PM） |
| 110         | mm-dd-yy                              |
| 111         | yy/mm/dd                              |
| **112**     | **yymmdd**                            |
| 113 或者 13 | dd mon yyyy hh:mm:ss:mmm(24h)         |
| 114         | hh:mi:ss:mmm(24h)                     |
| 120 或者 20 | yyyy-mm-dd hh:mi:ss(24h)              |
| 121 或者 21 | yyyy-mm-dd hh:mi:ss.mmm(24h)          |
| 126         | yyyy-mm-ddThh:mm:ss.mmm（没有空格）   |
| 130         | dd mon yyyy hh:mi:ss:mmmAM            |
| 131         | dd/mm/yy hh:mi:ss:mmmAM               |
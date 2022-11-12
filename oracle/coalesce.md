```
 coalesce((select xccc280a
                  from xccc_t t
                 where t.xccc004 = extract(year from sysdate)
                   and t.xccc005 = extract(month from sysdate)
                   and t.xccc006 = sfdd001
                   and t.xccccomp = sfddsite),
                (select xccc280a
                   from xccc_t t
                  where t.xccc004 = extract(year from sysdate-30)
                    and t.xccc005 = extract(month from sysdate-30)
                    and t.xccc006 = sfdd001
                    and t.xccccomp = sfddsite)/*,
                (select xccc280a
                   from xccc_t t
                  where t.xccc004 = extract(year from sysdate-60)
                    and t.xccc005 = extract(month from sysdate-60)
                    and t.xccc006 = sfdd001
                    and t.xccccomp = sfddsite)*/) 单价,coalesce
```


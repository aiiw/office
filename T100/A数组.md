静态数组:

### DEFINE g_desc ARRAY[3] OF CHAR(14)

```
DEFINE g_x      ARRAY[10] OF RECORD
                              a CHAR(10),
                              b CHAR(10),
                              c CHAR(10)
            END RECORD

```

动态数组:

### DEFINE g_i DYNAMIC ARRAY OF INTEGER

```
DEFINE g_x DYNAMIC  ARRAY  OF RECORD
                                       a CHAR(10),
                                       b CHAR(10),
                                       c CHAR(10)
               END RECORD
```

| **物件名稱**                   | **說  明**                                                   |
| ------------------------------ | ------------------------------------------------------------ |
| getLength( ) RETURNING INTEGER | 回傳一維陣列的長度                                           |
| clear()                        | 將動態陣列（Dynamic Array）中，所有記錄移除。將固定陣列（Static Array）中，所有紀錄值清為NULL。 |
| appendElement()                | 在動態陣列（Dynamic Array）後面加上一筆新的記錄。這個物件在固定陣列（Static Array）中無效。 |
| insertElement( INTEGER )       | 在指定位置新增記錄，並將指定位置後之資料往下移。動態陣列（Dynamic Array）的筆數加1。 |
| deleteElement( INTEGER )       | 移除指定位置記錄，並將指定位置後之資料往上移。動態陣列（Dynamic Array）的筆數減1。 |
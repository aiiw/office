# Filter的并与或

在 Excel 中，FILTER 函数的第二个参数可以帮助你指定多个条件，可以使用逻辑运算符来实现与（AND）和或（OR）的逻辑操作。

### 使用与逻辑（AND）

如果要使用与逻辑来筛选数据，即多个条件同时满足时，可以在第二个参数中分别指定多个条件，并使用逗号分隔。例如：

Code=FILTER(range, (condition1)*(condition2)*(condition3), [if_empty])

在这个例子中：

- `range` 是你要筛选的数据范围。
- `(condition1)*(condition2)*(condition3)` 是一个逻辑表达式，用来描述多个条件的与逻辑。条件之间使用乘号 `*` 连接，表示逻辑与关系。

例如，如果要筛选 A 列中数值大于 10 且小于 20 的数据，可以这样写：

Code=FILTER(A:A, (A:A > 10) * (A:A < 20))

### 使用或逻辑（OR）

如果要使用或逻辑来筛选数据，即多个条件中任一条件满足时，可以在第二个参数中使用逻辑运算符 `+` 来连接条件。例如：

Code=FILTER(range, (condition1)+(condition2), [if_empty])

在这个例子中：

- `range` 是你要筛选的数据范围。
- `(condition1)+(condition2)` 是一个逻辑表达式，用来描述多个条件的或逻辑。条件之间使用加号 `+` 连接，表示逻辑或关系。

例如，如果要筛选 A 列中数值大于 10 或小于 5 的数据，可以这样写：

Code=FILTER(A:A, (A:A > 10) + (A:A < 5))

过滤 Excel 中的数据。
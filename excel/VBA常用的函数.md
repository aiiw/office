- 以下是一些常用的 VBA 函数及其作用：
  - 字符串处理函数：
    - `Replace`：替换字符串中指定的字符或子串。
    - `Left`：返回字符串左侧指定长度的字符。
    - `Right`：返回字符串右侧指定长度的字符。
    - `Mid`：返回字符串中从指定位置开始指定长度的字符。
    - `Len`：返回字符串的长度。
    - `Trim`：去除字符串两侧的空格。
    - `LCase`：将字符串转换为小写。
    - `UCase`：将字符串转换为大写。
    - `InStr`：查找字符串中指定字符或子串的位置。
  - 数学函数：
    - `Abs`：返回一个数的绝对值。
    - `Round`：将一个数四舍五入到指定的小数位数。
    - `Int`：返回一个数的整数部分。
    - `Sqrt`：返回一个数的平方根。
    - `Exp`：返回以 e 为底的指数幂。
    - `Log`：返回一个数的自然对数。
    - `Sin`、`Cos`、`Tan`：返回一个角度的正弦、余弦、正切值。
  - 日期和时间函数：
    - `Date`：返回当前日期。
    - `Time`：返回当前时间。
    - `Now`：返回当前日期和时间。
    - `Year`、`Month`、`Day`：从日期中提取年份、月份、日期。
    - `Hour`、`Minute`、`Second`：从时间中提取小时、分钟、秒数。
    - `DateDiff`：计算两个日期之间的差距。
  - Excel 相关函数：
    - `Range`：用于操作 Excel 工作表中的单元格范围。
    - `Cells`：用于操作 Excel 工作表中的单个单元格。
    - `WorksheetFunction`：用于调用 Excel 工作表中的内置函数，如求和、平均值等。
  - 对话框函数：
    - `MsgBox`：在屏幕上显示一段消息，并提示用户进行选择。
    - `InputBox`：弹出一个输入框，允许用户输入文本或数字。

下面是一个使用 `Replace` 函数的示例代码：

```
Copy CodeSub example()
    Dim originalString As String
    Dim newString As String

    originalString = "Hello World!"
    newString = Replace(originalString, "World", "VBA")

    MsgBox newString
End Sub
```

在上面的示例中，我们使用 `Replace` 函数将原始字符串中的 "World" 替换为 "VBA"。最终的结果会显示在消息框中。
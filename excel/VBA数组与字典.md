- 数组类函数 `Array`：

  ```
  Copy CodeSub ArrayExample()
      Dim myArray As Variant
  
      ' 创建一个包含多个元素的数组
      myArray = Array(1, 2, 3, 4, 5)
  
      ' 访问数组元素
      MsgBox myArray(0) ' 输出 1
  
      ' 修改数组元素
      myArray(2) = 10
  
      ' 遍历数组
      For i = LBound(myArray) To UBound(myArray)
          MsgBox myArray(i)
      Next i
  End Sub
  ```

- 字典类函数 `Dictionary`：

  ```
  Copy CodeSub DictionaryExample()
      Dim myDict As Object
      Set myDict = CreateObject("Scripting.Dictionary")
  
      ' 添加键值对
      myDict.Add "Name", "John"
      myDict.Add "Age", 30
      myDict.Add "City", "New York"
  
      ' 访问字典中的值
      MsgBox myDict("Name") ' 输出 John
  
      ' 修改字典中的值
      myDict("Age") = 35
  
      ' 遍历字典
      For Each key In myDict.Keys
          MsgBox key & ": " & myDict(key)
      Next key
  End Sub
  ```
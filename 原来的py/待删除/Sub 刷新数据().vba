Sub 刷新数据()
    Dim nRow%, cpxx(), cjmc(), Arr(), jg(), nR2%, cMc$
    Dim cPath$, cFile$, wb As Workbook
    Dim ds As Object, n%
    Set ds = CreateObject("Scripting.Dictionary") '创建字典
    cPath = ThisWorkbook.Path & "\"
    nRow = Range("a65536").End(xlUp).Row '数据最大行号
    cpxx = Range("a4:b" & nRow).Value '产品信息
    cjmc = Range("g3:i3").Value '车间名称
    ReDim jg(1 To nRow - 3, 1 To 3) '定义数组jg(),保存查询结果
    For i = 1 To nRow - 3
        ds(Trim(cpxx(i, 1)) & Trim(cpxx(i, 2))) = i ' 将“生产单号+产品规格”对应行号保存到字典
    Next
    Application.ScreenUpdating = False
    For j = 1 To 3 '遍历各车间
        cMc = Left(cjmc(1, j), Len(cjmc(1, j)) - 4) '当前车间名称
        cFile = Dir(cPath & "*" & cMc & "*")
        If cFile <> "" Then
            Set wb = Workbooks.Open(cPath & cFile) '打开数据文件
            With wb.Sheets(1)
                nR2 = .Range("a1048576").End(xlUp).Row
                Arr = .Range("a6:h" & nR2).Value '将数据保存到数组Arr
                For i = 1 To nR2 - 5
                    n = ds(Trim(Arr(i, 1)) & Trim(Arr(i, 2))) '查字典
                    If n > 0 Then
                        jg(n, j) = Arr(i, 8) '将未完成数量保存到数组jg()
                    End If
                Next
            End With
            wb.Close (False) '关闭工作簿
        End If
    Next
    Range("g4:i" & nRow).Value = jg '将查询结果jg()输出到工作表
    Application.ScreenUpdating = True
    MsgBox "完成刷新"
End Sub

import xlwings as xw
app = xw.App(visible=False, add_book=False)  # 启动excel，但不新建
workbook = app.books.add()  # 新建工作簿
for i in range(6):

    worksheet = workbook.sheets.add("sh"+str(i))  # 新建工作表

workbook.save(f'test.xlsx')  # 保存
workbook.close()  # 关闭工作簿
app.quit()  # 退出excel程序

#workbook.sheets.add(sheet_name)
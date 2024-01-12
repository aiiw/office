import xlrd
book=xlrd.open_workbook('excel/9.xlsx') #打开Excel
sheet=book.sheet_by_name('Sheet1') #根据编号获取sheet页
#sheet=book.sheet_by_name('sheet1') #也可以根据sheet页名字获取sheet页
#、第一步将excel表读取到二维表---->list2
book1=xlrd.open_workbook('excel/n.xlsx') #打开Excel
sheet1=book1.sheet_by_name('Sheet1') 
import re
list=[]
list1=[]
list2=[]
str=""
for key,val in sheet.__dict__.items():#打印属性　dir(list)打印　方法

	str=str+" , "+key
# str="rowadfd dfdfro dsadfdrow"
# print(re.findall('\S*cell\S*', str))
# print(sheet._cell_values[0])
list=sheet._cell_values+sheet1._cell_values[1]
# 快速写
# def takeSecond(elem):
#     return int(elem[0])
import xlwings as xw
app=xw.App(visible=False,add_book=False)
list4=[]
book=app.books.add()
sheet=book.sheets['sheet1']
sheet.range('a1').value=list
book.save('excel\\77.xlsx')
book.close()
app.quit()
		
# print(sheet.cell(0,0).value) #获取到指定单元格的内容
# print(sheet.cell(0,1).value) #获取到指定单元格的内容

# print(sheet.row_values(0))  #获取到整行的内容
# print(sheet.col_values(0))   #获取到整列的内容

# for i in range(sheet.nrows):  #循环获取每行的内容
#     print(sheet.row_values(i))
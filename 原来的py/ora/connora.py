import cx_Oracle 
connection = cx_Oracle.Connection("dsdata/dsdata@T100")
import xlwt
book = xlwt.Workbook()  #创建 excel
sheet = book.add_sheet('sheet1')     #创建sheet页
sheet.write(0,0,'名字')   #编辑表头
sheet.write(1,0,'王一')   #编辑内容
sheet.write(2,0,'王二')

sheet.write(0,1,'手机号')  #编辑表头
sheet.write(1,1,'119')     #编辑内容
sheet.write(2,1,'110')

book.save("students.xls")  #保存下，xlsx也可以保存，但会打不开，使用wps可以打开，使用微软的会打不开

#保存的时候，如果是微软的office,后缀.xls
#保存的时候，如果是wps .xls .xlsx都可以

#给定文件内容：
stus= [
    ['id', 'name', 'sex', 'age', 'addr', 'grade', 'phone', 'gold'],
    [314, '矿泉水', '男', 18, '北京市昌平区', '摩羯座', '18317155663', 14405],
    [315, '矿泉水', '女', 27, '上海', '摩羯座', '18317155664', 100],
    [5985, '矿泉水', '男', 18, '北京市昌平区', '班级', '18513867663', 100]
]

#内容写入Excel
#book=xlrt.Workbook() #新建一个Excel
sheet=book.add_sheet('sheet2') #新建一个sheet页

row = 0#行号
for stu in stus:#控制行
    col = 0#列号
    for field in stu:#控制列的
        sheet.write(row,col,field)
        col+=1 #列号
    row+=1

book.save('students.xls') #保存内容
#如下为读excel
import xlrd
book=xlrd.open_workbook('students.xls') #打开Excel
sheet=book.sheet_by_index(0) #根据编号获取sheet页
#sheet=book.sheet_by_name('sheet1') #也可以根据sheet页名字获取sheet页

print(sheet.nrows) #Excel里有多少行
print(sheet.ncols)  #Excel里有多少列

print(sheet.cell(0,0).value) #获取到指定单元格的内容
print(sheet.cell(0,1).value) #获取到指定单元格的内容

print(sheet.row_values(0))  #获取到整行的内容
print(sheet.col_values(0))   #获取到整列的内容

for i in range(sheet.nrows):  #循环获取每行的内容
    print(sheet.row_values(i))
#如下为修改excel
#import xlutils

from xlutils import copy
import os

book=xlrd.open_workbook('students.xls')
#先用xlrd打开一个Excel
new_book=copy.copy(book)
#然后用xlutils里面的copy功能，复制一个Excel

sheet=new_book.get_sheet(0) #获取sheet页，注意这里的sheet 页是xlutils里的，只能用.get_sheet()的方法获取了

sheet.write(0,0,'aiiw')

os.rename('students.xls','student_bak1.xls') #先把之前的Excel改下名字，之前的内容不至于丢失

new_book.save('student.xls') #修改完内容后再保存成同名的Excel


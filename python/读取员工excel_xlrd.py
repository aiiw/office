import xlrd
book=xlrd.open_workbook('excel/工号.xlsx') #打开Excel
sheet=book.sheet_by_name('Sheet１') #根据编号获取sheet页
#sheet=book.sheet_by_name('sheet1') #也可以根据sheet页名字获取sheet页
#、第一步将excel表读取到二维表---->list2
nrows=sheet.nrows
list1=[]
list2=[]
tp={}
for i in range(1,nrows):#左开右不开
	# print(sheet.row_values(i))#第一行内容
	list1=[(str(sheet.row_values(j)[0])[0:5],str(sheet.row_values(j)[1])[0:5]) for j in range(1,nrows)]
	list2=[str(sheet.row_values(k)[1])[0:5] for k in range(1,nrows)]
import sys,locale

list2=["update  t set t.CardNumber='%s' from T_HR_PunchRecord t where t.CardNumber='%s'"%(str(sheet.row_values(m)[1])[0:5],str(sheet.row_values(m)[0])[0:5]) for m in range(1,nrows)]
for l2 in list2:
	print(l2)
li=','.join("'%s'"%(str(sheet.row_values(item)[0])[0:5]) for item in range(1,nrows)) #(item)这里加不加()都一样
print(type(li))
psql="select * from T_HR_PunchRecord t where t.CardNumber in ({})".format(li) #format(放)的是str,这里的str已经是一个最终的结果，已经拼接好了的

print(psql)


print(li)
sys.path.append("..")
print(list1)
# print(sys.getdefaultencoding())
# print(locale.getdefaultlocale())
import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '192.168.0.180'
#登陆用户名和密码
userName = 'sa'
passWord = '$u2930123WJ'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "KQA")
cursor = conn.cursor()
# try:
# 	print("aa1")
# 	sql="update emp0315 set id=(%s) where id=(%s)"
# 	cursor.executemany(sql,list1)
# 	conn.commit()
# 	print("aa2")
# except:
# 	print("aiiw")
# 	conn.rollback()

# print(list2)
list3=['10766','11608']

sql = "select id from emp0315 where id in ({}) ".format(
            ','.join(["'%s'" % item for item in list3]))
lstr=','.join(["--'%s'--" % item for item in list3])
print(lstr)

cur=conn.cursor()

cur.execute(sql)
rs=cur.fetchall()
print(rs)
conn.close()



















# # 快速写
# import xlwings as xw
# app=xw.App(visible=False,add_book=False)
# list4=[]
# book=app.books.add()
# sheet=book.sheets['sheet1']
# sheet.range('a1').value=list4
# book.save('excel02\\77.xlsx')
# book.close()
# app.quit()
		
# print(sheet.cell(0,0).value) #获取到指定单元格的内容
# print(sheet.cell(0,1).value) #获取到指定单元格的内容

# print(sheet.row_values(0))  #获取到整行的内容
# print(sheet.col_values(0))   #获取到整列的内容

# for i in range(sheet.nrows):  #循环获取每行的内容
#     print(sheet.row_values(i))
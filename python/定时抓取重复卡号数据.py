
import pymssql
from sendoa import sendoa
#sql服务器名，这里(127.0.0.1)是本地数据库IP

serverName = '192.168.0.180'
#登陆用户名和密码
userName = 'sa'
passWord = '$u2930123WJ'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "KQA")
cursor = conn.cursor()

sql = '''select convert(nvarchar(50),e.id), convert(nvarchar(50),e.EMPNAME),e.StopSalaryFlag,e.JOBID from employee e where e.jobid in (
select t.JOBID from EMPLOYEE t
group by t.JOBID having count(t.id)>1)
and e.JOBID <>'' '''
cur=conn.cursor()

cur.execute(sql)
rs=cur.fetchall()
sendoa(rs,'11608')
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
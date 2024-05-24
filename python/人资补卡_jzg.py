import sys,locale
sys.path.append("..")
print(sys.getdefaultencoding())
print(locale.getdefaultlocale())
import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '192.168.0.180'
#登陆用户名和密码
userName = 'sa'
passWord = '$u2930123WJ'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "KQA")
cursor = conn.cursor()

import xlrd
#如下借助了excel
book=xlrd.open_workbook('C:\\Users\\11608\\Desktop\\jzg.xlsx') #打开Excel
sheet=book.sheet_by_name('Sheet1')
list2=[]
for i in range(sheet.nrows):  #循环获取每行的内容
	list1=sheet.row_values(i)
	# list2=[str(list1[0]),list1[2],list1[3],list1[4]]
	list2.append((str(list1[0]),str(list1[4]),list1[2],list1[3],))
print(list2)
sql= f'INSERT into WorkCardSource values(%s,%s,%s,%s)'
# 查询记录
cursor.executemany(sql,list2)
# # 连接用完后记得关闭以释放资源
conn.commit()
conn.close()

import connector
import time
import os
os.system('color 12')
from pymysql.cursors import DictCursor
import pymysql
mydb = connector.connect(
  host="192.168.0.7",
  user="root",
  passwd="123456",
  database="dj3",
  auth_plugin='mysql_native_password', #要加上这个东东才行,

)
 

mycursor = mydb.cursor()
 
sql= f'select * from ladp_120 where status="正常"'
# 查询记录
mycursor.execute(sql)
listall=mycursor.fetchall()
print(listall[27][5][1:-1])
listone=listall[27][5][1:-1].split(r",")
listtow=[i for i in listone if i.find("OU")!=-1]
liststr=str(listtow)
print("----")
liststr1=liststr[1:-1].replace('OU=','')
liststr2=liststr1.replace(',','-->')
print(liststr2)
for item in listall:
	listone=item[5][1:-1].split(r",")
	listtow=[i for i in listone if i.find("OU")!=-1]
	liststr=str(listtow)
	liststr1=liststr[1:-1].replace('OU=','')
	liststr2=liststr1.replace(',','-->')
	print(item[3],"      :",liststr2)

mydb.close()



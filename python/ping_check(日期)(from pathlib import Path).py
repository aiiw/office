import connector
import os
import xlwings as xw
from datetime import datetime,date
from time import time,localtime,strftime
from pathlib import Path
#################################
app = xw.App(visible=False)#其中参数visible（表示处理过程是否可视，也就是处理Excel的过程会不会显示出来），
                                         # add_book（是否打开新的Excel程序，也就是是不是打开一个新的excel窗口）
book = app.books.add()

sheet = book.sheets['sheet1'] #这个地方好像固定是这样写的?
##################################
os.system('color 12')
from pymysql.cursors import DictCursor
import pymysql

mydb = connector.connect(
    host="192.168.0.7",
    user="root",
    passwd="123456",
    database="dj3",
    auth_plugin='mysql_native_password',

)

mycursor = mydb.cursor()
sql="select user_name,byname,LAST_VISIT_IP from auto_user"
mycursor.execute(sql)
rs_all=mycursor.fetchall()
print(rs_all)
ls=[]
begin_time=time()
for rs_one in  rs_all:
        ip=rs_one[2]
        print(ip)
        a=os.system("ping %s -n 1 "%ip)
        print(a) #0为成功非0为失败
        if a==0:
            date1=datetime.now(), #将内容转为元组,注意这里的一个豆号
            newTuple=date1+rs_one #类似 列表.append
            ls.append(newTuple)  #构建一个列表,每个列表是一个元组,即列表为行,元组为行的内容.第一行(1,2,3,4,5)
sheet.range('a1').value = ls #这个ls为[(row),(row)]
book.save('ip.xlsx')
book.close()
app.quit()
end_time=time()
total_time=end_time-begin_time
print(total_time)
total_time=time()+total_time
print(strftime("%Y-%m-%d %X", localtime(total_time))) #将时间措通过time.localtime转为时间结构体,再通过time.strftime转为yyyy-mm-dd HH:ss:mm
filename=str(date.today())+'('+str(strftime("%X",localtime() )).replace(":", "")+")" #这里要拼接一个新的文件名
mypath=Path('ip.xlsx')#获取需要更新的文件
mypath.rename(filename+'.xlsx')#将旧的文件改为新的文件
#如下这些是将文件归档到到统一的目录
NewDir=Path(r'ping_log')
if not NewDir.exists():
    NewDir.mkdir(parents=True)
NewFile=Path(filename+'.xlsx')
NewFile.replace(f'ping_log//{filename}.xlsx')  #系统无法将文件移到不同的磁盘驱动器 只能是同一个分区

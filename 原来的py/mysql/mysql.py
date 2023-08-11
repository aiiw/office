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
  database="mysql",
  auth_plugin='mysql_native_password', #要加上这个东东才行,

)
 

mycursor = mydb.cursor()
 
mycursor.execute("SHOW DATABASES")
data=mycursor.fetchall()
print(data,",")

mycursor.execute("select * from user")
result=mycursor.fetchall()
for row in result:
  # print(row[0],row[1],row[2],row[3])
  print(type(row))
print("=================================")

# time.sleep(150) #秒
# #s1=mycursor.execute("select * from test.user")
# #data = mycursor.fetchone()
# #print(data)
# #mycursor.execute("select * from test.user")
# #单条输入
# sql = "INSERT INTO user(id, \
#        username, sex, birthday, address) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
# mycursor.execute(sql)
# mydb.commit() 
# #批量输入
# sql = "INSERT INTO user (id, username,sex,birthday,address) VALUES (%s, %s,%s, %s,%s)"
# val = [
#   ('Google', 'https://www.google.com','12','23','44'),
#   ('Github', 'https://www.github.com','12','23','44'),
#   ('Taobao', 'https://www.taobao.com','12','23','44'),
#   ('stackoverflow', 'https://www.stackoverflow.com/','12','23','44')
# ]
 
# mycursor.executemany(sql, val)
# mydb.commit()
# #update
# sql="update user u set u.id='google1' where u.id='google'"
# mycursor.execute(sql)
# mydb.commit()
# mydb.close()


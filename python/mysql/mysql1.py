import pymysql
import numpy as np
import pandas as pd
conn = pymysql.connect(host='192.168.0.7', user='root', passwd='123456', db='dj3', charset='utf8')
mycursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
mycursor.execute("select * from emp")
result=mycursor.fetchall()
lst = []
for row in result:
  # print(row[0],row[1],row[2],row[3])
  print(row)
print("=================================")
print(result)
df = pd.read_sql("select Host from emp", conn)
df1 = np.array(df)
column_list = list(df.columns)
print(column_list)
for row in df1:

# 循环每一行数据，组装成一个字典，然后得到字典的列表

	lst.append(dict(zip(column_list, list(row))))
print(lst)
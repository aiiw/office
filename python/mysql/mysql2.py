import pymysql
import numpy as np
import pandas as pd
conn = pymysql.connect(host='192.168.0.7', user='root', passwd='123456', db='dj3', charset='utf8')
mycursor = conn.cursor()
mycursor.execute("select id dd from emp")
print(mycursor.description)
result = mycursor.fetchall()

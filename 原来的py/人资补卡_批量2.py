
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

d0=[i for i in range(24,28)]

print (d0)


d1=['2021-09-%s 00:00:00.000'%i for i in d0]
# t1=['07:28:21','11:32:21','12:59:21','17:39:21']
import collections 
dic = collections.defaultdict(list) #实则不用这个,直接用列表就可以解决了
import xlrd
#如下借助了excel
book=xlrd.open_workbook('C:\\Users\\11608\\Desktop\\2.xlsx') #打开Excel
sheet=book.sheet_by_name('Sheet1')
for i in range(sheet.nrows):  #循环获取每行的内容
    dic['key'].append(sheet.row_values(i))
t0=dic['key']

print(t0)
n=-1

for d in d1:
	n=n+1
	for t in t0[n]:

		value=('16','61564',d,t)
		sql= f'INSERT into WorkCardSource VALUES {value}'
		print(sql)





		cursor.execute(sql)
		# 查询记录
		

conn.commit()
conn.close()

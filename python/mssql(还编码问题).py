#coding=gbk
import sys,locale

# sys.path.append("..")
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

# 查询记录
sql1="select convert(nvarchar(12),id)  from employee  where id ='方高燕'"
sql1="select id  from employee  where id ='方高燕'"
cursor.execute(sql1)
# 获取一条记录
row = cursor.fetchone()
b='方高燕'
print(b.encode('unicode_escape'))
print(b.encode('utf-8').decode().encode())
print(b.encode('gbk').decode('gbk').encode('gbk'))
# 循环打印记录(这里只有一条，所以只打印出一条)
c=r'\xb7\xbd\xb8\xdf\xd1\xe0'
print(c.encode('gbk'))

while row:
	a=row[0].encode('unicode_escape')
	b=a.decode('gbk')
	# c=row[0].encode('gbk')
	
	

	# b=row[8].encode('gbk').decode('utf-8')
	print(a)
	print(b)
	row = cursor.fetchone()
# 连接用完后记得关闭以释放资源
conn.close()
a=input()
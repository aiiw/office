#62917  梁土英 20号7:30   11:30   13:30  17:30 21号7:30 11:30 13:30 19:30 22号 7：30 考勤请签上



import sys,locale

aa=sys.path.append(".") #这个表示当前路径
print(sys.path,"aai")
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
value=('016','11608','2024-01-09 00:00:00.000','18:08:25')
sql= f'INSERT into WorkCardSource VALUES {value}'
# 查询记录
cursor.execute(sql)

# 获取一条记录
# row = cursor.fetchone()
# # 循环打印记录(这里只有一条，所以只打印出一条)
# while row:
# 	# a=row[0].encode('utf-8')
# 	# b=row[8].encode('gbk').decode('utf-8')
	
# 	row = cursor.fetchone()
# # 连接用完后记得关闭以释放资源
conn.commit()
conn.close()


# 11497 09:00
# 11307 09:30
# 10418 07:56
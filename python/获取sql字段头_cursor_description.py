import json
import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '192.168.0.180'
#登陆用户名和密码
userName = 'sa'
passWord = '$u2930123WJ'
#建立连接并获取cursor
conn = pymssql.connect(serverName , userName , passWord, "KQA")

def gethead(sql):
	cursor=conn.cursor()
	cursor.execute(sql)
	desc=cursor.description
	meat=[]
	for item in desc:
		meat.append(item[0])
	# return(meat)
	return desc
a=gethead("select * from workcardsource")
print(a)



# import json
# import pymssql
# #sql服务器名，这里(127.0.0.1)是本地数据库IP
# serverName = '192.168.0.180'
# #登陆用户名和密码
# userName = 'sa'
# passWord = '$u2930123WJ'
# #建立连接并获取cursor
# conn = pymssql.connect(serverName , userName , passWord, "KQA")

# def gethead(sql):
# 	cursor=conn.cursor()
# 	cursor.execute(sql)
# 	desc=cursor.description
# 	meat=[]
# 	for item in desc:
# 		meat.append(item[0])
# 	return(meat)
# a=gethead("select * from workcardsource")
# print(a)
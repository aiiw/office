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
print('unicode_escape   ',b.encode('unicode_escape'))
print('utf-8   ',b.encode('utf-8'))
print('gbk  ',b.encode('gbk').decode('gbk').encode('gbk'))
# 循环打印记录(这里只有一条，所以只打印出一条)
c=r'\xb7\xbd\xb8\xdf\xd1\xe0'
print(c.encode('gbk'))


while row:
	a=row[0].encode('unicode_escape')
	b=row[0].encode('latin-1')#这个简单点说就是将str转换为byte对像，以便可以使用正常的gbk,进行decode
	# c=row[0].encode('gbk')
	# print(len(row[0][0]))
	# print(hex(ord(row[0][0])))#这个提取出来的是ＧＢＫ码来的\xb7\xbd\xb8\xdf\xd1\xe0
	# print("单独",row[0][0:1])
	
	print("--------------------------")
	# b=row[8].encode('gbk').decode('utf-8')
	print('unicode_escape',a) #这个与第一行有区分了，同的字符集，在这里用unicode表示的话，是表示ＧＢＫ码了
	print(b)
	print(b.decode('gbk'))
	print("--------------------------")
	row = cursor.fetchone()
# 连接用完后记得关闭以释放资源
conn.close()

o=hex(ord("方"))
print("方",o)  #这里证明了从文件读到内存里的编码为unicode,其实按我理解，不用关注unicode,这个是中间码，
# 这个文件的编码为ansi,即采用ＧＢＫ的，可以要求声明也要用ＧＢＫ标明，标明后python解释器会使用ＧＢＫ进行
# 编码自动转换，即：在文件中的使用ＧＢＫ读取"方"为：Ｂ７ＢＤ，实际在本文的查编码已经是unicode："65Ｂ9"
#coding=gbk
import sys,locale

# sys.path.append("..")
# print(sys.getdefaultencoding())
# print(locale.getdefaultlocale())
import pymssql
#sql��������������(127.0.0.1)�Ǳ������ݿ�IP
serverName = '192.168.0.180'
#��½�û���������
userName = 'sa'
passWord = '$u2930123WJ'
#�������Ӳ���ȡcursor
conn = pymssql.connect(serverName , userName , passWord, "KQA")
cursor = conn.cursor()

# ��ѯ��¼
sql1="select convert(nvarchar(12),id)  from employee  where id ='������'"
sql1="select id  from employee  where id ='������'"
cursor.execute(sql1)
# ��ȡһ����¼
row = cursor.fetchone()
b='������'
print(b.encode('unicode_escape'))
print(b.encode('utf-8').decode().encode())
print(b.encode('gbk').decode('gbk').encode('gbk'))
# ѭ����ӡ��¼(����ֻ��һ��������ֻ��ӡ��һ��)
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
# ���������ǵùر����ͷ���Դ
conn.close()
a=input()
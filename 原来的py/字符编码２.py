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
print('unicode_escape   ',b.encode('unicode_escape'))
print('utf-8   ',b.encode('utf-8'))
print('gbk  ',b.encode('gbk').decode('gbk').encode('gbk'))
# ѭ����ӡ��¼(����ֻ��һ��������ֻ��ӡ��һ��)
c=r'\xb7\xbd\xb8\xdf\xd1\xe0'
print(c.encode('gbk'))


while row:
	a=row[0].encode('unicode_escape')
	b=row[0].encode('latin-1')#����򵥵�˵���ǽ�strת��Ϊbyte�����Ա����ʹ��������gbk,����decode
	# c=row[0].encode('gbk')
	# print(len(row[0][0]))
	# print(hex(ord(row[0][0])))#�����ȡ�������ǣǣ£�������\xb7\xbd\xb8\xdf\xd1\xe0
	# print("����",row[0][0:1])
	
	print("--------------------------")
	# b=row[8].encode('gbk').decode('utf-8')
	print('unicode_escape',a) #������һ���������ˣ�ͬ���ַ�������������unicode��ʾ�Ļ����Ǳ�ʾ�ǣ£�����
	print(b)
	print(b.decode('gbk'))
	print("--------------------------")
	row = cursor.fetchone()
# ���������ǵùر����ͷ���Դ
conn.close()

o=hex(ord("��"))
print("��",o)  #����֤���˴��ļ������ڴ���ı���Ϊunicode,��ʵ������⣬���ù�עunicode,������м��룬
# ����ļ��ı���Ϊansi,�����ãǣ£˵ģ�����Ҫ������ҲҪ�ãǣ£˱�����������python��������ʹ�ãǣ£˽���
# �����Զ�ת�����������ļ��е�ʹ�ãǣ£˶�ȡ"��"Ϊ���£��£ģ�ʵ���ڱ��ĵĲ�����Ѿ���unicode��"65��9"
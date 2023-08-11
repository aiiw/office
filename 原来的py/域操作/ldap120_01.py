import sys
import json
import re
#查询作用,通过部门查人员
from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES,ALL, NTLM
server = Server('192.168.0.120', get_info=ALL)
conn = Connection(server, user='mastercn\\Dnk', password='M2925090', auto_bind=True, authentication=NTLM)
conn1 = Connection(server, user='mastercn\\Dnk', password='M2925090', auto_bind=True, authentication=NTLM)
res = conn.search('dc=mastercn,dc=local', search_filter ='(objectCategory=organizationalUnit)', attributes=['*'],size_limit=25000, get_operational_attributes=True)
result=conn.entries[1].entry_to_json()
num=len(conn.entries)
print("一共有%s个组织架构"%num)
list2=[]
for a in range(0,num):
	rs=conn.entries[a].entry_to_json()
	# dic_rs=json.loads(rs).get('attributes','a').get('distinguishedName','b')[0]
	# json_rs=json.dumps(dic_rs,sort_keys=True,indent=5,ensure_ascii=False)
	dic_rs_str=json.loads(rs).get('attributes','a').get('distinguishedName','b')[0]
	list_rs=dic_rs_str.split(',')
	# json_rs=json.dumps(dic_rs,sort_keys=True,indent=5,ensure_ascii=False)
	search01=[a for a in list_rs if 'OU'  in a]
	search02=str(search01)
	# print(search02[1:-1])
	search03=search02[1:-1]
	#sub 方法用于替换
	p = re.compile(r'[\']+')
	# print (p.sub(r' ', search03))  #两上参数，第一个是需要替换的字符，第二个是源 使用 'hello world' 替换 'hello 123' 和 'hello 456'
	search04=p.sub(r' ', search03)
	# print(search04)
	# print('{},dc=mastercn,dc=local'.format(search04))                                                      
	search04='{},dc=mastercn,dc=local'.format(search04)
	ss=' OU=设备管理科 ,  OU=SBB设备部 ,  OU=Mastergroup ,dc=mastercn,dc=local'
	p=re.compile(r'\s')
	search05=p.sub('',search04)
	# print(search05)
	# user01=conn1.search(search_base='{}.format(search05),dc=mastercn,dc=local', search_filter ='(objectClass=person)', attributes=['*'],size_limit=1000, get_operational_attributes=True)
	# user01=conn1.search(search05, search_filter ='(objectClass=person)', attributes=['*'],size_limit=25000, get_operational_attributes=True)#这个会带出电脑
	user01=conn1.search(search05, search_filter ='(objectCategory=person)', attributes=['*'],size_limit=25000, get_operational_attributes=True,search_scope = 1) #search_scope 为1是不包含下级,2为包含下级
	num01=len(conn1.entries)

	for b in range(0,num01):

		list1=[]
		rs1=conn1.entries[b].entry_to_json()
		name=json.loads(rs1).get('attributes','a').get('name','b')[0]
		account=json.loads(rs1).get('attributes','a').get('userPrincipalName','为空')[0]
		department=search05
		memberOf=str(json.loads(rs1).get('attributes','a').get('memberOf','为空'))
		status=json.loads(rs1).get('attributes','a').get('userAccountControl','为空')[0]
		if status==512:
			status='正常'
		elif status==2:
			status='禁用'
		elif status==514:
			status='账号正常+禁用'
		elif status==66048:
			status='密码不过期+正常'
		elif status==66050:
			status='密码不过期+正常+禁用'
		list1.append(a)
		list1.append(status)
		list1.append(department)
		list1.append(name)
		list1.append(account)
		list1.append(memberOf)
		print(memberOf.split(''))
		list2.append(list1)
# print(list2)
# import xlwings as xw
# app=xw.App(visible=False,add_book=True)
# book=app.books.add()
# sheet=book.sheets['sheet1']
# sheet.range('a1').value=list2
# book.save('88.xlsx')
# book.close()
# app.quit()
#512 正常 2 禁用  514=账号正常+禁用
#66050=65536+512+2 密码不过期+正常+禁用
#66048=65536+512 密码不过期+正常

#######################################以上是导入excel################################################
# SELECT COUNT(*) FROM information_schema.TABLES WHERE table_name ='ladp_120'
# SELECT COUNT(*) FROM information_schema.TABLES WHERE table_name ='ladp_120'
# truncate table ladp_120
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
  database="dj3",
  auth_plugin='mysql_native_password', #要加上这个东东才行,

)
 

mycursor = mydb.cursor()
 
mycursor.execute("truncate table ladp_120")

sql= f'INSERT into ladp_120(num,status,ou,name,account,menof) values(%s,%s,%s,%s,%s,%s)'
# 查询记录
mycursor.executemany(sql,list2)
mydb.commit()
mydb.close()



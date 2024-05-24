from bs4 import BeautifulSoup
import re
import html
import requests,json
from urllib.parse import  quote,unquote
import xlwings as xw
# quote()
# 导入：from urllib.parse import quote
# 传入参数类型：字符串（传递中文参数给URL）
# 功能：将单个字符串编码转化为 %xx%xx 的形式
############new oa
import connector
import time
import os
os.system('color 12')
from pymysql.cursors import DictCursor
import pymysql
mydb = connector.connect(
  host="192.168.0.102",
  port= 3336,
  user="root1",
  passwd="root1",
  database="TD_OA",
  auth_plugin='mysql_native_password', #要加上这个东东才行,

)
############end new oa
import sys
session = requests.Session()


form_data = {
    "UNAME": "11608",
    "PASSWORD": "!@12qwaszx",
    "encode_type": 1,
}

i2 = session.post('http://192.168.0.101/logincheck.php', data=form_data)
c2 = i2.cookies.get_dict()
print(c2)
str1=""
for key,d in c2.items():
	str1=str1+key+"="+d+";"
print(str1)
headers = {
    'Cookie':str1,
    # 'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registr1ation_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
    'Host': '192.168.0.101',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
}
# a='<div><span style="color:#FF0000;"><str1ong>这是通过后台发送的信息!!</str1ong></span></div>'
# a1=a.encode('gbk')
# print(a1)
# data = {'TO_UID':'66','TO_NAME':'','TD_HTML_EDITOR_CONTENT':a1,'I_VER':'2','C':'web','ACTION_TYPE':'sms'}
# url = json.dumps(data).encode('utf8')
# data1=json.loads(url)
# print(url,type(url))

 # print(data1)
 # print(data)

mycursor = mydb.cursor()
#mycursor.execute("select  FORM_ID,form_name from bpm_form_version where use_flag='1' and form_id in ('298','300','309','299','298')")
mycursor.execute("select  FORM_ID,form_name from bpm_form_version where use_flag='1' ")
#mycursor.execute("select  FORM_ID,form_name from bpm_form_version where use_flag='1' and form_id ='287' ")
result=mycursor.fetchall()
app=xw.App(visible=False,add_book=True)
book=app.books.add()
pattern = re.compile(r'\/|\（|\）')
for item in result:
	form_id=item[0]
	form_name=item[1]
	form_name=pattern.sub(r'', form_name)
	# if form_id==287:
	# 	form_id=1
	print(form_id,form_name)
	html_doc = requests.get( r'http://192.168.0.101/general/system/approve_center/flow_form/cool_form/ue.php?FORM_ID={}'.format(form_id), headers=headers,timeout=20)
 # print( unquote(r.content.decode( 'utf-8' )) )
#html_doc=unquote(html_doc.content.decode( 'utf-8' )) 
	html_doc=html_doc.text
#960为11608  1为admin

#soup = BeautifulSoup(html_doc, 'html.parser')

	soup = BeautifulSoup(html_doc, 'lxml')
#print(soup.prettify())#整个DOM 加上prettify 格式化
#ls = soup.find_all(['textarea', 'input'],attrs={"name":re.compile(r'DATA')})
	form1=soup.find(['form'],attrs={"name":"form1"})
	form2=html.unescape(str(form1)) # 这个地方会将实体转会非实体,当然转之前要将对象转为字符串
# print(form2)
#这个时候 form2是字符串来的,要转为bs4对象,再操作一次

	soup1=BeautifulSoup(form2,'html.parser')
	#t2=soup1.find(['table'],attrs={"class","td-min-height"})
	t2=soup1.find(['table'])
	if  t2:
		# t1=soup1.find(['table'],attrs={"class","td-min-height"}).find_all(['input','select','textarea','img'])
		t1=soup1.find(['table']).find_all(['input','select','textarea','img'])
		ls=[]
		for t in t1:
			if t.name=='img' and t.get('lv_title') and t.get('name'):
				tup=t['name'],t.get('lv_title'),
				print(t.get('lv_title'))
			# print(t['name'],t['title'])  #获取 属性   通常使用soup.tagName[attr]简化上面两个方法，例如：soup.a['href']，获取第一个a标签的href属性
			elif t.get('title') and t.get('name'):
				tup=t['name'],t['title'],
			ls.append(tup)
	#soup.a.string 获取a标签的文本内容，如果里面嵌套标签，则为None

		print(ls)
		sheet=book.sheets.add(form_name)
		ls.sort()
		sheet.range('a1').value=ls
book.save('flow1.xlsx')
book.close()
app.quit()


 




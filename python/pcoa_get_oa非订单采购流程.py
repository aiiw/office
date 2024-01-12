from bs4 import BeautifulSoup
import re
import html
import requests,json
from urllib.parse import  quote,unquote
import xlwings as xw
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  # [ 这个用来 解决 乱码]
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

str1=""
for key,d in c2.items():
	str1=str1+key+"="+d+";"

headers = {
    'Cookie':str1,
    # 'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registr1ation_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
    'Host': '192.168.0.101',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
}
url='http://192.168.0.106/lgt_workflow/archive.php?flow_id=293&id=61'
res = requests.get( r'http://192.168.0.106/lgt_workflow/archive.php?flow_id=293&id=61')
requests.encoding='gb18030'
# #html_doc=html_doc.text.encode('utf-8').decode('utf-8')
# # print(html_doc)
# form2=html.unescape(str(res.text)) # 这个地方会将实体转会非实体,当然转之前要将对象转为字符串
# # print(form2)
# #这个时候 form2是字符串来的,要转为bs4对象,再操作一次




soup1=BeautifulSoup(res.text,'html.parser')


soup1=soup1.find(['table'],attrs={"class":"layui-table"})
t1=soup1.find_all(['tr'])
# encode('utf-8').decode('utf-8')
key=[]
val=[]
for tr in t1:
  td=tr.find_all(['td'],attrs={"width":"30%"})
  input1=tr.find_all(['input'],attrs={"class":"layui-input","style":"min-width: 300px;"})

  for tag in input1:
      # print(tag.get("value"))
      key.append(tag.get("value"))

  for tag in td:
      # print(tag.text.strip())
      val.append(tag.text.strip())

dic=dict(zip(key,val))



html_mb='''{}: <input type="text" name="{}">'''
html_newmb='''
  <div class="form-group">
    <label for="name">{}</label>
    <input type="text" class="form-control" id="{}" 
         placeholder="使用批量生成">
  </div>

'''
n=0
for key,value in dic.items():
  n=n+1
  if n%3 == 0:
    print(html_newmb.format(value,key)+"</br>")
  else:
    print(html_newmb.format(value,key))





but_mb='''{}: $("#{}").val(),'''
for key,value in dic.items():
  print(but_mb.format(key,key))

for key,value in dic.items():
  print(key,":",value)



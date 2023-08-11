 import requests,json
from urllib.parse import  quote,unquote
from . import connector
import time
import os
class conn():

  mydb = connector.connect(
  host="192.168.0.102",
  port= 3336,
  user="root1",
  passwd="root1",
  database="TD_OA",
  auth_plugin='mysql_native_password' #要加上这个东东才行
)
 

def sendoa(sstr,*id):
  print("begin")
  a=conn()
  print(id)
  mycursor=a.mydb.cursor()
  mid=','.join(["'%s'"%item for item in id])
  sql="select uid from user where BYNAME in(%s)"%mid
  print(sql)
  mycursor.execute(sql)
  sid=mycursor.fetchall()
  print(sid)
  
session = requests.Session()
  form_data = {
      "UNAME": "admin",
      "PASSWORD": "Dnk8090",
      "encode_type": 1,
  }
  i2 = session.post('http://192.168.0.101/logincheck.php', data=form_data)
  c2 = i2.cookies.get_dict()
  
  str=""
  for key,d in c2.items():
    str=str+key+"="+d+";"
  # print(str)
  headers = {
      'Cookie':str,
      # 'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
      'Host': '192.168.0.101',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
      'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
  }
  a='<div><span style="color:#FF0000;"><strong>%s</strong></span></div>'%sstr
  a='''<li>1</li><li>2</li><li>3</li><li>4</li><li>5</li>'''
  a1=a.encode('gbk')
  # print(a1)
  for ssid in sid:
    print(sid)
    data = {'TO_UID':ssid,'TO_NAME':'','TD_HTML_EDITOR_CONTENT':a1,'I_VER':'2','C':'web','ACTION_TYPE':'sms'}
    r = requests.post( r'http://192.168.0.101/general/status_bar/sms_send.php', headers=headers,data=data)
    #<br><p><a><span><strong><b><em><u><img><ul><li><ol><font><div>
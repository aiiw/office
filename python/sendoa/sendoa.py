import requests,json
from urllib.parse import  quote,unquote
from . import connector
import time
import os
def sendoa(sstr,*id):
  conn = connector.connect(
  host="192.168.0.101",
  port= 3336,
  user="root",
  passwd="myoa888",
  database="TD_OA",
  auth_plugin='mysql_native_password' #要加上这个东东才行
)
  mycursor=conn.cursor()
  print(type(id))
  list1=[]
  list2=[]
  list3=[]
  for lid in id:
    print(lid)
    sql="select uid from user where BYNAME ='%s'"%lid
    print(sql)
    mycursor.execute(sql)
    row=mycursor.fetchone()
    if row==None:
      list1.append(lid)
    else:
      list2.append(lid)
      list3.append(row[0])
    print("失败的code",list1)
    print("成功的code",list2)
    print("成功的id",list3)
  mycursor.close()
  conn.close
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
  headers = {
      'Cookie':str,
      # 'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
      'Host': '192.168.0.101',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
      'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
  }
  a='<div><span style="color:#FF0000;"><strong>%s</strong></span></div>'%sstr
  a1=a.encode('gbk')
  # print(a1)
  for ssid in list3:
    data = {'TO_UID':ssid,'TO_NAME':'','TD_HTML_EDITOR_CONTENT':a1,'I_VER':'2','C':'web','ACTION_TYPE':'sms'}
    r = requests.post( r'http://192.168.0.101/general/status_bar/sms_send.php', headers=headers,data=data)

  result1=','.join(list1)
  result2=','.join(list2)
  result="如下这些工号发送成功"+result2+"如下这些工号发送失败"+result1
  return result



    


  



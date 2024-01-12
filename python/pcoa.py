
import requests,json
from urllib.parse import  quote,unquote
# quote()
# 导入：from urllib.parse import quote
# 传入参数类型：字符串（传递中文参数给URL）
# 功能：将单个字符串编码转化为 %xx%xx 的形式
import sys
session = requests.Session()
argv1=sys.argv[1]

form_data = {
    "UNAME": "11608",
    "PASSWORD": "!@12qwaszx",
    "encode_type": 1,
}

i2 = session.post('http://192.168.0.101/logincheck.php', data=form_data)
c2 = i2.cookies.get_dict()
print(c2)
# {'OA_USER_ID': '960', 'PHPSESSID': '9flhmh48j8nkhh9uljga9d1i84', 'SID_960': '83406c81'}
str=""
for key,d in c2.items():
	str=str+key+"="+d+";"
print(str)
# OA_USER_ID=960;PHPSESSID=9flhmh48j8nkhh9uljga9d1i84;SID_960=83406c81;
headers = {
    'Cookie':str,
    # 'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
    'Host': '192.168.0.101',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
}
a='<div><span style="color:#FF0000;"><strong>这是通过后台发送的信息!!</strong></span></div>'
a1=a.encode('gbk')
print(a1)
data = {'TO_UID':'1','TO_NAME':'','TD_HTML_EDITOR_CONTENT':a1,'I_VER':'2','C':'web','ACTION_TYPE':'sms'}
# url = json.dumps(data).encode('utf8')
# data1=json.loads(url)
# print(url,type(url))
for  i in range(1,2):
 # print(data1)
 # print(data)
	r = requests.post( r'http://192.168.0.101/general/status_bar/sms_send.php', headers=headers,data=data)

# print( unquote(r.content.decode( 'utf-8' )) )

#960为11608  1为admin
print(r)
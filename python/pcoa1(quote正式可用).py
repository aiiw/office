
import requests,json
from urllib.parse import  quote,unquote
# quote()
# 导入：from urllib.parse import quote
# 传入参数类型：字符串（传递中文参数给URL）
# 功能：将单个字符串编码转化为 %xx%xx 的形式
import sys
session = requests.Session()


form_data = {
    "UNAME": "11608",
    "PASSWORD": "!@12qwaszx",
    "encode_type": 1,
}

i2 = session.post('http://192.168.0.101/logincheck.php', data=form_data)
c2 = i2.cookies.get_dict()
print(type(i2.cookies))
print(type(c2))
print(c2)
str=""
for key,d in c2.items():
	str=str+key+"="+d+";"
print(str)#{'OA_USER_ID': '960', 'PHPSESSID': 'h3dipehl6lq6uj5lsp3nhcp9l4', 'SID_960': '5a08a137'}
headers = {
    'Cookie':str,
    # 'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
    'Host': '192.168.0.101',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Referer': 'http://192.168.0.101/general/status_bar/sms_back.php?I_VER=2&type=mac&C=Web'
}
a='<div><span style="color:#FF0000;"><strong><table width="200" border="1"><tbody><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr><tr><td>7</td><td>8</td><td>9</td></tr></tbody></table></strong></span></div>'
a1=a.encode('gbk')

data = {'TO_UID':'1','TD_HTML_EDITOR_CONTENT':a,'ACTION_TYPE':'sms'}
# url = json.dumps(data).encode('utf8')
# data1=json.loads(url)
# print(url,type(url))

 # print(data1)
 # print(data)
r = requests.post( r'http://192.168.0.101/general/status_bar/msg_send.php', headers=headers,data=data)

# print( unquote(r.content.decode( 'utf-8' )) )

#960为11608  1为admin
print(r)

import requests,json
from urllib.parse import  quote,unquote

#!/usr/bin/env python
# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup



############## 方式二 ##############
session = requests.Session()

# 1. 携带authenticity_token和用户名密码等信息，发送用户验证
form_data = {
    "UNAME": "11608",
    "PASSWORD": "!@12qwaszx",
    "encode_type": 1,

}

i2 = session.post('http://192.168.0.101/logincheck.php', data=form_data)
c2 = i2.cookies.get_dict()
print(c2)
for a in i2.cookies:
	print(a.name)
for item in i2.cookies.get_dict().items():
	print(item,type(item))



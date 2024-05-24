# -*- coding: utf-8 -*-
# author:laidefa

# 载入包
import requests
import json
import time
import hashlib
from hashlib import md5
def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()
from datetime import datetime, date,  timezone

# 当前时间+3天 print(datetime.datetime.now() + datetime.timedelta(3))
# print(str(datetime.now())) # datatime.now 取当前时间
import re
pattern = re.compile(r'\d+')
m1 = pattern.findall(str(datetime.now()))
a=''
for i in m1:
    a=a+i
print(a[:-3])
timestamp=a[:-3]

name=r"{prod:'testclent',ip:'192.168.4.253',lang:'zh_CN',timestamp:'%s',ver:'1.0'}{prod:'OA',name:'Message'}"%(timestamp)
print(name)
digikey=encrypt_md5(name)
print(digikey)
print(name)
host1={}
service1={}
host1['prod']="testclent"
host1['ip']="192.168.4.253"
host1['lang']="zh_CN"
host1['timestamp']=timestamp
host1['ver']="1.0"
# host1=json.dumps(host1)
service1['prod']="OA"
service1['name']="Message"
# service1=json.dumps(service1)
# datakey={}
# datakey["FromSystem"]="HR"
# # datakey=json.dumps(datakey)

data={"from_id":"admin","to_id":[{"user_id":"11608"}],"content":"ffffffffsfds"}


url='http://192.168.0.51:9990/CROSS/RESTful'

time1=time.time()


print(data)
html = requests.post(url, headers={"content-type": "application/json","digi-protocol": "raw","digi-type": "sync","digi-key": digikey,"digi-host":json.dumps(host1),"digi-service":json.dumps(service1)},data=json.dumps(data))
print(html)

# time2=time.time()
# print('总共耗时：' + str(time2 - time1) + 's')
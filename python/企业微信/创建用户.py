from flask import Flask, make_response,request

import json

import string

import hashlib

import random

import time

import urllib

import redis

import requests


r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379


appid = 'wwda00f8b50a26dbd2' 

sceret = 'ANWGMbduyJhzLoragXRKuYYdH9y4QcDfxNS7oQXc7w0'
sceret='qUnxp4hfdkV9Lseh06CnjWNVYTSWKK84TszSrgq1kuY' #通信录的私钥

def get__token(appid,sceret): 

    ACCESS_TOKEN = r.get('wx:ACCESS_TOKEN') # 从redis中获取ACCESS_TOKEN

    if ACCESS_TOKEN:

        return ACCESS_TOKEN

    try:
        print("这里绕开了redis")
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(appid,sceret) # 创建获取token的url

        response = urllib.request.urlopen(token_url)

        b = response.read().decode('utf-8')

        token = json.loads(b)

        ACCESS_TOKEN = token.get("access_token")

        #r.setex('wx:ACCESS_TOKEN', ACCESS_TOKEN, 7200) # 将获取到的 ACCESS_TOKEN 存入redis中并且设置过期时间为7200s  这里有一个坑,看到没有?

        r.setex('wx:ACCESS_TOKEN', 7200,ACCESS_TOKEN)


        return ACCESS_TOKEN

    except Exception as e:

        return e


# https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='wwda00f8b50a26dbd2'&corpsecret='ANWGMbduyJhzLoragXRKuYYdH9y4QcDfxNS7oQXc7w0'

def wxapi():
    ACCESS_TOKEN=get__token(appid,sceret)
    dept_id='1'
    op='1'
    api_url='https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child={}'.format(ACCESS_TOKEN,dept_id,op)
    response=requests.get(api_url)
    b = response.content.decode( 'utf-8' )



def getdept():
    ACCESS_TOKEN=get__token(appid,sceret)
    api_url='https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={}&id=1'.format(ACCESS_TOKEN)
    response=requests.get(api_url)
    b = response.text


    obj=json.loads(b)
    # print(obj)
    # print(obj.get('userlist'))
    list=[]
    for item in obj.get('department'):

        a=(item.get('id'),item.get('name'),item.get('parentid'))

        list.append(a)
    print(list)
    import sys
    sys.path.append('../') #这个是添加模块的路径

    import connector

    mydb = connector.connect(
    host="192.168.0.101",
    user="root",
    port="3336",
    passwd="myoa888",
    database="TD_OA",
    auth_plugin='mysql_native_password',  # 要加上这个东东才行,

    )
    mycursor = mydb.cursor()
    mycursor.execute('truncate table wx_dept')
    # value=[('16','62917','2021-10-20 00:00:00.000','07:29:00'),('16','62917','2021-10-20 00:00:00.000','11:30:00'),('16','62917','2021-10-20 00:00:00.000','13:29:00'),('16','62917','2021-10-20 00:00:00.000','17:31:00')]
    sql= f'INSERT into wx_dept(vid,name,parentid) values(%s,%s,%s)'
    mycursor.executemany(sql,list)
    mydb.commit()
    mydb.close()

def createuser(code,name,dept,tel):
    ACCESS_TOKEN=get__token(appid,sceret)
    api_url='https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={}'.format(ACCESS_TOKEN)
    mb={
    "userid": code,
    "name": name,
    "mobile": tel,
    "department":['{}'.format(dept)]}
    response=requests.post(api_url,data=mb)
    mb1=json.dumps(mb).encode('utf-8').decode('utf-8')
    print(mb1)
    response=requests.post(api_url,data=json.dumps(mb))#说明这个data参数是用str,重温下,dump将dict转为string,loads将str转为dict(json)
    # response=requests.post(api_url,data=mb)
    print(response.text)
    print(mb)




if __name__ == '__main__':
    # getdept() #获取指定部门
    # getdept() #将部门写入wx_dept表
    # createuser('32690','13622465672')
#使用前请同步下kettle 的同步新增人员的作业

#     import sys
#     sys.path.append('../') #这个是添加模块的路径

#     import connector

#     mydb = connector.connect(
#     host="192.168.0.101",
#     user="root",
#     port="3336",
#     passwd="myoa888",
#     database="TD_OA",
#     auth_plugin='mysql_native_password',  # 要加上这个东东才行,

#     )
#     mycursor = mydb.cursor()
#     sql1='''
# select u.byname, u.user_name, d1.vid,e.phone
#   from user u
#   left join user_add_hr e
#     on e.code = u.byname
#   left join department d
#     on d.DEPT_ID = u.dept_id
#   left join wx_dept d1 on d.DEPT_NAME=d1.`name`

#  where 1 = 1
#    and not exists (select 1 from wx_user t where t.wx_code = u.byname)
#    and e.HireDate > '2022-01-01 00:00:00'
#    and e.employeestatusid = '1'
# '''
#     mycursor.execute(sql1)
#     myrs=mycursor.fetchall()
#     rs_dict={}
#     for item in myrs:
#         if item[2]:
#             print(item)
#             createuser(item[0],item[1],item[2],item[3])
#     # print(rs_dict)
#     mycursor.close()
#     mydb.close()



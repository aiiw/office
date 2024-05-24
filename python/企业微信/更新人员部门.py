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


def getemp():#这里按部门查人员信息
    
    ACCESS_TOKEN=get__token(appid,sceret)
    DEPARTMENT_ID='1' #广东万事泰集团有限公司
    FETCH_CHILD='1'

    api_url='https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child={}'.format(ACCESS_TOKEN,DEPARTMENT_ID,FETCH_CHILD)
    response=requests.get(api_url)
    b = response.content.decode( 'utf-8' )
    #print(b)
    obj=json.loads(b)
    # print(obj)
    # print(obj.get('userlist'))
    list=[]
    for item in obj.get('userlist'):

        a=(item.get('userid'),item.get('name'),item.get('department')[0])

        list.append(a)


    import arrow
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
    mycursor.execute('truncate table wx_user')
    # value=[('16','62917','2021-10-20 00:00:00.000','07:29:00'),('16','62917','2021-10-20 00:00:00.000','11:30:00'),('16','62917','2021-10-20 00:00:00.000','13:29:00'),('16','62917','2021-10-20 00:00:00.000','17:31:00')]
    sql= f'INSERT into wx_user values(%s,%s,%s)'
    mycursor.executemany(sql,list)
    mydb.commit()
    mydb.close()



def getdept():
    ACCESS_TOKEN=get__token(appid,sceret)
    api_url='https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={}&id=1'.format(ACCESS_TOKEN)
    response=requests.get(api_url)
    b = response.text


    obj=json.loads(b)
    # print(obj)
    # print(obj.get('userlist'))
    list=[]
    # print(obj)
    for item in obj.get('department'):

        a=(item.get('id'),item.get('name'),item.get('parentid'))

        list.append(a)

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
    # sql= f'select d.DEPT_NAME,u.BYNAME,u.USER_NAME from user u left join department d on u.DEPT_ID=d.DEPT_ID'
    sql= f'INSERT into wx_dept(vid,name,parentid) values(%s,%s,%s)'
    mycursor.executemany(sql,list)
    mydb.commit()
    mydb.close()

    # print(mysql1)
    #如下为mongodb 学习
    # from pymongo import MongoClient
    # client = MongoClient("mongodb://localhost:27017/")
    # mydb = client["aiiw"] #client 指向数据库
    # mycol = mydb["wx_dept"] # 注意这个地方,这个表是可以直接指定,不需要提前创建

    # x = mycol.insert_many(obj.get('department'))
    # client.close()

def updatedept(id,parentid):
    ACCESS_TOKEN=get__token(appid,sceret)

    api_url='https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={}&debug=1'.format(ACCESS_TOKEN)
    mb={
    "id": id,
    "parentid": parentid}
    response=requests.post(api_url,data=mb)
    mb1=json.dumps(mb).encode('utf-8').decode('utf-8')
    print(mb1)
    response=requests.post(api_url,data=json.dumps(mb))#说明这个data参数是用str,重温下,dump将dict转为string,loads将str转为dict(json)
    # response=requests.post(api_url,data=mb)
    print(response.text)
    print(mb)

def updateuser(code,dept_id):#code,dept_id

    ACCESS_TOKEN=get__token(appid,sceret)

    api_url='https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={}'.format(ACCESS_TOKEN)
    mb={
    "userid": code,
    "department":['{}'.format(dept_id)]}
    response=requests.post(api_url,data=mb)
    mb1=json.dumps(mb).encode('utf-8').decode('utf-8')
    print(mb1)
    response=requests.post(api_url,data=json.dumps(mb))#说明这个data参数是用str,重温下,dump将dict转为string,loads将str转为dict(json)
    # response=requests.post(api_url,data=mb)
    print(response.text)
    print(mb)





if __name__ == '__main__':
    getemp()#同步最新的wx_user
    getdept() #同步最新的wx_dept
    #getdept() #将部门写入wx_dept表
    # updateuser('46425','506')
   
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
    sql1='''select d.DEPT_NAME oa部门,u.BYNAME 工号 ,u.USER_NAME 姓名 ,xu.wx_dept 微信旧部门ID,xd.`name` 微信旧部门,xd1.vid newdeptid  from user u left join department d
on u.DEPT_ID=d.DEPT_ID
left join wx_user xu on xu.wx_code=u.BYNAME
left join wx_dept xd on xu.wx_dept=xd.vid
left join wx_dept xd1 on xd1.`name`=d.DEPT_NAME 
where d.DEPT_NAME<>xd.`name`'''
    mycursor.execute(sql1)
    myrs=mycursor.fetchall()
    rs_dict={}
    for item in myrs:
        if item[5]:
            rs_dict[item[1]]=item[5]
    # print(rs_dict)
    for rs_item in rs_dict.items():
        print(rs_item)
        updateuser(rs_item[0],rs_item[1])
    mycursor.close()
    mydb.close()


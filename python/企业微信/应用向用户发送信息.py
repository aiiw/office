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
sceret='ANWGMbduyJhzLoragXRKuYYdH9y4QcDfxNS7oQXc7w0' #测试应用01

def get__token(appid,sceret): 

	ACCESS_TOKEN = r.get('app01:ACCESS_TOKEN') # 从redis中获取ACCESS_TOKEN

	if ACCESS_TOKEN:

		return ACCESS_TOKEN

	try:

		token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(appid,sceret) # 创建获取token的url

		response = urllib.request.urlopen(token_url)

		b = response.read().decode('utf-8')

		token = json.loads(b)

		ACCESS_TOKEN = token.get("access_token")

		#r.setex('wx:ACCESS_TOKEN', ACCESS_TOKEN, 7200) # 将获取到的 ACCESS_TOKEN 存入redis中并且设置过期时间为7200s  这里有一个坑,看到没有?

		r.setex('app01:ACCESS_TOKEN', 7200,ACCESS_TOKEN)


		return ACCESS_TOKEN

	except Exception as e:

		return e



def createmenu(AgentId):

	ACCESS_TOKEN=get__token(appid,sceret)

	dic={
    "button": [
        {
            "name": "扫码", 
            "sub_button": [
                {
                    "type": "scancode_waitmsg", 
                    "name": "扫码带提示", 
                    "key": "rselfmenu_0_0", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "scancode_push", 
                    "name": "扫码推事件", 
                    "key": "rselfmenu_0_1", 
                    "sub_button": [ ]
                },

            ]
        }, 
        {
            "name": "发图", 
            "sub_button": [
                {
                    "type": "pic_sysphoto", 
                    "name": "系统拍照发图", 
                    "key": "rselfmenu_1_0", 
                   "sub_button": [ ]
                 }, 
                {
                    "type": "pic_photo_or_album", 
                    "name": "拍照或者相册发图", 
                    "key": "rselfmenu_1_1", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "pic_weixin", 
                    "name": "微信相册发图", 
                    "key": "rselfmenu_1_2", 
                    "sub_button": [ ]
                }
            ]
        }, 
        {
            "name": "发送位置123", 
            "type": "location_select", 
            "key": "rselfmenu_2_0"
        },        
        {
            "name": "发送位置123", 
            "type": "location_select", 
            "key": "rselfmenu_2_0"
        },   
    ]
}

# https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN&agentid=AGENTID
	api_url='https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token={}&agentid={}'.format(ACCESS_TOKEN,AgentId)

	response=requests.post(api_url,data=json.dumps(dic))
	print(response.text)
def sendmsg(content):
	ACCESS_TOKEN=get__token(appid,sceret)
	dic={
   "touser" : "11608",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "text",
   "agentid" : 1000012,
   "text" : {
       "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
   },
   "safe":0,
   "enable_id_trans": 0,
   "enable_duplicate_check": 0,
   "duplicate_check_interval": 1800
}
	api_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(ACCESS_TOKEN)
	response=requests.post(api_url,data=json.dumps(dic))
	print(response.text)

def sendmsg_mb():
	ACCESS_TOKEN=get__token(appid,sceret)
	dic={
    "userids" :"11608",

    "agentid" : 1,
    "response_code": "response_code",
    "template_card" : {
        "card_type" : "text_notice",
        "source" : {
            "icon_url": "图片的url",
            "desc": "企业微信",
            "desc_color": 1
        },
        "action_menu": {
            "desc": "卡片副交互辅助文本说明",
            "action_list": [
                {"text": "接受推送", "key": "A"},
                {"text": "不再推送", "key": "B"}
            ]
        },
        "main_title" : {
            "title" : "欢迎使用企业微信",
            "desc" : "您的好友正在邀请您加入企业微信"
        },
        "quote_area": {
            "type": 1,
            "url": "https://work.weixin.qq.com",
            "title": "企业微信的引用样式",
            "quote_text": "企业微信真好用呀真好用"
        },
        "emphasis_content": {
            "title": "100",
            "desc": "核心数据"
        },
        "sub_title_text" : "下载企业微信还能抢红包！",
        "horizontal_content_list" : [
            {
                "keyname": "邀请人",
                "value": "张三"
            },
            {
                "type": 1,
                "keyname": "企业微信官网",
                "value": "点击访问",
                "url": "https://work.weixin.qq.com"
            },
            {
                "type": 2,
                "keyname": "企业微信下载",
                "value": "企业微信.apk",
                "media_id": "文件的media_id"
            },
            {
                "type": 3,
                "keyname": "员工信息",
                "value": "点击查看",
                "userid": "zhangsan"
            }
        ],
        "jump_list" : [
            {
                "type": 1,
                "title": "企业微信官网",
                "url": "https://work.weixin.qq.com"
            },
            {
                "type": 2,
                "title": "跳转小程序",
                "appid": "小程序的appid",
                "pagepath": "/index.html"
            }
        ],
        "card_action": {
            "type": 2,
            "url": "https://work.weixin.qq.com",
            "appid": "小程序的appid",
            "pagepath": "/index.html"
        }
    }
}

	api_url='https://qyapi.weixin.qq.com/cgi-bin/message/update_template_card?access_token={}'.format(ACCESS_TOKEN)
	response=requests.post(api_url,data=json.dumps(dic))
	print(response.text)
	print(json.dumps(dic,indent=3,ensure_ascii=False))



def uploadimg():
	ACCESS_TOKEN=get__token(appid,sceret)
	api_url='https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg?access_token={}'.format(ACCESS_TOKEN)
	files = {'file': open(r'../img/1.png', 'rb')}
	response=requests.post(api_url,files=files)
	print(response.text)

def uploadtemp(type):
	ACCESS_TOKEN=get__token(appid,sceret)
	api_url='https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}'.format(ACCESS_TOKEN,type)
	files = {'file': open(r'D:\\py\\wx_lj.xls', 'rb')}
	response=requests.post(api_url,files=files)
	return json.loads(response.text).get('media_id')

def sendfile():
	ACCESS_TOKEN=get__token(appid,sceret)
	dic={
   "touser" : "11608",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "file",
   "agentid" : 1000012,
   "file" : {
        "media_id" : uploadtemp('file')
   },
   "safe":0,
   "enable_duplicate_check": 0,
   "duplicate_check_interval": 1800
}
	api_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(ACCESS_TOKEN)
	response=requests.post(api_url,data=json.dumps(dic))
	print(response.text)


if __name__ == '__main__':
    sendmsg("aiiw")
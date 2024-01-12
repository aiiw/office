from flask import Flask, make_response,request

import json

import string

import hashlib

import random

import time

import urllib

import redis

import requests
from urllib.parse import  quote,unquote
AppID='25804087'
client_id='MqTM8icss9Th4pZEdMDmDPeRPti90tzK'
client_secret='MCgkTbwnG80LmLH7qGdHdNEc9cQvuQaZ'
Signkey='9eUknSbJqdi^Nma52lw-vUa3$V~O12dt'

#获取授权
# http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id=MqTM8icss9Th4pZEdMDmDPeRPti90tzK&redirect_uri=http://4v5k8a.natappfree.cc/api/01/&scope=basic,netdisk


# def getdevice():
#     client_id='MqTM8icss9Th4pZEdMDmDPeRPti90tzK'
#     client_secret='MCgkTbwnG80LmLH7qGdHdNEc9cQvuQaZ'
#     # url='https://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&code={}&client_id={}&client_secret={}'.format(code,client_id,client_secret)
#     date={'client_id':'MqTM8icss9Th4pZEdMDmDPeRPti90tzK','response_type':'device_code','scope':'basic,netdisk'}
#     url='https://openapi.baidu.com/oauth/2.0/device/code'
#     response=requests.post(url,data=date)
#     print(response.text)#be142e5cf0fd1fdf703e6da4c8e6bea6


# def getaccess():
#     data={'grant_type':'device_token','code':'be142e5cf0fd1fdf703e6da4c8e6bea6','client_id':'MqTM8icss9Th4pZEdMDmDPeRPti90tzK','client_secret':'MCgkTbwnG80LmLH7qGdHdNEc9cQvuQaZ'}
#     url='https://openapi.baidu.com/oauth/2.0/token'
#     response=requests.post(url,data=data)
#     print(response.text)

def getaccess():
    data={'grant_type':'authorization_code','code':'aa5ee384b557e807f0c0c3aa677c9031','client_id':'MqTM8icss9Th4pZEdMDmDPeRPti90tzK','client_secret':'MCgkTbwnG80LmLH7qGdHdNEc9cQvuQaZ','redirect_uri':'http://4v5k8a.natappfree.cc/api/01/'}
    url='https://openapi.baidu.com/oauth/2.0/token'
    response=requests.post(url,data=data)
    print(response.text)
#回调函数地址:http://4v5k8a.natappfree.cc/api/01/?code=0da26e566f06fe8b29d5704bf8b5c3ef
#{"expires_in":2592000,"refresh_token":"122.d9f919c009b7b34f2552580142149047.Y_q0ViC9AP3KibiidLPUKXKbxaP3--js4nzZb-x.Cte_yQ","access_token":"121.e494ee8984c531ac79020535267acec2.Y5smkIIeayV_loeySayVYm4j1p07RCBo-JMj6r8.4oFrIg","session_secret":"","session_key":"","scope":"basic netdisk"}
def getfile(path,access_token):
    url = "https://pan.baidu.com/rest/2.0/xpan/file?method=list&dir={}&order=time&start=0&limit=1000&web=web&folder=0&access_token={}".format(path,access_token)
    payload = {}
    headers = {
    'User-Agent': 'pan.baidu.com'
    }

    response = requests.get(url, headers=headers, data = payload)
    list1=json.loads(response.text)['list']
    list2=[i['path'][1:] for i in list1]
    list3=[i['server_filename'] for i in list1]
    print(list2)
    print(list3)

def searchfile(path,key,access_token):
    url='http://pan.baidu.com/rest/2.0/xpan/file?dir={}&access_token={}&web=1&recursion=1&page=1&num=2&method=search&key={}'.format(path,access_token,key)
    response=requests.get(url)
    list1=json.loads(response.text)['list']
    print(list1)
def getdlink(fsid,access_token):

    url = "http://pan.baidu.com/rest/2.0/xpan/multimedia?access_token={}&method=filemetas&fsids=[{}]&thumb=1&dlink=1&extra=1".format(access_token,fsid)

    payload = {}
    files = {}
    headers = {
    'User-Agent': 'pan.baidu.com'
    }

    response = requests.get(url, headers=headers, data = payload, files = files)
    list1=json.loads(response.text)['list'][0]['dlink']
    print(list1)


if __name__ == '__main__':
    # getdept() #获取指定部门
    #getdept() #将部门写入wx_dept表
    # getaccess()
    access_token="121.e7750e000bb83aeae5ff1bdc7decd8df.Y5q2S5Q8wpvUWd0tBEj5yH9nKaKecO2D5UTzNcT.aGK-UQ"
    # getfile('/学习视频',access_token)
    searchfile('/','d邪',access_token) #这个是做搜索文件
    print("=======================================================================")
    getdlink('1095941852184756',access_token)






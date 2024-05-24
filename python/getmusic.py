#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider_bilibili_v2.py
# @Author: 未衬

# 它可以模拟浏览器向网站发送一个请求[命令]
import requests
from urllib.parse import  quote,unquote
import json
import time
import os
import re

def get_json(url,ss,page):
    # 伪装成浏览器向这个接口拿数据 作用域
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
            'cookie':'UM_distinctid=17309d50a273e3-0368ffaf1509c4-581b3318-1fa400-17309d50a283e2'
    }

    # 分析api这个链接
        # 在api中 会有一些关键字
        # 如果这些关键字改变的话 那它返回的值也是不一样的

    ds = {
         'input':ss,
         'filter':'name',
         'type':'netease',#migu
         'page':page,
    }



    try:
        # 获取api的所有数据
        #html = requests.get(url, params=params, headers=headers)
        bb = requests.post(url, data=ds,headers=headers)
        
        return bb.text
    except BaseException:
        
        return 'error'



def downloader(url, path):
    # 初始化参数 当你在下载视频的时候 0kb开始一直到这个视频的总大小 在下载之前我们要定义这个视频
    # 大小的参数
    size = 0

    # 伪装成浏览器向这个接口拿数据
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'cookie':'UM_distinctid=17309d50a273e3-0368ffaf1509c4-581b3318-1fa400-17309d50a283e2'
    }

    # 取变量名一定见名起意
    response = requests.get(url, headers=headers, stream=True)


    # socket 做下载 IO流 每次下载的数据大小 以1024作为一个节点
    chunk_size = 1024

    #视频总大小 在python中是字典格式
    #print(type(dict(response.headers)))
    header=dict(response.headers)
   
    # for k,v in header.items():
    #     #print(header.get(k))#这样不会报错
    #     print(k+'--------------------',v)
    # for key,itme in header.items():
    #     print(key+'1111111111111',itme)

    if 'Content-Length' in header:
        print('aiiw-------')
        content_size = int(response.headers['content-length'])
       

        if response.status_code == 200:
            print('[文件大小]: %0.2f MB' % (content_size / chunk_size / 1024))
        
            with open(path, 'wb') as file:
            # 迭代响应数据
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    #size += len(data)
    #             #time.sleep( 1 )

# 入口函数
if __name__ == "__main__":
    #songs=['邓丽君','周华健','黄家驹','潭永鳞','邰正宵','张学友','张国荣','任贤齐','林子祥','费玉清','张惠妹','黎明']
    #songer=['aa','bb']
    
    s1 = input("请输入歌手,以逗号隔开：")
    songer=s1.split(',')
    inum=input("请输入页数：一页10条：")
    num=int(inum)
    #num=3
    # songer='王杰'
    # num=5
    print(songer)
    if num<1:
        num=1    
    for song in songer:
        # url = '''https://www.tool22.com/zb_tools/html/MusicTools/?
        # '''
       ul='''https://www.tool22.com/zb_tools/ajax.php?act=MusicTools'''
        # 翻页的值 动态的 11 21 31
        #num = i * 10 + 1

       for i in range(1,num+1):
        
        if str(get_json(ul,song,i)) !='error':
            html = get_json(ul,song,i)
            #print(html)
            text = json.loads(html)
            #print(type(text))
            #print(text['data'])
            #i=0
        
            for kv in text['data']:
            #  print(kv)
               
              # print(kv['title'])
              # print(kv['url'])
               # if kv is None:
                   
               #      continue
               #mtitle=kv['title'].replace('[','')
               sss=re.compile(r'[\[\]\s\(\)\/]')
               stitle=kv['title']
               mtitle=sss.sub('',stitle)
               mymusic=mtitle+'.mp3'
               if not os.path.isfile(mymusic):
                   #i=i+1
                   print(mymusic,kv['url'])
                   downloader(kv['url'],mymusic)
                   #downloader(ul,mymusic)
               #print(kv)

        else:
            print('aiiw')
    input("Press <enter>")




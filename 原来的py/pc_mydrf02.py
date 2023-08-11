# -*- coding: utf-8 -*-
import requests

url = 'http://127.0.0.1:9000/api/books/'
headers = {'Authorization': 'Token 89ed43be846c72e393877b7a044dd263de9f5fe2'}

response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == requests.codes.ok:
    # 处理响应数据
    data = response.json()
    print(data)
else:
    print('请求失败，状态码为：', response.status_code)


# url = 'http://127.0.0.1:9000/api/sync'
# headers = {'Authorization': 'Token 89ed43be846c72e393877b7a044dd263de9f5fe2'}

# response = requests.get(url, headers=headers)

# # 检查响应状态码
# if response.status_code == requests.codes.ok:
#     # 处理响应数据
#     data = response.text
#     print(data)
# else:
#     print('请求失败，状态码为：', response.status_code)

# [{"id":1,"genre":"小说","title":"红http://127.0.0.1:9000/setusers/users/?username__contains=6楼梦","author":"曹雪芹","description":"一部中国古典小说","publish_date":"1791-01-01"},{"id":2,"genre":"小说","title":"西游记","author":"吴承恩","description":"一部神话小说","publish_date":"1592-01-01"},{"id":3,"genre":"小说","title":"水浒传","author":"施耐庵","description":"一部英雄志小说","publish_date":"1368-01-01"},{"id":4,"genre":"历史","title":"资治通鉴","author":"司马光","description":"一部历史著作","publish_date":"1084-01-01"},{"id":5,"genre":"历史","title":"明朝那些事儿","author":"当年明月","description":"描述明朝历史事件的书籍","publish_date":"2006-08-01"},{"id":6,"genre":"传记","title":"毛泽东传","author":"斯诺","description":"详细介绍毛泽东生平的传记","publish_date":"1960-01-01"},{"id":7,"genre":"传记","title":"乔布斯传","author":"沃尔特·艾萨克森","description":"描写苹果公司创始人乔布斯生平的传记","publish_date":"2011-10-24"},{"id":8,"genre":"小说","title":"福尔摩斯探案集","author":"阿瑟·柯南道尔","description":"一部侦探小说集","publish_date":"1892-01-01"},{"id":9,"genre":"惊悚","title":"1984","author":"乔治·奥威尔","description":"一部反乌托邦小说","publish_date":"1949-06-08"},{"id":10,"genre":"惊悚","title":"尘埃落定","author":"余华","description":"描写人性的惊悚小说","publish_date":"2018-02-01"},{"id":11,"genre":"历史","title":"大话西游","author":"周星星","description":"讲述周星星的日子","publish_date":"2023-04-23"},{"id":12,"genre":"历史","title":"大话西游","author":"周星星","description":"讲述周星星的日子","publish_date":"2023-04-23"},{"id":13,"genre":"小说","title":"大话西游","author":"周星星","description":"122","publish_date":"2023-04-22"}]

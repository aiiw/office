import json

data = {
    'name' : '简',
    'sex' : 'boy',
    'age' : 26
}
print("-----------------原始-----------------------")
print(data,type(data)) 
data1=json.dumps(data)
print(data1,type(data1)) #总结 字典对象使用 dumps 转为字符串  字符串使用 loads 装载为 字典
# print("-----------------dumps-----------------------")
# print(data1,type(data1))
# data2=json.loads(data1)
# print("-----------------loads-----------------------")
# print(data2,type(data2))
# print(type(data))#输出原始数据格式
# print(type(data1))#输出经过json.dumps的数据格式
# print(type(data2))#输出经过json.loads的数据格式
# for index,qq in enumerate(data):
# 	print(index)
#response2=json.dumps(response1,indent=3,sort_keys=True,ensure_ascii=False) 这个是格式化显示 
# import requests
# import json


# def main():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
#     data_model = json.loads(resp.text)
#     print(resp)
#     for news in data_model:
#         print(news)


# if __name__ == '__main__':
#     main()
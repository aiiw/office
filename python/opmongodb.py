# Requires pymongo 3.6.0+
from pymongo import MongoClient
#1 查询集数据  类似select
client = MongoClient("mongodb://localhost:27017/")
database = client["aiiw"] #client 指向数据库
collection = database["weixin_user"] # database 指向表,即数据集合

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}


cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
print("*"*180)
#2判断集全是否存在这个数据库
client = MongoClient("mongodb://localhost:27017/")
mydb = client['aiiw']
 
collist = mydb. list_collection_names()
print(collist)
# collist = mydb.collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
  print("集合已存在！")
else:
	mycol = mydb["sites"]
	client.close()
print("*"*180)
#3 插入集合
client = MongoClient("mongodb://localhost:27017/")
mydb = client["aiiw"] #client 指向数据库
mycol = mydb["sites1"] # 注意这个地方,这个表是可以直接指定,不需要提前创建
 
mydict = { "name": "Google", "alexa": "1", "url": "https://www.google.com" }
 
x = mycol.insert_one(mydict)
client.close()

#4 批量插入集合
print("4 批量插入集合")
client = MongoClient("mongodb://localhost:27017/")
mydb = client["aiiw"] #client 指向数据库
mycol = mydb["sites2"] # 注意这个地方,这个表是可以直接指定,不需要提前创建
 
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
 
 
x = mycol.insert_many(mylist)
print(x)
client.close()


# #4 批量插入集合
# client = MongoClient("mongodb://localhost:27017/")
# mydb = client["aiiw"] #client 指向数据库
# mycol = mydb["sites2"] # 注意这个地方,这个表是可以直接指定,不需要提前创建
 
# mylist = [
#   { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程11"}, #指定的ID不能存在
#   { "_id": 2, "name": "Google", "address": "Google 搜索1"},
#   { "_id": 3, "name": "Facebook", "address": "脸书1"},
#   { "_id": 4, "name": "Taobao", "address": "淘宝1"},
#   { "_id": 5, "name": "Zhihu", "address": "知乎1"}
# ]
 
 
# x = mycol.insert_many(mylist)
# print(x)
# client.close()

#5修改
client = MongoClient("mongodb://localhost:27017/")
mydb = client["aiiw"]
mycol = mydb["sites2"]
 
myquery = { "name": "QQ" }
newvalues = { "$set": { "name": "QQ123" } }
 
mycol.update_many(myquery, newvalues) #update_one() 方法只能修匹配到的第一条记录，如果要修改所有匹配到的记录，可以使用 update_many()。
 
# 输出修改后的  "sites"  集合
for x in mycol.find():
  print("for x in :",x)
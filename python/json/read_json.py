import json
# with open('test.json','r',encoding='UTF-8') as j:
# 	print(j.readlines())

#将文件中的内容直接读取为字典
with open('test1.json','r') as j:
	b=json.load(j)
print(b)
print(type(b))

#将字典直接写入为文件内容
dic={'a':123,'b':321}
with open('rjson.json','a') as fp:
	a=json.dump(dic,fp,sort_keys=True,indent=5,ensure_ascii=False)


#
with open('morejson.json','r') as myfile:
	data=json.load(myfile)
	print(data)

with open('163.json','r') as fp:
	data=json.load(fp)
	print(data)
	zdata=json.dumps(data,sort_keys=True,indent=5,ensure_ascii=False)
	print(zdata)

with open('post.json','r') as fp:
	data=json.load(fp)
	# print(data)
	# zdata=json.dumps(data,sort_keys=True,indent=5,ensure_ascii=False)
	# print(zdata)
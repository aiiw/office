
# list = [i for i in range(1,100,6)]
# # data=random.choice(list)
# # print(data)

# # list2=[[{"1"}]]
# # print(list2[0][0])


# str1='[{"id":1,"text":"text1"},{"id":2,"text":"text2"},{"id":3,"text":"text3","selected":"true"},{"id":4,"text":"text4"},{"id":5,"text":"text5"}]'
# # print(type(str1))
# # print(str1)

# print(type(eval(str1)))

# str2=str1.split('},{')
# print(type(str2))
# print(str2)
# # s='["a","b","c"]'
# # print(eval(s))
# import json
# with open('f.json') as j:
# 	data=json.load(j)
# print(type(data))
# ck=[]
# for item in data:
# 	ck.append(item.get("id"))
# 	print(item)
# print(ck)
# d={'id':3,'text':'123'}
# l={'id':'1','text':'2'}
# for i in range(1,100):
# 	l['id']=i
# 	l['text']="aiiw" +str(i)
# 	if i not in ck:
# 		data.append(l)

import arrow,os,json

d=arrow.now().format('YYYY-MM-DD HH:mm:ss')
logmark = str(d)+"sussessful"+"\n"

with open('f.json','w+') as k:
	json.dump(d, k)


export ORACLE_BASE=/db/oracle

export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/db_1 

export ORACLE_SID=orcl 

export ORACLE_TERM=xterm 

export PATH=$ORACLE_HOME/bin:$PATH 

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib 

export LANG=C

export NLS_LANG=AMERICAN_AMERICA.ZHS16GBK
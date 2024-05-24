import os
import requests,json
from urllib.parse import  quote,unquote
from urllib import request
from remonth import remonths
a=input("请输入年份：　")
b=input("请输入月份：　")
ab=remonths(a,b)
session = requests.Session()

ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
header  =  {"User-Agent"  : ua,
            "Referer" :  "http://192.168.0.181:8090/eHR/PSN01/Index",
            "Cookie":r"rffbvm0zaiariab5dak3idcd; __RequestVerificationToken=I8KeFtydQWIruk8yP2iBrLGV1g5XojuehemWpTlYlg-HAzLHWKl1K8K9_kA54lcLXjmUE3nbk-sIC9V-ASFI2sQEsa-PDH_cJBHM_1dU72_u6X0vTb3A4SGiXTbxWPt4GJRFrNz5lUb-rxg_povOew2; uid=id=1&usercode=admin&username=%e7%b3%bb%e7%bb%9f%e7%ae%a1%e7%90%86%e5%91%98&login=admin&usertype=9&isadmin=True&customcode=&suppliercode="
            }

filter1="a.id is not null and ISNULL(DimissionDate,'9999-12-31')>='%s' AND  HireDate<='%s'"%ab
form_data = {
      "AppCode":"PSN01",
      "InterCode":"Mst",
      "Filter": filter1,
      "search": "false",
      "nd":"",
      "rows":"3000",
      "page":"1",
      "sortColName":"fullcode,Code",
      "sortDirection":"asc",
     
}



i2 = session.post('http://192.168.0.181:8088/Api/PSN01Api/GetMst', headers = header,data=form_data)
# i2 = session.post('http://192.168.0.181:8090/Api/PSN01Api/GetMst', headers = header,)
c2 = i2.cookies.get_dict()
strdoc=i2.text
bdoc=i2.content
# print(bdoc.decode('utf-8','ignore'))
if os.path.exists('lagou.txt'):
	os.remove('lagou.txt')
with open('lagou.txt', 'a+',encoding='utf-8') as f:
	f.writelines(strdoc)

with open('lagou.txt', 'r',encoding='utf-8') as f1:
	str=f1.readlines()


# du=json.dumps(str)
# print(du)
keys=json.loads(str[0]).get('griddata')
vl=[]
dif=keys[0]
for gd1,gd2 in dif.items():
	print(gd1,"--")
chose=input("请输入需要增加的列内容，默认不输入为code,name:  ")
lchose=chose.split(',')

for d1 in keys:


	v={}
	for b1,b2 in d1.items():
		if b1=="Code" or b1=="Name" or b1 in lchose:
			v[b1]=b2
	vl.append(v)


keys=vl
# print(key[0])
list=[]
item=[]
n=0


for field,value in keys[0].items():
	item.append(field)
list.append(item)
for a in keys:
	item=[]
	for i,j in a.items():
		item.append(j)
	list.append(item)
import xlwings as xw
app=xw.App(visible=False,add_book=False)
book=app.books.add()
sheet=book.sheets['sheet1']
sheet.range('a1').value=list
book.save('hrm.xlsx')
book.close()
app.quit()
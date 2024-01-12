import pytesseract
from PIL import Image
import PIL.ImageOps
import os
import requests,json
from urllib.parse import  quote,unquote
import connector
import time
import json
from urllib import request
session = requests.Session()

def convert_img(img, threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img


def initTable(threshold=60):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table
def getverify(path):
	for root,dir,file in os.walk(path):
		for tt in  file:
			dd=os.path.join(os.path.abspath(root),tt)
			im = Image.open(dd)
	#图片的处理过程
			im = im.convert('L')
			binaryImage = im.point(initTable(), '1')
			im1 = binaryImage.convert('L')
			im2 = PIL.ImageOps.invert(im1)
			im3 = im2.convert('1')
			im4 = im3.convert('L')
			#将图片中字符裁剪保留
			box = (3,2,46,22) 
			region = im4.crop(box)  
			#将图片字符放大
			out = region.resize((120,55)) 
			return pytesseract.image_to_string(out)

def get_and_save_verify(url1,i):
    try:
        url = url1
        request.urlretrieve(url,'img\\'+str(i) + '.png')
        print('第' + str(i) + '张图片下载成功')
    except Exception:
        print('第' + str(i) + '张图片下载失败')


from urllib.parse import  quote,unquote
from urllib.parse import  quote,unquote
from bs4 import BeautifulSoup

# i1=session.get('http://192.168.0.181:8090/Authentication/Login')
# html_doc=i1.text
# soup = BeautifulSoup(html_doc, 'html.parser')
# purl=soup.find(id='validateCode1_imgValidateCode').attrs['src']
# vurl="http://192.168.0.181:8090/"+purl

# # get_and_save_verify(vurl,1)
# # vd=getverify('img')                                                                                                      
# # print(vd)
# print(vurl)
ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
header  =  {"User-Agent"  : ua,
            "Referer" :  "http://192.168.0.181:8090/eHR/PSN01/Index",
            "Cookie":r"ASP.NET_SessionId=rffbvm0zaiariab5dak3idcd; __RequestVerificationToken=I8KeFtydQWIruk8yP2iBrLGV1g5XojuehemWpTlYlg-HAzLHWKl1K8K9_kA54lcLXjmUE3nbk-sIC9V-ASFI2sQEsa-PDH_cJBHM_1dU72_u6X0vTb3A4SGiXTbxWPt4GJRFrNz5lUb-rxg_povOew2; uid=id=1&usercode=admin&username=%e7%b3%bb%e7%bb%9f%e7%ae%a1%e7%90%86%e5%91%98&login=admin&usertype=9&isadmin=True&customcode=&suppliercode="
            }
form_data = {
      "AppCode":"PSN01",
      "InterCode":"Mst",
      "Filter": "a.id is not null and ISNULL(DimissionDate,'9999-12-31')>='2021-01-01' AND  HireDate<='2021-01-31' and  Code is not null",
      "search": "false",
      "nd":"",
      "rows":"3000",
      "page":"1",
      "sortColName":"fullcode,Code",
      "sortDirection":"asc",
     
}



i2 = session.post('http://192.168.0.181:8090/Api/PSN01Api/GetMst', headers = header,data=form_data)
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
book.save('77.xlsx')
book.close()
app.quit()
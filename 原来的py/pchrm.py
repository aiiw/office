import pytesseract
from PIL import Image
import PIL.ImageOps
import os
import requests,json
from urllib.parse import  quote,unquote
import connector
import time
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

i1=session.get('http://192.168.0.181:8090/Authentication/Login')
html_doc=i1.text
soup = BeautifulSoup(html_doc, 'html.parser')
purl=soup.find(id='validateCode1_imgValidateCode').attrs['src']
vurl="http://192.168.0.181:8090/"+purl

# get_and_save_verify(vurl,1)
# vd=getverify('img')
# print(vd)
print(vurl)
ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
header  =  {"User-Agent"  : ua,
            "Referer" :  "http://192.168.0.181:8090/Authentication/Login",
            "Cookie":r"ASP.NET_SessionId=rffbvm0zaiariab5dak3idcd; uid=id=1&usercode=admin&username=%e7%b3%bb%e7%bb%9f%e7%ae%a1%e7%90%86%e5%91%98&login=admin&usertype=9&isadmin=True&customcode=&suppliercode="
            }
form_data = {
      "ReturnUrl":"ww.dd.cc",
      "ValidateCodeID":"ValidateCode1",
      "Login": "admin",
      "Password": "txcallme",
      "ValidateCode":2750,
      "RememberMe":0
     
}



i2 = session.post('http://192.168.0.181:8090/Authentication/Validate', headers = header,data=form_data)
c2 = i2.cookies.get_dict()
print (i2.content.decode('utf-8'))

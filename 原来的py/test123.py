
import urllib2 
from bs4 import BeautifulSoup
import json
import sys 
#sys系统编码为ascii 通过下面两行代码更改默认编码
reload(sys)

resultData = []#用来存放每次抓取的信息
#http:#www.snnu.edu.cn/tzgg/217.htm
#urllib2 抓取网页
url = 'http://www.snnu.edu.cn/tzgg/'
count =1
for i in range(1, 219):
num = 219 - i
url_com = url + str(num) + “.htm”#循环组成所有目标url
response = urllib2.urlopen(url_com)
print response
#charset = chardet.detect(url)
#print charset #获取目标网页的编码方式
#print response.getcode() #检测是否抓取成功输出200
#cont = response.read().decode(‘utf-8’) 读出获得的网页
# BeautifulSoup 解析网页
soup = BeautifulSoup(response, ‘html.parser’)
link = soup.find_all(class_=“con_newslist”)[0] #寻找目标特征
links = link.find_all(“li”)
for li in links:
data = {
“title” : li.find(“a”).text
}
print count
count = count + 1
resultData.append(data)#将每次循环获取的数据写入数组
with open(‘result.json’, ‘wb’) as f:#将数组写入相同目录resylt.json中 wb表示可读取 可写入
f.write(json.dumps(resultData).decode(“unicode-escape”))、、写入的这行代码跟开头sys配套更改最后写入编码

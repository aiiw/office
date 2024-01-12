import requests
from urllib.parse import  quote,unquote
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
r = requests.get( r'https://www.zaobao.com/realtime/china', headers=headers )
# print( unquote(r.content.decode( 'utf-8' )) )
html_doc=unquote(r.content.decode( 'utf-8' ))
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)
ls = soup.find_all(class_ = 'f18 m-eps')  #这个地方class要加_由于class是Python的保留关键字，为了避免与之冲突，BeautifulSoup内部将class属性改名为class_
for item in ls:
	print(item.text)
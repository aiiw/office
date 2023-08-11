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
ls = soup.find_all(class_ = 'f18 m-eps')  #这个地方class要加_
for item in ls:
	print(item.text)
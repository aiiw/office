#coding:gbk
import sys,json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  # [ 这个用来 解决 乱码]
print('\ufffd')
'\ufffd'.encode("utf-8", 'ignore').decode("utf-8")
# '\ufffd'.encode("GBK").decode #这个会报错
# print(sys.getdefaultencoding())
a="中"
s="中"
s1 = s.encode('unicode_escape')
print("unicode_escape",s1)
a1=a.encode()
print("默认",a1)
a2=a.encode('utf-8')
print("utf-8",a2)
a3=a.encode('gbk')
print("gbk",a3)
# temp5=json.dumps(temp2,sort_keys=True,indent=5,ensure_ascii=False)
# s1 = {'TO_UID':'1','TO_NAME':'','TD_HTML_EDITOR_CONTENT':a1,'I_VER':'2','C':'web','ACTION_TYPE':'sms'}
# # encode 卤脿脗毛拢卢脠莽潞脦陆芦str --> bytes, ()
# # s11=json.dumps(s1)
# # s12 = s11.encode('utf-8')
# # print(s12)
# # s12 = s11.encode('gbk')
# # print(s12)
# print(s1,type(a1))

# # s2='脛茫脫脨脪禄脤玫脨脗碌脛脨脜脧垄,脟毛脳垄脪芒虏茅脢脮'
# # print(s2.encode('utf-8'))
# # print(s2.encode('gbk'))
from urllib.parse import  quote,unquote
from bs4 import BeautifulSoup
import re
html_doc='''
error during connect: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.37/containers/json: open //./pipe/docker_engine: The system cannot find the file specified. In the default daemon configuration on Windows, the docker client must be run elevated to connect. This error may also indicate that the docker daemon is not running.
'''

print(unquote(html_doc)) #quote url编码 unquote url解码
# html_doc1=html_doc.encode().decode()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.select('span'))
b='中国人'
print('中国人unicode:',b.encode('unicode_escape'),"decode:",b.encode('unicode_escape').decode('unicode_escape'))
print('中国人utf-8   ',b.encode('utf-8'))
print('中国人gbk   ',b.encode('gbk'))
print('中国人gbk  ',b.encode('gbk').decode('gbk').encode('gbk'))

# u=b.encode('unicode_escape')
# print(u.encode())
print("=======================================================")
kk='\\u4e2d\\u56fd\\u4eba'
print(kk)
print(kk.encode())
print(kk.encode('utf-8').decode('unicode_escape'))
o=hex(ord("方"))
print("方",o)  #这里证明了从文件读到内存里的编码为unicode,其实按我理解，不用关注unicode,这个是中间码，
# 这个文件的编码为ansi,即采用ＧＢＫ的，可以要求声明也要用ＧＢＫ标明，标明后python解释器会使用ＧＢＫ进行
# 编码自动转换，即：在文件中的使用ＧＢＫ读取"方"为：Ｂ７ＢＤ，实际在本文的查编码已经是unicode："65Ｂ9"
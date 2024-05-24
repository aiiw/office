html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p name="dd" class="title"><b>标签中的内容The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://exam1le.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story1" style="color:red">...storystorystorystorystorystory</p>
"""
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())#整个DOM 加上prettify 格式化
#以标签形式
print("以标签形式%s",soup.p)#以标签形式，对于Tag，它有两个重要的属性，是name和attrs
print("以标签形式+names:%s"%(soup.p.name),soup.p.name)  #""%())
print("以标签形式+attrs%s",soup.p.attrs)
#----以内容形式
print("以内容形式")
print("以标签形式+显示内容::::::::%s",soup.p.string)
# # #二遍历
# # #1.直接子节点：.contents .children 属性 返回第一个标签的子节点，以列表形式
# print("以遍历contents形式%s",soup.p.contents)
# #2 如上的效果一样，通过children实现
# for child in  soup.p.children:
#     print("以遍历children形式%s",child)
# for child1 in soup.p.descendants:
#     print ("以遍历descendants形式,可以遍历所有子节点%s",child1,"遍历也是只能对第一个符合要求的进行遍历子节点")

# #find_all 查找所有标签，如上是查找第一个满足要求的标签
print("find_all 查找所有标签，如上是查找第一个满足要求的标签")
# #a 字符串方式
print(soup.find_all('p'))#标签内含有p
#b 正则表达式
# print('以正则查找所有b开头的标签',soup.find_all(re.compile(r'^p')))
# #c 传列表
# print('以列表形式',soup.find_all(['p1','Elsie']))

# # #查找文本内容
# print('查找文本内容',soup.find_all(text="Elsie"))#内容也可以按列表查找的

# # #通过css选择器 all_tertiaryconsumers = soup.find_all(class_ = 'tertiaryconsumerslist') 

# #通过标签名
print("通过标签名")
#find_all(name, attrs, recursive, text, limit, **kwargs)
li_quick = soup.find_all(attrs={'class':'story1'})
print(li_quick[0].name)
print(li_quick[0].attrs)
print(li_quick[0].string)
print (soup.select('a') )

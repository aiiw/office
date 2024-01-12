import re
'''
match 方法：从起始位置开始查找，一次匹配
search 方法：从任何位置开始查找，一次匹配
findall 方法：全部匹配，返回列表
finditer 方法：全部匹配，返回迭代器
split 方法：分割字符串，返回列表
sub 方法：替换'''

pattern = re.compile(r'\d+')
m = pattern.match('123one12twothree34four')# 查找头部，没有匹配
print (m)
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print (m)

pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m1 = pattern1.match('Hello World Wide Web')
print (m1.group(0)) # 返回匹配成功的整个子串

pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
print('-------------search------------------')
m1 = pattern1.search('Hello World Wide Web')
print (m1)

#search 一次匹配
pattern = re.compile(r'\d+')
m = pattern.search('hello 123456 789')
if m:
    # 使用 Match 获得分组信息
    print ('matching string:%s',m.group())
    # 起始位置和结束位置
    print ('position:%d',m.span())
print("----findall------")
#findall 全部匹配 返回列表
pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m1 = pattern1.findall('Hello World Wide Web')
print(m1)
for item in m1:
 print(item)
print("----------")
#split 方法按照能够匹配的子串将字符串分割后返回列表
p = re.compile(r'[\s\,\;]+')
print (p.split('a,b;; c   d'))

#sub 方法用于替换
print("----------")
p = re.compile(r'(\w+) (\w+)') # \w = [A-Za-z0-9_]
s = 'hello 123, hello 456'
print (p.sub(r'hello world', s))  #P为匹配的规则,,,,两上参数，第一个是需要替换的字符，第二个是源(被替换)使用 'hello world' 替换 'hello 123' 和 'hello 456'  

ss=' OU=设备管理科 ,  OU=SBB设备部 ,  OU=Mastergroup ,dc=mastercn,dc=local'
p=re.compile(r'\s')
s1=p.sub('',ss)
print(s1)
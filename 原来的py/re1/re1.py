import re
'''
match 方法：从起始位置开始查找，一次匹配
search 方法：从任何位置开始查找，一次匹配
findall 方法：全部匹配，返回列表
finditer 方法：全部匹配，返回迭代器
split 方法：分割字符串，返回列表
sub 方法：替换'''
#p这是通过模式实例化
# pattern = re.compile(r'\d+')
# m = pattern.match('1one12twothree34four')# 查找头部，没有匹配
# print (m)

# #使用原始的
# vv='1one12twothree34four'
# re.match(vv,r'\d+')
# print (m)

# m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
# print (m)

# pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
# m1 = pattern1.match('Hello World Wide Web')
# print (m1.group(0)) # 返回匹配成功的整个子串

# pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
# m1 = pattern1.search('Hello World Wide Web')
# print (m1)

# #search 一次匹配
# pattern = re.compile(r'\d+')
# m = pattern.search('hello 123456 789')
# if m:
#     # 使用 Match 获得分组信息
#     print ('matching string:%s',m.group())
#     # 起始位置和结束位置
#     print ('position:%d',m.span())

# #findall 全部匹配 返回列表
# pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
# m1 = pattern1.findall('Hello World Wide Web')
# for item in m1:
#  print(item)

# #split 方法按照能够匹配的子串将字符串分割后返回列表
# p = re.compile(r'[\s\,\;]+')
# print (p.split('a,b;; c   d'))

# #sub 方法用于替换
# p = re.compile(r'(\w+) (\w+)') # \w = [A-Za-z0-9_]
# s = 'hello 123, hello 456'
# print (p.sub(r'hello world', s))  #两上参数，第一个是需要替换的字符，第二个是源 使用 'hello world' 替换 'hello 123' 和 'hello 456'

# p=re.compile(r'[\u4e00-\u9fa5]')
# s='MMF-809 B/1.6mm纤维板/94V0/单按键,红/蓝灯,带线长80mm,热缩管长60mm'
# print(p.findall(s))
#数据处理 
# sss=re.compile(r'o+')
# sss1='''Touch Medley: Water of Love /独家试唱/星秀传说/ 信者得爱(feat. MC仁) [Live].mp3'''
# print(sss1)
# print(re.sub(r'[\[\]\s\(\)\/]',"－",sss1))

sss=re.compile(r'[\[\]\s\(\)\/家]')
sss1='''Touch Medley: Water of Love /独家试唱/星秀传说/ 信者得爱(feat. MC仁) [Live].mp3'''
print(sss1)
print(sss.sub('@',sss1)) #要替换的值  源字段

vy='123A168.0.254 1232132 192.168.0.253  544543'
p1=re.compile(r'\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}')
print(p1.findall(vy))
print(vy)
print(p1.sub('##',vy))

vy='''SELECT DISTINCT < field > pmdsdocno,
                pmdsdocdt,
                pmds002,
                ooag011,
                pmds003,
                ooefl003,
                pmds008,
                pmaal004 < / field >
  FROM < table > pmds_t
  LEFT OUTER JOIN ooag_t
    ON ooagent = pmdsent
   AND ooag001 = pmds002
  LEFT OUTER JOIN ooefl_t
    ON ooeflent = pmdsent
   AND ooefl001 = pmds003
   AND ooefl002 = :DLANG
  LEFT OUTER JOIN pmaal_t
    ON pmdsent = pmaalent
   AND (pmds008 = pmaal001)
   AND pmaal002 = :DLANG, pmdt_t < / table >
 WHERE < wc > pmdsent = pmdtent
    AND pmdsdocno = pmdtdocno
    AND pmdsent = :ENT
    AND pmds000 IN arg1 < / wc > < inwc >
    AND (pmdsstus = 'Y' OR pmdsstus = 'S') < / inwc >
 ORDER BY pmdsdocno
'''

p1=re.compile(r'\<[a-z A-Z \/]+\>')
vy1=p1.sub('', vy)
p2=re.compile(r'(= :DLANG)|(= :ENT)|(= :SITE)')
print(p2.sub("is not null", vy1))


sql='''
SELECT SUM(sfac003-COALESCE(sfac005,0)),sfaa013,sfaa005 FROM ",              
               " (SELECT sfaaent,sfaa019,(COALESCE(sfac003,0)-COALESCE(sfac005,0)) sfaa012,",
               "         sfac001,sfac006,sfaadocno,sfaa017,sfaa006,sfaa002,sfaa013,sfaa010,sfaa003,sfaa005,sfaa021,sfaa022 FROM sfaa_t ",   
                " LEFT JOIN ", 
                "(SELECT sfac001,sfac006,sfacent,sfacdocno,COALESCE(sfac003,0) sfac003,COALESCE(sfac005,0) sfac005 FROM sfac_t WHERE sfacent='",g_enterprise,"' AND sfacsite='",g_site,"' AND (COALESCE(sfac003,0)-COALESCE(sfac005,0)) <> 0)", 
                " ON sfacdocno=sfaadocno AND sfaaent=sfacent",
               " WHERE sfaaent = ",g_enterprise,
               "   AND sfaasite = '",g_site,"'",
               "   AND sfac001 = '",g_imaa_d[l_ac].imaa001,"'",  
               "   AND sfaa003 <> '4' ",
               "   AND sfaastus <> 'X'",
               "   AND sfaastus <> 'C'",
               "   AND sfaastus <> 'M'",
               "   AND sfaa057 = '1' ",
               "    AND (COALESCE(sfac003,0)-COALESCE(sfac005,0)) <> 0) T1",   
               " LEFT OUTER JOIN ",
               "(SELECT sfac001,sfac006,sfacdocno,COALESCE(sfac003,0) sfac003,COALESCE(sfac005,0) sfac005 FROM sfac_t WHERE sfacent='",g_enterprise,"' AND sfacsite='",g_site,"' AND (COALESCE(sfac003,0)-COALESCE(sfac005,0)) <> 0) T2", 
               " ON T1.sfaadocno=T2.sfacdocno "
               ," AND T1.sfac001 = T2.sfac001 AND T1.sfac006 = T2.sfac006 ",   
               " GROUP BY sfaa019,sfaadocno,sfaa017,sfaa005,sfaa002,sfaa003,sfaa013,sfaa010,sfaa022,sfaa021,sfaa006 ", 
               " ORDER BY sfaa019,sfaadocno,sfaa017,sfaa005,sfaa002,sfaa003,sfaa013,sfaa010,sfaa022,sfaa021,sfaa006 
                   "    AND COALESCE(sfba017,0) = 0 
'''
pv=re.compile(r'(",)|(")')
print(pv.sub("", sql))
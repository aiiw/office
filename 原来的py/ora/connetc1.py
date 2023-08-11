import cx_Oracle 
connection = cx_Oracle.Connection("dsdata/dsdata@T100")
cr=connection.cursor();
sql='''select  y.imaal003
  from tama t
  left join imaa_t x
    on t.imaa001 = x.imaa035
   and x.imaaent = '100'
   and x.imaastus = 'Y'
   And x.imaa010 = 2
  left join imaal_t y
    on y.imaal001 = x.imaa001 and y.imaalent = '100'
   and y.imaal002 = :ab 
'''
cr.execute(sql,ab='zh_CN')
rs=cr.fetchone();
print (rs)
# #print (str(rs))
# #--------------------------------
# import re
# p=re.compile(r'[\u4e00-\u9fa5]')
# import xlwt 
# book=xlwt.Workbook()
# #sheet1=book.add_sheet('sheet1')
# sheet2=book.add_sheet('sheet2')
# n=-1
# y=-1
# n1=-1
# title=['a','b','c','d']
# for tt in title:
#   n = n + 1
#   sheet2.write(0,n,title[n])

# for row in rs:
#  if row[0] is not None:#要求要查询的值不为空
#     n = n + 1
#     t = p.findall( str( row ) )
#     s = ''
#     for t1 in t:
#       s = s + '%' + t1 + '%'
#     sql1 = '''select y.imaal001,y.imaal003,y.imaal004 from imaa_t x left join imaal_t y on y.imaal001 = x.imaa001 and y.imaalent = '100'
#           where y.imaal003 like :bc
#          '''
#     #print(s)
#     cr.execute( sql1, bc=s )
#     rs1 = cr.fetchall()
#     #print(n)

#     for row1 in rs1:
#       y = y + 1
#      #if row1 == '':
#       # print(y)
#       # print(str(row1))
#       c1=len(row1)-1
#       c2=len(row1)

#       for i in range(0,c2):
#         sheet2.write( y+1, i, row1[i]) 
        
#         print(c1)
#       sheet2.write( y+1, c1+1, s )
# book.save('1.xls')


# #-------------------------------------------------------
#sheet2.write(y,0,'a')
#sheet2.write(y,0,str(row1))


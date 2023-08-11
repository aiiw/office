import cx_Oracle 
connection = cx_Oracle.Connection("dsdata/dsdata@T100")
cr=connection.cursor();
# sql='''select  y.imaal003
#   from tama t
#   left join imaa_t x
#     on t.imaa001 = x.imaa035
#    and x.imaaent = '100'
#    and x.imaastus = 'Y'
#    And x.imaa010 = 2
#   left join imaal_t y
#     on y.imaal001 = x.imaa001 and y.imaalent = '100'
#    and y.imaal002 = :ab 
# '''
# cr.execute(sql,ab='zh_CN')

# sql='''select a from dual '''
# cr.execute(sql,a='sfaastus',b='sfaa_t')

sql0='select distinct '
f=input('请输入字段')
sql1=' from '
table=input('请输入表')
sql2=sql0+f+sql1+table
print(sql2)

cr.execute(sql2)
rs=cr.fetchall();
print(rs)



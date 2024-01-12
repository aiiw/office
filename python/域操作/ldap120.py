from ldap3 import Server, Connection, ALL, NTLM
import json

# 连接标准的属性在LDAP规范中定义，如 cn 表示通用名称，ou 表示组织单位，dc 表示域名组件等。自定义属性则由LDAP服务器管理员根据需要进行定义。
#在这个例子中，OU 和 ou 是不同的属性名。通常情况下，标准LDAP属性名是全小写的，而自定义属性名则可以使用任何大小写组合
server = Server('192.168.0.120', get_info=ALL)
conn = Connection(server, user='mastercn\\Dnk', password='M2925090', auto_bind=True, authentication=NTLM)
# print(server.info)

# 查询
# res = conn.search('dc=mastercn,dc=local', search_filter ='(sAMAccountName=11580)', attributes=['*'])
#res = conn.search('dc=mastercn,dc=local', search_filter ='(objectClass=person)', attributes=['*'],size_limit=150)
#res = conn.search('dc=mastercn,dc=local', search_filter ='(objectClass=person)', attributes=['*'],size_limit=25000, get_operational_attributes=True)
res = conn.search('dc=mastercn,dc=local', search_filter ='(&(objectCategory=organizationalUnit)(ou=Employee))', attributes=['*'],size_limit=25000, get_operational_attributes=True)
#OU=RLB人资部 ,  OU=HR人力资源中心
res = conn.search('OU=电器质检科,OU=JDB电器公司,OU=Mastergroup,dc=mastercn,dc=local',search_filter ='(objectClass=person)', attributes=['*'],size_limit=25000, get_operational_attributes=True)

print(conn.result)  # 查询失败的原因
print(type(conn.entries))  # 查询到的数据
n=len(conn.entries)
print(n)
list=[]
for a in range(0,n):
    result=conn.entries[a].entry_to_json()
    print(json.dumps(json.loads(result),sort_keys=True,indent=5,ensure_ascii=False))
    memberOf=json.loads(result)['attributes'].get('memberOf','为空')

    if not memberOf:
        memberOf=[]
    name=json.loads(result)['attributes'].get('name')
    userAccountControl=json.loads(result)['attributes'].get('userAccountControl','userAccountControl')
    userPrincipalName=json.loads(result)['attributes'].get('userPrincipalName', 'userPrincipalName')
    str1=json.dumps(memberOf,sort_keys=True,indent=5,ensure_ascii=False)
    # print(name+memberOf+userAccountControl,userPrincipalName)  # 查询到的数据
    m=len(memberOf)
    for b in memberOf:
        list0=[]
        # print(name,b,userAccountControl,userPrincipalName)
        list0.append(name[0])
        list0.append(b)
        list0.append(userAccountControl[0])
        list0.append(userPrincipalName[0])
    list.append(list0)
conn.unbind()
print(list0)
#attributes{givenName  姓  sn名 cn:全称  name:全称   sAMAccountName:账号  userPrincipalName:账号@mastercn.local,userAccountControl 状态,memberOf 属于哪个组}
#dn  "dn": "CN=袁 海英,OU=事业一部离职,OU=Employee,DC=mastercn,DC=local"
#512 正常 2 禁用  514=账号正常+禁用
#66050=65536+512+2 密码不过期+正常+禁用
#66048=65536+512 密码不过期+正常
import xlwings as xw
app=xw.App(visible=False,add_book=True)
book=app.books.add()
sheet=book.sheets['sheet1']
sheet.range('a1').value=list
book.save('77.xlsx')
book.close()
app.quit()
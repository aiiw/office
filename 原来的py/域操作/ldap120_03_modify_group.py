import sys
import json
import re
#查询作用,通过部门查人员
from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES,ALL, NTLM
server = Server('192.168.0.120', get_info=ALL)
conn = Connection(server, user='mastercn\\Dnk', password='M2925090', auto_bind=True, authentication=NTLM)
#self.conn.extend.microsoft.modify_password(dn, "XXXXXXXXX")    #设置用户密码
#self.conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE',512)]})    #激活用户
#self.conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE',512)]})    #激活用户
user01=conn.search('dc=mastercn,dc=local', search_filter ='(&(objectCategory=person)(sAMAccountName=11608))', attributes=['*'],size_limit=25000, get_operational_attributes=True,search_scope = 1) #search_scope 为1是不包含下级,2为包含下级
user01=conn.search('dc=mastercn,dc=local', search_filter ='(sAMAccountName=11608)', attributes=['*'],size_limit=25000, get_operational_attributes=True) #search_scope 为1是不包含下级,2为包含下级
# print(conn.response)
# print(conn.entries[0].entry_to_json())  # 查询到的数据  将列转为{attributes:'',dn:''}
# print(conn.entries[0])  # 查询到的数据# 列表

dn=json.loads(conn.entries[0].entry_to_json()).get('dn')
print(dn)
# self.conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE',512)]})    #激活用户
conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE',512)]})    #激活用户
conn.modify_dn()
from ldap3 import Server, Connection, ALL, NTLM
import json

# 连接
server = Server('192.168.0.120', get_info=ALL)
conn = Connection(server, user='mastercn\\11608', password='12qwaszx', authentication=NTLM)

# 手动绑定连接并检查状态
if conn.bind():
    print('Successfully authenticated LDAP user')
else:
    print('Failed to authenticate LDAP user')
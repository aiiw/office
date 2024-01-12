import sys
import json
import re
#查询作用,通过部门查人员
from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES,ALL, NTLM
def get_login_computers_by_account(account):
    # 建立与LDAP服务器的连接
    server = Server('192.168.0.120', get_info=ALL)
    conn = Connection(server, user='mastercn\\up', password='123369', auto_bind=True, authentication=NTLM)

    # 查询作用，通过用户账号查人员
    user_search_filter = f'(&(objectCategory=person)(userPrincipalName={account}))'
    user_info = conn.search(search_base='dc=mastercn,dc=local', search_filter=user_search_filter, attributes=['memberOf'])

    computers = []
    if len(conn.entries) > 0:
        memberOf = conn.entries[0].memberOf.values
        if memberOf:
            computer_search_filter = f'(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=8192)(|(memberOf={memberOf})))'
            computer_info = conn.search(search_base='dc=mastercn,dc=local', search_filter=computer_search_filter, attributes=['sAMAccountName'])
            
            for computer in computer_info.entries:
                computer_name = computer.sAMAccountName.value
                computers.append(computer_name)

    return computers

account = '11601'
computers = get_login_computers_by_account(account)
print(f"账号 {account} 可以登录的计算机列表：")
for computer in computers:
    print(computer)


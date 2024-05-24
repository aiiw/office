import sys
import json
import re
#查询作用,通过部门查人员
from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES,ALL, NTLM
server = Server('192.168.0.120', get_info=ALL)
conn = Connection(server, user='mastercn\\up', password='123369', auto_bind=True, authentication=NTLM)
# conn1 = Connection(server, user='mastercn\\Dnk', password='M2925090', auto_bind=True, authentication=NTLM)
res = conn.search('dc=mastercn,dc=local', search_filter ='(objectCategory=organizationalUnit)', attributes=['*'],size_limit=25000, get_operational_attributes=True)
result=conn.entries[1].entry_to_json()
result1=json.loads(result)
# print(result)

print(result1.get('attributes'))

# {
#     "attributes": {
#         "dSCorePropagationData": [
#             "2021-09-06 02:32:01+00:00",
#             "2018-06-12 11:31:26+00:00",
#             "2018-06-12 11:26:07+00:00",
#             "2017-04-14 02:08:42+00:00",
#             "1601-01-01 18:29:21+00:00"
#         ],
#         "description": [
#             "\u603b\u88c1\u529e"
#         ],
#         "distinguishedName": [
#             "OU=ZCB\u603b\u88c1\u529e,OU=Mastergroup,DC=mastercn,DC=local"
#         ],
#         "instanceType": [
#             4
#         ],
#         "name": [
#             "ZCB\u603b\u88c1\u529e"
#         ],
#         "objectCategory": [
#             "CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=mastercn,DC=local"
#         ],
#         "objectClass": [
#             "top",
#             "organizationalUnit"
#         ],
#         "objectGUID": [
#             "{150a5a74-0895-43af-be06-2785d036fce3}"
#         ],
#         "ou": [
#             "ZCB\u603b\u88c1\u529e"
#         ],
#         "uSNChanged": [
#             52273486
#         ],
#         "uSNCreated": [
#             12387
#         ],
#         "whenChanged": [
#             "2020-03-07 08:30:10+00:00"
#         ],
#         "whenCreated": [
#             "2005-10-03 15:57:18+00:00"
#         ]
#     },
#     "dn": "OU=ZCB\u603b\u88c1\u529e,OU=Mastergroup,DC=mastercn,DC=local"
# }
# [Finished in 1.2s]
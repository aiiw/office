import sys
import json
import re
#查询作用,通过部门查人员
from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES,ALL, NTLM
server = Server('192.168.0.120', get_info=ALL)
conn = Connection(server, user='mastercn\\up', password='123369', auto_bind=True, authentication=NTLM)
# conn1 = Connection(server, user='mastercn\\Dnk', password='M2925090', auto_bind=True, authentication=NTLM)
res = conn.search('dc=mastercn,dc=local', search_filter ='(objectCategory=person)', attributes=['*'],size_limit=25000, get_operational_attributes=True)
result=conn.entries[1].entry_to_json()
result1=json.loads(result)
print(result)

print(result1.get('attributes'))

# {

#objectCategory=person


# {
#     "attributes": {
#         "accountExpires": [
#             "9999-12-31 23:59:59.999999+00:00"
#         ],
#         "badPasswordTime": [
#             "2021-08-18 10:59:57.152489+00:00"
#         ],
#         "badPwdCount": [
#             3
#         ],
#         "cn": [
#             "Guest"
#         ],
#         "codePage": [
#             0
#         ],
#         "countryCode": [
#             0
#         ],
#         "dSCorePropagationData": [
#             "2021-09-06 02:32:50+00:00",
#             "2018-06-12 11:31:33+00:00",
#             "1601-01-01 00:21:21+00:00"
#         ],
#         "description": [
#             "Built-in account for guest access to the computer/domain"
#         ],
#         "distinguishedName": [
#             "CN=Guest,CN=Users,DC=mastercn,DC=local"
#         ],
#         "instanceType": [
#             4
#         ],
#         "isCriticalSystemObject": [
#             true
#         ],
#         "lockoutTime": [
#             "2023-07-21 08:54:34.190420+00:00"
#         ],
#         "memberOf": [
#             "CN=Guests,CN=Builtin,DC=mastercn,DC=local"
#         ],
#         "name": [
#             "Guest"
#         ],
#         "objectCategory": [
#             "CN=Person,CN=Schema,CN=Configuration,DC=mastercn,DC=local"
#         ],
#         "objectClass": [
#             "top",
#             "person",
#             "organizationalPerson",
#             "user"
#         ],
#         "objectGUID": [
#             "{1b37ea59-3d71-43ca-ad00-71d9e98aecb7}"
#         ],
#         "objectSid": [
#             "S-1-5-21-1387195525-1636011110-1427239487-501"
#         ],
#         "primaryGroupID": [
#             514
#         ],
#         "pwdLastSet": [
#             "1601-01-01 00:00:00+00:00"
#         ],
#         "sAMAccountName": [
#             "Guest"
#         ],
#         "sAMAccountType": [
#             805306368
#         ],
#         "uSNChanged": [
#             108207009
#         ],
#         "uSNCreated": [
#             8214
#         ],
#         "userAccountControl": [
#             66082
#         ],
#         "whenChanged": [
#             "2023-07-21 08:54:35+00:00"
#         ],
#         "whenCreated": [
#             "2005-10-01 03:43:01+00:00"
#         ]
#     },
#     "dn": "CN=Guest,CN=Users,DC=mastercn,DC=local"
# }
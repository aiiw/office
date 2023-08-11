#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from ldap3 import ALL_ATTRIBUTES
# 注意：ldap3库如果要使用tls（安全连接），需要ad服务先安装并配置好证书服务，才能通过tls连接，否则连接测试时会报LDAPSocketOpenError('unable to open socket'
# 如果是进行账号密码修改及账户激活时，会报错：“WILL_NOT_PERFORM”
from ldap3 import Connection, NTLM, Server
from ldap3 import MODIFY_REPLACE
server1 = Server("adtest.com", port=636, use_ssl=True, get_info=ALL, connect_timeout=5)
LDAP_SERVER_POOL = [192.168.0.120]
SERVER_USER = 'mastercn\\Dnk'
SERVER_PASSWORD = "M2925090"
class AD(object):
    '''    AD用户操作    '''
    def __init__(self):
        '''初始化'''
        self.conn = Connection( #配置服务器连接参数
            server=LDAP_SERVER_POOL,
            auto_bind=True,
            authentication=NTLM,  #连接Windows AD需要配置此项
            read_only=False,  #禁止修改数据：True
            user=SERVER_USER,#管理员账户
            password=SERVER_PASSWORD,
        )

        self.leaved_base_dn = 'ou=Leaved,dc=adtest,dc=intra'#离职账户所在OU
        self.active_base_dn = 'ou=测试部门,dc=adtest,dc=intra'#正式员工账户所在OU
        self.search_filter = '(objectclass=user)'#只获取【用户】对象
        self.ou_search_filter = '(objectclass=organizationalUnit)'#只获取【OU】对象

    def users_get(self):
        '''获取所有的用户'''
        self.conn.search(search_base=self.active_base_dn,search_filter=self.search_filter,attributes=ALL_ATTRIBUTES)
        res = self.conn.response_to_json()
        res = json.loads(res)['entries']
        return res

    def OU_get(self):
        '''获取所有的OU'''
        self.conn.search(search_base=self.active_base_dn,search_filter=self.ou_search_filter,attributes=ALL_ATTRIBUTES)
        res = self.conn.response_to_json()
        res = json.loads(res)['entries']
        return res

    def create_obj(self,dn,type,attr=None):
        '''
        新建用户or 部门，User需要设置密码，激活账户
        :param dn: dn = "ou=人事部3,ou=罗辑实验室,dc=adtest,dc=intra"  # 创建的OU的完整路径
                   dn = "cn=张三,ou=人事部3,ou=罗辑实验室,dc=adtest,dc=intra"  # 创建的User的完整路径
        :param type:选项：ou or user
        :param attr = {#User 属性表，需要设置什么属性，增加对应的键值对
                        "SamAccountName": "zhangsan",  # 账号
                        "EmployeeID":"1",    # 员工编号
                        "Sn": "张",  # 姓
                        "name": "张三",
                        "telephoneNumber": "12345678933",
                        "mobile": "12345678933",
                        "UserPrincipalName":"zhangsan@adtest.com",
                        "Mail":"zhangsan@adtest.com",
                        "Displayname": "张三",
                        "Manager":"CN=李四,OU=人事部,DC=adtest,DC=com",#需要使用用户的DN路径
                    }
                attr = {#OU属性表
                        'name':'人事部',
                        'managedBy':"CN=张三,OU=IT组,OU=罗辑实验室,DC=adtest,DC=intra", #部分负责人
                        }
        :return:True and success 是创建成功了
        (True, {'result': 0, 'description': 'success', 'dn': '', 'message': '', 'referrals': None, 'type': 'addResponse'})

        '''
        object_class = {'user':['user', 'posixGroup', 'top'],
                        'ou':['organizationalUnit', 'posixGroup', 'top'],
                        }
        res = self.conn.add(dn=dn,object_class=object_class[type],attributes=attr)
        if type == "user": # 如果是用户时，我们需要给账户设置密码，并把账户激活
            self.conn.extend.microsoft.modify_password(dn, "XXXXXXXXX")    #设置用户密码
            self.conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE',512)]})    #激活用户
        return res, self.conn.result

    def del_obj(self,DN):
        '''
        删除用户 or 部门
        :param DN:
        :return:True
        '''
        res = self.conn.delete(dn=DN)
        return res

    def update_obj(self, dn, attr):
        '''更新员工 or 部门属性
        先比较每个属性值，是否和AD中的属性一致，不一样的记录，统一update
        注意：
            1. attr中dn属性写在最后
            2. 如果name属性不一样的话，需要先变更名字（实际是变更原始dn为新name的DN），后续继续操作update and move_object
        User 的 attr 照如下格式写：
        dn = "cn=test4,ou=IT组,dc=adtest,dc=com" #需要移动的User的原始路径
        {#updateUser需要更新的属性表
             "Sn": "李",  # 姓
             "telephoneNumber": "12345678944",
             "mobile": "12345678944",
             "Displayname": "张三3",
             "Manager":"CN=李四,OU=人事部,DC=adtest,DC=com",#需要使用用户的DN路径
             'DistinguishedName':"cn=张三,ou=IT组,dc=adtest,dc=com" #用户需要移动部门时，提供此属性，否则不提供
            }

        OU 的 attr 格式如下：
        dn = "ou=人事部,dc=adtest,dc=com" #更新前OU的原始路径
        attr = {
        'name':'人事部',
        'managedBy':"CN=张三,OU=IT组,DC=adtest,DC=com",
        'DistinguishedName': "ou=人事部,dc=adtest,dc=com" # 更新后的部门完整路径
        }
        '''
        changes_dic = {}
        for k,v in attr.items():
            if not self.conn.compare(dn=dn,attribute=k,value=v):
                if k == "name":
                    res = self.__rename_obj(dn=dn,newname=attr['name']) # 改过名字后，DN就变了,这里调用重命名的方法
                    if res['description'] == "success":
                        if "CN" == dn[:2]:
                            dn = "cn=%s,%s" % (attr["name"], dn.split(",", 1)[1])
                        if "OU" == dn[:2]:
                            dn = "DN=%s,%s" % (attr["name"], dn.split(",", 1)[1])
                if k == "DistinguishedName": # 如果属性里有“DistinguishedName”，表示需要移动User or OU
                    self.__move_object(dn=dn,new_dn=v) # 调用移动User or OU 的方法
                changes_dic.update({k:[(MODIFY_REPLACE,[v])]})
                self.conn.modify(dn=dn,changes=changes_dic)
        return self.conn.result

    def __rename_obj(self,dn,newname):
        '''
        OU or User 重命名方法
        :param dn:需要修改的object的完整dn路径
        :param newname: 新的名字，User格式："cn=新名字";OU格式："OU=新名字"
        :return:返回中有：'description': 'success', 表示操作成功
        {'result': 0, 'description': 'success', 'dn': '', 'message': '', 'referrals': None, 'type': 'modDNResponse'}
        '''
        self.conn.modify_dn(dn,newname)
        return self.conn.result

    def compare_attr(self,dn,attr,value):
        '''比较员工指定的某个属性
        '''
        res = self.conn.compare(dn=dn,attribute=attr,value=value)
        return res

    def __move_object(self,dn,new_dn):
        '''移动员工 or 部门到新部门'''
        relative_dn,superou = new_dn.split(",",1)
        res = self.conn.modify_dn(dn=dn,relative_dn=relative_dn,new_superior=superou)
        return res


def check_credentials(username, password):
    """
    用户认证接口 #
    """
    ldap_user = '\\{}@adtest.intra'.format(username)
    server = Server('adtest.intra', use_ssl=True)

    connection = Connection(server, user=ldap_user, password=password, authentication=NTLM)
    try:
        logger.info("username:%s ;res: %s" %(username,connection.bind()))
        return connection.bind()
    except:
        logger.warning("username:%s ;res: %s" % (username, connection.bind()))
        return False
    finally:
        connection.closed
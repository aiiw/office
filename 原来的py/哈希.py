import hashlib,json
sha1 = hashlib.sha1()
sha1.update('1236473411'.encode('utf-8'))
sha1.update('1618967351'.encode('utf-8'))
sha1.update('alidongxing'.encode('utf-8'))
hashcode = sha1.hexdigest() #获取加密串
# print (hashcode)
#
#
# # md5加密
def md5sum(str):
    name=r'''<host prod="T100" ver="1.0" ip="10.40.40.18" id="t10tst" timestamp="20160414190605947" acct=""/><service prod="MES" name="create_mo" srvver="1.0"/>'''
    m = hashlib.md5()  # 创建一个hashlib.md5()对象
    m.update(name.encode(encoding='utf-8') ) # 将参数转换为UTF8编码
    print(m.hexdigest())  # 用十六进制输出加密后的数据



from hashlib import md5


def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


# 调用
if __name__ == '__main__':
    # name = r'''<host prod="CRMQ5" ver="1.0" ip="192.168.0.27" id="CRMQ5" timestamp="20220314024683576" acct="tiptop"/><service prod="test" name="demoService" srvver="1.0"/>'''
    # print(encrypt_md5(name))
    print("9db802dbfba0c728d33dca8aec342391")
    # host={"prod":"CRMQ5","ip":"192.168.0.27","id":"CRMQ5","lang":"zh_CN","timestamp":"20220314024683576","ver":"1.0","acct":"tiptop"}
    # service={"prod":"test","name":"demoService","ip":"192.168.4.251","id":"test"}
    # c='''""'''
    # c="{}""{}".format(json.dumps(host),json.dumps(service))
    # c='''"%s""%s"'''%(json.dumps(host),json.dumps(service)) {73BDA7696EE72779EFA68557450F9649}

    # print(encrypt_md5(c))
# digi-host: {"prod":"CRMQ5","ip":"192.168.0.27","id":"CRMQ5","lang":"zh_CN","timestamp":"20220314024683576","ver":"1.0","acct":"tiptop"}
# digi-service: {"prod":"test","name":"demoService","ip":"192.168.4.251","id":"test"}
# digi-datakey: {"FromSystem":"test"}
# digi-key: 9db802dbfba0c728d33dca8aec342391
    a=r"{prod='MES',ver='1.0',ip='10.20.88.49',id='',timezone='+8',timestamp='20190904120200',acct='admin'}{prod='RESTSERVICE',ip='10.20.88.49',id='',name='demoService',srvver='1.0'}"
    print(encrypt_md5(a))
    print('73BDA7696EE72779EFA68557450F9649')
    print(a)
    # b=r"{ip:'192.168.0.27',prod:'CRMQ5',id:'CRMQ5',lang:'zh_CN',timestamp:'20220314024683576',ver:'1.0',acct:'tiptop'}{prod:'test',name:'demoService',ip:'192.168.4.251',id:'test'}"
    # print(encrypt_md5(b))
    # print(b)


# name = r'''<host prod="CRMQ5" ver="1.0" ip="192.168.0.27" id="CRMQ5" timestamp="{}" acct=""/><service prod="HR" name="GetEmp" srvver="1.0"/>'''.format(timestamp)

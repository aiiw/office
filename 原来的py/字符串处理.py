

# dic={'no1':"t.xmdadocno",'no2':"t.xmda033",'IMAA001':"t.xmdc001",'IMAAL003':"t.imaal003",'IMAAL004':"t.imaal004"}

# for key,value in dic.items():
# 	ss='''${{if(len({key})=0,"",if(find("*",{key})>0,"AND {value} LIKE '%" + replace({key}, "*", "%") + "%'","AND {value}='" + {key} + "'"))}}'''
# 	ss='''${{if(len({key})=0,"",if(find("*",{key})>0,"AND {value} LIKE '" + replace({key}, "*", "%") + "'","AND {value}='" + {key} + "'"))}}'''
# 	aa=ss.format(key=key, value=value)
# 	print(aa)

# 采购单
dic={'no1':"t.单号",'no2':"t.生产单号",'IMAA001':"t.料号",'IMAAL003':"t.品名",'IMAAL004':"t.规格"}
for key,value in dic.items():
	ss='''${{if(len({key})=0,"",if(find("*",{key})>0,"AND {value} LIKE '%" + replace({key}, "*", "%") + "%'","AND {value}='" + {key} + "'"))}}'''
	ss='''${{if(len({key})=0,"",if(find("*",{key})>0,"AND {value} LIKE '" + replace({key}, "*", "%") + "'","AND {value}='" + {key} + "'"))}}'''
	aa=ss.format(key=key, value=value)
	print(aa)

str1=b'\xA5'
print(str1.decode('GBK'))


# str2="$"
# print(str2.encode('gbk'))
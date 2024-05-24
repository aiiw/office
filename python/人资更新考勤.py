def updatekq(newtime,wctime,code):
	import pymssql
#sql服务器名，这里(127.0.0.1)是本地数据库IP
	serverName = '192.168.0.181'
#登陆用户名和密码
	userName = 'sa'
	passWord = '$u2930123WJ'
#建立连接并获取cursor
	conn = pymssql.connect(serverName , userName , passWord, "T9IMS")
	cursor = conn.cursor()
#sql= f'INSERT into WorkCardSource VALUES {value}'
# sql='''update dd
# set dd.time='2022-12-16 07:55:55'
# from T_HR_PunchRecord dd
# where dd.Time='2022-12-16 07:59:55' and dd.CardNumber='11608'
# '''
# token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(appid,sceret) # 创建获取token的url
	sql=" update dd set dd.time='{}' from T_HR_PunchRecord dd where dd.Time='{}' and dd.CardNumber='{}'".format(newtime,wctime,code)
	print(sql) 
	cursor.execute(sql)


	conn.commit()
	conn.close()


if __name__ == '__main__':
    # getdept() #获取指定部门
    #getdept() #将部门写入wx_dept表
    updatekq('2022-12-16 07:55:55','2022-12-16 07:55:55','11608')

from pywebio.input import *
from pywebio.output import *


def kq(code,date,op):
    import pymssql
    #sql服务器名，这里(127.0.0.1)是本地数据库IP
    serverName = '192.168.0.180'
    #登陆用户名和密码
    userName = 'sa'
    passWord = '$u2930123WJ'
    #建立连接并获取cursor
    conn = pymssql.connect(serverName , userName , passWord, "KQA")
    cursor = conn.cursor()
    if op==1:
        time='07:59:16'
    elif op==2:
        time='12:03:16'
    elif op==3:
        time='13:56:56'
    elif op==4:
        time='18:09:12'

    value=('016',code,date,time)
    sql= f'INSERT into WorkCardSource VALUES {value}'
    # 查询记录
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return sql




from datetime import date as date1,timedelta
a="2023-09-20"
data = input_group("Basic info",[
    input('请输入你的工号', name='code'),
    input('请输入你的日期', name='date', type=DATE,value=a),
    input('请输入卡次', name='time', type=NUMBER),
])
# if kq(data['code'], data['date'],data['time']):
#     put_text('成功向数据库写入如下数据:',data['code'], data['date'],data['time'])
import os
import arrow
import re
import requests
import json
from urllib.parse import quote, unquote
from urllib import request
from remonth import remonths


def callkqtask():
    a = arrow.now()
    print(a)
    year = str(a.year)
    month = str(a.month)
    day = str(a.day)
    if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        month01 = year+"年0"+month+"月"
    else:
        month01 = year+"年"+month+"月"


    if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        month02 = "0"+month
    else:
        month02 = month



    startday = year+'-'+month02+'-01'
    endday = year+'-'+month02+'-'+day

    # month00=str(a)[0:7]+"月"
    #如下为增加取periodid
    dic={}
    n=24
    for j in range(2021,2100):
        for k in range(1,13):
            n=n+1
            if len(str(k))==1:
                kk='0'+str(k)
            else:
                kk=str(k)
            key=str(j)+str(kk)
            dic[key]=n

    #
    key1=year+month02
    print(key1)
    periodid=dic[key1]
    print(periodid)


    # month01=re.sub('\-',' ',month00)
    session = requests.Session()
    print(month01)
    print(startday)
    print(endday)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    header = {"User-Agent": ua,
              "Referer":  "http://192.168.0.181:8090/eHR/ATD15/Index",
              "Cookie": r"rffbvm0zaiariab5dak3idcd; __RequestVerificationToken=I8KeFtydQWIruk8yP2iBrLGV1g5XojuehemWpTlYlg-HAzLHWKl1K8K9_kA54lcLXjmUE3nbk-sIC9V-ASFI2sQEsa-PDH_cJBHM_1dU72_u6X0vTb3A4SGiXTbxWPt4GJRFrNz5lUb-rxg_povOew2; uid=id=1&usercode=admin&username=%e7%b3%bb%e7%bb%9f%e7%ae%a1%e7%90%86%e5%91%98&login=admin&usertype=9&isadmin=True&customcode=&suppliercode="
              }

    form_data = {
        "type": "1",
        "periodid": periodid,
        "begin": startday,
        "end": endday,
        "empid": "",
        "dept": "",
        "total": "true",
        "periodname": month01,
        "stbegin": startday,
        "stend": endday
    }
    print(form_data)

    i2 = session.post('http://192.168.0.181:8090/Api/ATD14Api/Calc',
                      headers=header, data=form_data)
    # i2 = session.post('http://192.168.0.181:8090/Api/PSN01Api/GetMst', headers = header,)
    # c2 = i2.cookies.get_dict()
    # files=open(r'c:\\log.txt','a+')
    # print(time.localtime(),file=files)
    # files.close()
    if not os.path.exists("d:\\log"):
        os.mkdir("d:\\log")
    files = open(r'd:\\log\\f2.txt', 'a+')
    d=arrow.now().format('YYYY-MM-DD HH:mm:ss')
    logmark = str(d)+"sussessful"+"\n"
    files.writelines(logmark)
    files.close()


callkqtask()

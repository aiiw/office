import os
import arrow
import re
import requests
import json
from urllib.parse import quote, unquote
from urllib import request
from remonth import remonths


def callkqtask(dept):
    print(dept)
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
        "dept": dept,
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


# callkqtask()
import xlrd,xlutils
from xlutils.copy import copy

wb=xlrd.open_workbook(r'zj.xlsx')
ws=wb.sheet_by_index(0)
col_values = ws.col_values(1)
for value in col_values:
    callkqtask(value)

# for i in range(10,19):
#     j='0'+str(i)
#     callkqtask(j)
# xlrd 是一个用于读取 Excel 文件的 Python 库。下面列出了 xlrd 中一些常用的方法：

# xlrd.open_workbook(filename, encoding_override=None, formatting_info=False, on_demand=False, ragged_rows=False): 打开指定的 Excel 文件并返回一个 workbook 对象。
# workbook.sheets(): 返回所有工作表对象的列表。
# workbook.sheet_by_name(sheet_name): 按名称获取工作表对象。
# workbook.sheet_by_index(sheetx): 按索引获取工作表对象。
# worksheet.cell(row, col): 返回指定行和列的单元格对象。
# worksheet.row_values(rowx, start_colx=0, end_colx=None): 返回指定行的值列表。
# worksheet.col_values(colx, start_rowx=0, end_rowx=None): 返回指定列的值列表。
# worksheet.nrows: 返回工作表中的行数。
# worksheet.ncols: 返回工作表中的列数。
# cell.value: 返回单元格的值。
# cell.ctype: 返回单元格的数据类型。
# 除上述方法外，xlrd 还提供了许多其他的方法和属性，例如：sheet_names()、sheet_loaded()、unload_sheet()、release_resources() 等。

# 需要注意的是，xlrd 主要用于读取 Excel 文件，并不支持写入。如果您需要生成或修改 Excel 文件，请使用其他第三方库，如 openpyxl 或 xlsxwriter
import xlrd,xlutils
from xlutils.copy import copy

wb=xlrd.open_workbook(r'd:\py\77.xlsx')
cope_file = copy(wb)
ws=wb.sheet_by_index(0)
print(ws.nrows)
print(ws.row_values(1))
print(ws.col_values(1))


sheet1=cope_file.get_sheet(0)  # 获取工作表
sheet1.write(0, 0, '第一行，第一列')
cope_file.save('cope_file.xls')  # 保存
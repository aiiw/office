import os
import openpyxl
from pathlib import Path
import xlrd #读取数据

from mysqlclass import Database
db = Database(
    host="192.168.0.7",
    user="root",
    port="3306",
    passwd="123456",
    database="dj3"
)

class walk():
	"""docstring for wark"""
	path=''
	def __init__(self, path):
		self.path = path
	def getfiles(self):
		print("path %s"%(self.path))
		list=[]
		if os.path.exists(self.path):
			for root,dir,file in os.walk(self.path):
				for name in dir:
					# str=str+os.path.join(root, name)+'\n'
					continue
				for name in file:
					# str=str+os.path.join(root.replace("//","\\"), name)+'\n'
					list.append(os.path.join(root.replace("//","\\"), name))
		return list




def find_kpi_section(lst):
    start_index = None
    end_index = None

    for i in range(len(lst) - 1):
        if lst[i].startswith('K'):
            if start_index is None:
                start_index = i
            if not lst[i+1].startswith('K'):
                end_index = i
                break
    return start_index, end_index

if __name__ == '__main__':
	a=walk(r'E:\gongcheng')
	files=a.getfiles()
	n=0
	for file in files:
		n=n+1
		extension = Path(file).suffix
		# if extension=='xlsx':
		# 	try:
		# 		workbook = openpyxl.load_workbook(file)

		# 		workbook.close()
		# 	except Exception as e:
		# 		print("发生了错误:", e)
		# print(file)
		if (extension=='.xlsx' or extension=='.xls') and "~$" not in file:
			workbook = xlrd.open_workbook(file)
			#获取表单
			worksheet = workbook.sheet_by_index(0)
			#读取数据
			name = worksheet.cell_value(2,2)
			# code = worksheet.cell_value(3,4)
			# print(code,name,str(n))
			kpi=7
			row_values = worksheet.row_values(6)
			
			start_col, end_col=find_kpi_section(row_values)
			obj_list=[]
			# print(name,row_values,start_col, end_col)			
			for a in range(start_col,end_col+1):
				# colum_values = worksheet.row_values(6)
				column_values = worksheet.col_values(a)
				tem_list=column_values[6:20]
				# print(obj_list,tem_list)
				fields = ['部门','姓名', '指标名称', '指标定义', '指标权重', '计算公式', '数据来源', '月度奖金包', '目标值', '实际值', '计分标准']
				values=('工程中心',)+(name,) +(tem_list[0]+tem_list[1],)+tuple(tem_list[2:9])+(str(tem_list[9])+str(tem_list[10])+str(tem_list[11])+str(tem_list[11])+str(tem_list[12]),)
				last_id = db.insert('kpi', fields, values)
				print(last_id)

			
			# # 指定要读取的区域范围
			# start_row = 6  # 起始行索引（从0开始）
			# end_row = 16    # 结束行索（不包括该行）
			# start_col = 0  # 起始列索引（0开始）
			# end_col = 3    # 结束列索引（包括该列）

			# # 遍历指定区域的单元格打印值
			# for row in range(start_row, end_row):
			#     for col in range(start_col, end_col):
			#         cell_value = worksheet.cell_value(row, col)
			#         print(f'({row}, {col}): {cell_value}')

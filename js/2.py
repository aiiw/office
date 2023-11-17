import os

from pathlib import Path
import xlrd #读取数据



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




if __name__ == '__main__':
	a=walk(r'C:\Users\11608\Desktop\public')
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
#获取表单
			worksheet = workbook.sheet_by_index(0)
			c1 = worksheet.col_values(1)
			for c in c1:
				print(c)
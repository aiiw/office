import os
import re
from pathlib import Path
import xlrd #读取数据
import collections 


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
		list=[]
		list2=[]
		if (extension=='.xlsx' or extension=='.xls') and "63980"  in file:
			workbook = xlrd.open_workbook(file)
			#获取表单
#获取表单
			sheet = workbook.sheet_by_index(0)
			n=True
			for i in range(sheet.nrows):  #循环获取每行的内容
				list.append(sheet.row_values(i))
				row_list=sheet.row_values(i)
				if n:
					n=False
					continue



				a=('16','63980',row_list[3],row_list[7],)
				b=('16','63980',row_list[3],row_list[8],)
				c=('16','63980',row_list[3],row_list[9],)
				d=('16','63980',row_list[3],row_list[10],)





				if row_list[7]:
					list2.append(a)
				if row_list[8]:
					list2.append(b)
				if row_list[9]:
					list2.append(c)
				if row_list[10]:
					list2.append(d)

			print(list2)
			#value=[('16','62917','2021-10-20 00:00:00.000','07:29:00'),('16','62917','2021-10-20 00:00:00.000','11:30:00'),('16','62917','2021-10-20 00:00:00.000','13:29:00'),('16','62917','2021-10-20 00:00:00.000','17:31:00')]

			import pymssql
			#sql服务器名，这里(127.0.0.1)是本地数据库IP
			serverName = '192.168.0.180'
			#登陆用户名和密码
			userName = 'sa'
			passWord = '$u2930123WJ'
			#建立连接并获取cursor
			conn = pymssql.connect(serverName , userName , passWord, "KQA")
			cursor = conn.cursor()
			sql= f'INSERT into WorkCardSource values(%s,%s,%s,%s)'
			# 查询记录
			# cursor.executemany(sql,list2)

			# 获取一条记录
			# row = cursor.fetchone()
			# # 循环打印记录(这里只有一条，所以只打印出一条)
			# while row:
			# 	# a=row[0].encode('utf-8')
			# 	# b=row[8].encode('gbk').decode('utf-8')
				
			# 	row = cursor.fetchone()
			# # 连接用完后记得关闭以释放资源
			# conn.commit()
			# conn.close()
import os
import re
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
			keys = worksheet.col_values(0)
			values = worksheet.col_values(1)
			dictionary = dict(zip(keys, [value.strip() for value in values]))
			# print(dictionary)
	string = '''
	SELECT xmdfuc013,
       xmdfuc009,
       xmdfuc011,
       xmdeuc038,
       xmdfuc039,
       SUM(xmdfuc038),
       xmdeuc010,
       xmdeuc006,
       xmdeuc007,
       xmdfuc029,
       SUM(xmdfuc028),
       xmdeuc023,
       xmdeuc022,
       xmdeuc021,
       xmdeuc018,
       xmdeuc014,
       xmdeuc005,
       xmdeuc016,
       xmdeuc004,
       xmdeuc003,
       xmdeuc015,
       xmdeuc027,
       xmdeuc002,
       xmdeuc009,
       xmdeuc001,
       xmdeucsite,
       xmdeucent,
       xmdeuc017,
       xmdfuc002,
       xmdfuc001,
       xmdeuc040,
       xmdeuc034,
       xmdeuc024,
       xmdeuc012,
       xmdeuc039,
       xmdfucent,
       xmdfucdocno,
       xmdeucdocno,
       xmdeuc029,
       xmdeuc026,
       SUM(xmdfuc025),
       xmdfuc026,
       xmdeuc053,
       xmdeuc060,
       xmdeuc020
  FROM xmdeuc_t, xmdfuc_t
 WHERE xmdeucdocno = 'DDX55-23060700001'
   and xmdeucdocno = xmdfucdocno
   AND 1 = 1
 GROUP BY xmdfuc013,
          xmdfuc009,
          xmdfuc011,
          xmdeuc038,
          xmdfuc039,
          xmdeuc010,
          xmdeuc006,
          xmdeuc007,
          xmdfuc029,
          xmdeuc023,
          xmdeuc022,
          xmdeuc021,
          xmdeuc018,
          xmdeuc014,
          xmdeuc005,
          xmdeuc016,
          xmdeuc004,
          xmdeuc003,
          xmdeuc015,
          xmdeuc027,
          xmdeuc002,
          xmdeuc009,
          xmdeuc001,
          xmdeucsite,
          xmdeucent,
          xmdeuc017,
          xmdfuc002,
          xmdfuc001,
          xmdeuc040,
          xmdeuc034,
          xmdeuc024,
          xmdeuc012,
          xmdeuc039,

          xmdfucent,
          xmdfucdocno,

          xmdeucdocno,
          xmdeuc029,
          xmdeuc026,
          xmdfuc026,

          xmdeuc053,
          xmdeuc060,

          xmdeuc020




'''


	pattern = r'[\W_]'  # 匹配空格和斜杠字符
	replacement = ''
# 找到 WHERE 后的子字符串
	where_index = string.upper().find("WHERE")
	if where_index != -1:
		where_string = string[where_index:]
	else:
		where_string = ""

# 对前半部分的字符串进行替换操作
	string = string[:where_index]
	for key, value in dictionary.items():
		string = string.replace(key, key + ' ' + key + re.sub(pattern, replacement, value))

# 拼接最终结果
	string = string + where_string

	print(string)
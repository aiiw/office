#旧版推荐使用xlrd,新版本推荐使用openpyxl
#降低第三方库xlrd的版本至1.2.0 支持xlsx
#pip show xlrd
#pip install --upgrade xlrd
#pip install xlrd==1.2.0
import os
import json
import time
import xlrd
import re
from pathlib import Path
from urllib.parse import  quote,unquote
import pandas as pd
import xlwings as xw
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
def remove_special_chars(text):
    # 去除特殊符号和换行符号
    cleaned_text = re.sub(r'[\s]|	', '', text.replace('\n', ''))
    return cleaned_text


def extract_numbers(text):
    pattern = r'\d+(?:\.\d+)?'
    numbers = re.findall(pattern, text)
    if len(numbers) >= 2:
        return int(numbers[0]), float(numbers[1])
    else:
    	if len(numbers) == 1:
    		return int(numbers[0]),0
    	else:
    		return 0,0

import random 
def generate_random_number():
    return random.randint(0, 5)  # 生成0到9之间的随机整数


if __name__ == '__main__':
	a=walk(r'C:\Users\11608\Desktop\public\gp') #walk是 个类,通过getfiles返回文件的列表
	files=a.getfiles()

	n=0
	my_dict={}
	list=[]
	list2=[]
	for filename in files:
		n=n+1
		print(n)
		extension = Path(filename).suffix
		
		if extension=='.xlsx' or extension=='.xls' in filename:
			# target_filename =filename.replace("gp", "gp2")
			# shutil.copy(filename, target_filename)
			try:
				workbook = xlrd.open_workbook(filename)
				sheet = workbook.sheet_by_name('Worksheet')
				row1=1
				col1=1
				A1 = sheet.cell_value(1,1) #访问是从0索引
				B1 = sheet.cell_value(1,2)
				print(A1)
				if A1=='2023-03-31':
					values=(filename,'第一季度',sheet.cell_value(2,1),sheet.cell_value(3,1),sheet.cell_value(4,1),sheet.cell_value(5,1))
					list.append(values)
				if A1=='2023-06-30':
					values=(filename,'第一季度',sheet.cell_value(2,2),sheet.cell_value(3,2),sheet.cell_value(4,2),sheet.cell_value(5,2))
					list.append(values)
					values1=(filename,'第二季度',sheet.cell_value(2,1),sheet.cell_value(3,1),sheet.cell_value(4,1),sheet.cell_value(5,1))
					list.append(values1)
			except Exception as e:
				list2.append(filename)
				print(filename,e)
				pass
	app1=xw.App(visible=False,add_book=True)
	book=app1.books.add()
	sheet=book.sheets['sheet1']
	sheet.range('a1').value=list
	book.save(r'C:\Users\11608\Desktop\public\88.xlsx')
	book.close()
	app1.quit()

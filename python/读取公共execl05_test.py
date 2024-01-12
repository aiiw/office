import os
import json
import time
import re
from pathlib import Path
import requests
from urllib.parse import  quote,unquote
import xlwings as xw
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
from bs4 import BeautifulSoup
from mysqlclass import Database

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
	db = Database(
    host="192.168.0.7",
    user="root",
    port="3306",
    passwd="123456",
    database="dj3"
)
	a=walk(r'C:\Users\11608\Desktop\public\gp') #walk是 个类,通过getfiles返回文件的列表
	files=a.getfiles()
	n=0
	my_dict={}
	for file in files:
		n=n+1
		print(n)
		# while n==3: #while也是一个循环, 这个是错误的
		# if n==1000:
		# 	break;
		# 	print("============================")
		extension = Path(file).suffix
		filename = Path(file).stem
		# if extension=='xlsx':
		# 	try:
		# 		workbook = openpyxl.load_workbook(file)

		# 		workbook.close()
		# 	except Exception as e:
		# 		print("发生了错误:", e)
		# print(file)
		list=[]
		list2=[]
		app = xw.App(visible=False)
		if extension=='.xlsx' or extension=='.xls'  in file:

			# print(file)
		# 打开Excel文件
			wb = xw.Book(file)
			# 选择工作表
			sheet = wb.sheets['Worksheet']
			# 读取单元格数据
			A1 = sheet.range('B2').value
			B1 = sheet.range('C2').value
			# print(A1)
			# print(B1)
			# sheet = workbook.sheet_by_index(0)


			my_dict_item1={}
			my_dict_item2={}
			fields = ['股票','期间', '净利润', '净利润同比', '扣非净利润', '扣非净利润同比']

			# last_id = db.insert('kpi', fields, values)
			if A1=='2023-03-31':
					my_dict_item1['第一季度']=sheet.range('B2').value
					my_dict_item1['净利润']=sheet.range('B3').value
					my_dict_item1['净利润同比增长率']=sheet.range('B4').value
					my_dict_item1['扣非净利润']=sheet.range('B5').value
					my_dict_item1['扣非净利润同比增长率']=sheet.range('B6').value
					my_dict[filename+"第一季度"]=my_dict_item1
					values=(filename,'第一季度',sheet.range('B3').value,sheet.range('B4').value,sheet.range('B5').value,sheet.range('B6').value)
					last_id = db.insert('gplr', fields, values)
			if B1=='2023-06-31':
					my_dict_item1['第二季度']=sheet.range('C2').value
					my_dict_item1['净利润']=sheet.range('C3').value
					my_dict_item1['净利润同比增长率']=sheet.range('C4').value
					my_dict_item1['扣非净利润']=sheet.range('C5').value
					my_dict_item1['扣非净利润同比增长率']=sheet.range('C6').value
					my_dict[filename+"第二季度"]=my_dict_item2
					values=(filename,'第二季度',sheet.range('C3').value,sheet.range('C4').value,sheet.range('C5').value,sheet.range('C6').value)
					last_id = db.insert('kpi', fields, values)
			# with open(r'C:\Users\11608\Desktop\public\gp.json', "w",encoding="utf-8") as json_file:
			# 	json.dump(my_dict, json_file,ensure_ascii=False, indent=4)
			wb.close()



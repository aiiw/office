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
			if n==2 :
				break
			# target_filename =filename.replace("gp", "gp2")
			# shutil.copy(filename, target_filename)
			try:
				# workbook = xlrd.open_workbook(filename)
				# 需要注意的是，如果你想读取多个表格并将其存储为一个字典，可以将 sheet_name 参数设置为 None。这样，返回的将是一个字典，键是表格名称，值是对应的 DataFrame。
				# 例如：data = pd.read_excel(filename, sheet_name=None)。
				#默认不写就是读取第一个表 
				#df = pd.read_excel('filename.xlsx', sheet_name='Sheet1')
				#使用 head() 方法可以查看 DataFrame 的前几行，默认显示前 5 行：
				df = pd.read_excel(filename,header=None)
				# df = pd.read_excel(filename, usecols='A:C', names=['A', 'B', 'C'])
				# print(df.columns)
				print('df.iat',df.iat[1, 1])#序号从0,0开始
				# print('df.iloc',df.iloc[1:6, 1])#序号从0,0开始
				A=df.iloc[0:6, 2]#返回series ,可以使用切片访问,如何返回的是DataFrame,不能使用切片访问.
				B=df.iloc[1:6, 2]#返回series ,可以使用切片访问
				print('A1',A[1])
				# # print('df.at',df.at[1, 'B'])# 序号 行:也是从0开始了.
				# print("loc=================================================start")
				# print('loc',df.iloc[1:3])
				# print("loc=================================================end")
				# print(type(df['A']))
				# sheet = workbook.sheet_by_name('Worksheet')
				# print(df.shape,filename)
				# 打印数据集的前几行
				# print(df.head())
			except Exception as e:
				list2.append(filename)
				print(filename,e)
				pass


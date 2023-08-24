import os
import json
import time
import xlrd
import re
from pathlib import Path
from urllib.parse import  quote,unquote
import pandas as pd
import shutil
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
			except Exception as e:
				list2.append(filename)
				print(filename)
				pass
	print(list2)

# def delete_file(file_path):
#     try:
#         os.remove(file_path)
#         print("文件删除成功")
#     except FileNotFoundError:
#         print("文件不存在")
#     except PermissionError:
#         print("没有权限删除文件")
#     except Exception as e:
#         print(f"发生错误: {str(e)}")
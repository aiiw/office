import os
import json
import time
import re
from pathlib import Path
import xlrd #读取数据
import collections 
import requests
from urllib.parse import  quote,unquote
import xlwings as xw

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}



from bs4 import BeautifulSoup
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

from mysqlclass import Database
db = Database(
    host="192.168.0.7",
    user="root",
    port="3306",
    passwd="123456",
    database="dj3"
)
import queue
if __name__ == '__main__':
	a=walk(r'C:\Users\11608\Desktop\public\gp') #walk是 个类,通过getfiles返回文件的列表
	files=a.getfiles()
	n=0
	my_dict={}
	list=[]
	list2=[]
	
	for file in files:
	    n = n + 1
	    print(n)
	    print(file)
	    
	    try:
	        app = xw.App(visible=False)
	        wb = xw.Book(file)
	        wb.save()
	        wb.close()
	        os.system("taskkill /f /im EXCEL.EXE")

	    except Exception as e:
	        print(f"Error occurred while processing {file}: {str(e)}")
	        pass
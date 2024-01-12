import os
import json
import time
import re
from pathlib import Path
import xlrd #��ȡ����
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
    # ȥ��������źͻ��з���
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
    return random.randint(0, 5)  # ����0��9֮����������

from mysqlclass import Database
db = Database(
    host="192.168.0.7",
    user="root",
    port="3306",
    passwd="123456",
    database="dj3"
)

if __name__ == '__main__':
	a=walk(r'C:\Users\11608\Desktop\public\gp') #walk�� ����,ͨ��getfiles�����ļ����б�
	files=a.getfiles()
	n=0
	my_dict={}
	for file in files:
		n=n+1
		print(n)
		# while n==3: #whileҲ��һ��ѭ��, ����Ǵ����
		if n==1000:
			break;
			print("============================")
		extension = Path(file).suffix
		filename = Path(file).stem
		# if extension=='xlsx':
		# 	try:
		# 		workbook = openpyxl.load_workbook(file)

		# 		workbook.close()
		# 	except Exception as e:
		# 		print("�����˴���:", e)
		# print(file)
		list=[]
		list2=[]
		if extension=='.xlsx' or extension=='.xls'  in file:

			print(file)
		# ��Excel�ļ�
			# app = xw.App(visible=False)
			wb = xw.Book(file)
			# ѡ������
			sheet = wb.sheets['Worksheet']
			# ��ȡ��Ԫ������
			A1 = sheet.range('B2').value
			B1 = sheet.range('C2').value
			print(A1)
			print(B1)
			# sheet = workbook.sheet_by_index(0)


			my_dict_item1={}
			my_dict_item2={}
			fields = ['��Ʊ','�ڼ�', '������', '������ͬ��', '�۷Ǿ�����', '�۷Ǿ�����ͬ��']
			values=(,)
			last_id = db.insert('kpi', fields, values)
			if A1=='2023-03-31':
					my_dict_item1['��һ����']=sheet.range('B2').value
					my_dict_item1['������']=sheet.range('B3').value
					my_dict_item1['������ͬ��������']=sheet.range('B4').value
					my_dict_item1['�۷Ǿ�����']=sheet.range('B5').value
					my_dict_item1['�۷Ǿ�����ͬ��������']=sheet.range('B6').value
					my_dict[filename+"��һ����"]=my_dict_item1
					values=(filename,'��һ����',sheet.range('B3').value,sheet.range('B4').value,sheet.range('B5').value,sheet.range('B6').value)
					last_id = db.insert('kpi', fields, values)
			if B1=='2023-06-31':
					my_dict_item1['�ڶ�����']=sheet.range('C2').value
					my_dict_item1['������']=sheet.range('C3').value
					my_dict_item1['������ͬ��������']=sheet.range('C4').value
					my_dict_item1['�۷Ǿ�����']=sheet.range('C5').value
					my_dict_item1['�۷Ǿ�����ͬ��������']=sheet.range('C6').value
					my_dict[filename+"�ڶ�����"]=my_dict_item2
					values=(filename,'�ڶ�����',sheet.range('C3').value,sheet.range('C4').value,sheet.range('C5').value,sheet.range('C6').value)
					last_id = db.insert('kpi', fields, values)
			with open(r'C:\Users\11608\Desktop\public\gp.json', "w",encoding="utf-8") as json_file:
				json.dump(my_dict, json_file,ensure_ascii=False, indent=4)



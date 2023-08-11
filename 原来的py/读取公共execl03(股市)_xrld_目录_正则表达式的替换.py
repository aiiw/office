import os
import re
from pathlib import Path
import xlrd #读取数据
import collections 
import requests
from urllib.parse import  quote,unquote
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
		if (extension=='.xlsx' or extension=='.xls') and "000002"  in file:
			workbook = xlrd.open_workbook(file)
			#获取表单
#获取表单
			# sheet = workbook.sheet_by_index(0)
			#换一种方式,通过name
			sheet = workbook.sheet_by_name('Sheet1')
			rows=sheet.nrows
			# print(rows)
			for row in range(1,rows):
				gp=sheet.cell_value(row,0)[2:]
				gpname=sheet.cell_value(row,1)
				url=r'http://basic.10jqka.com.cn/{}/bonus.html'.format(gp)
				# print(url)
				r = requests.get(url, headers=headers )
				html_doc=unquote(r.content.decode( 'gbk' ))
				# print(html_doc)
				soup = BeautifulSoup(html_doc, 'html.parser')
				# ls = soup.find_all(class_ = 'p5_0 tip f14')  #这个地方class要加_
				div = soup.find('div', class_='p5_0 tip f14')
				content = remove_special_chars(div.get_text().strip())
				# content=div.get_text().strip()
				first_number, second_number = extract_numbers(div.get_text().strip())

				print(gp,gpname,":",str(first_number),str(second_number))
				# print(content)
				# pattern=r'\d+(?:\.\d+)?'
				# numbers = re.findall(pattern, content)
				# print(numbers)



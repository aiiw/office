# import json
# list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
import os

def abcd(**id):
	print(type(id))
	# os.mkdir(r'e:/ab')
def abc(*id):
	print(type(id))
	mid=','.join(["'%s'"%item for item in id])
	print(mid)

class walk():
	"""docstring for wark"""
	path=''
	def __init__(self, path):
		self.path = path
	def speak(self):
		print("path %s"%(self.path))
		str=''
		if os.path.exists(self.path):
			for root,dir,file in os.walk(self.path):
				for name in dir:
					str=str+os.path.join(root, name)+'\n'
				for name in file:
					str=str+os.path.join(root.replace("//","\\"), name)+'\n'
		return str
if __name__ == '__main__':
	# abc('1','2','3','d')
	a=walk(r'E:\gongcheng')
	print(a.speak())
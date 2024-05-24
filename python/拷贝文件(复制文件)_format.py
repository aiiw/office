import os 
list=['47313','47314','62960','62962','62968','62967','62977','62979','62984','63026','63046','63032','63045','63048','63049','63136','63137','63139','63155','63149','63161','63193','63211','63207','63213','63318','63333','63335','47347','63362']
for i in list:
	os.system(r'copy D:\py\img1\{}.bmp D:\py\img2\{}.bmp'.format(i,i))

list1=[]
class walk():
	"""docstring for wark"""
	
	def __init__(self, path):
		self.path = path
	def speak(self):
		print("path %s"%(self.path))
		str=''
		if os.path.exists(self.path):
			for root,dir,file in os.walk(self.path):
				for name in dir:
					pass
				for name in file:
					list1.append(name[:-4])
path=r'D://py//img2//'
ins=walk(path)
ins.speak()
# print(list1)

set1=set(list)
set2=set(list1)
set3=set1-set2
print(set3)

a={'1','2','3'}
b={'1','2'}

c=a-b
print(c)

# &	取两集合公共的元素
# |	取两集合全部的元素
# -	取一个集合中另一集合没有的元素
# ^	取集合 A 和 B 中不属于 A&B 的元素

# 原始
# class walk():
# 	"""docstring for wark"""
# 	path=''
# 	def __init__(self, path):
# 		self.path = path
# 	def speak(self):
# 		print("path %s"%(self.path))
# 		str=''
# 		if os.path.exists(self.path):
# 			for root,dir,file in os.walk(self.path):
# 				for name in dir:
# 					str=str+os.path.join(root, name)+'\n'
# 				for name in file:
# 					str=str+os.path.join(root.replace("//","\\"), name)+'\n'

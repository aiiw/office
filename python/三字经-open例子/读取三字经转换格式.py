import os,re
files=open(r'f2.txt','a+')
with open(r'千字文.txt','r+') as r1:
	str1=re.compile(r'[\n\r]')
	# n=0
	# r2=''
	# open 
	# for line in r1:
	#     #ls=str.sub('',line)
	# 	n=n+1
		
	# 	if n%2==0:
	# 		print(str(n))
	# 		r2=r2+line
	# 	else:
	# 		print(str(n))
	# 		r2=r2+str1.sub('',line)
	list1=r1.readlines()
	n=0
	for l1 in list1:
		# print(l1.count('\n'))
		# print(len(l1))
		# print(l1)
		# print('##'*100)
		# if l1.count('\n')!=len(l1):#全行的数量 为1  换行的也是1
		if len(l1)!=1:#只有一个空白行
			#print(len(l1),l1)
			n=n+1
			l1=str1.sub('',l1)
			
			if n%2==0:
				print(n,l1,file=files)
			else:
				print(n,l1,end='',file=files)
	
files.close()
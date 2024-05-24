import os
path=r'img'
for root,dir,file in os.walk(path):
	
	n=0
	d=os.path.abspath(root)
	for i in file:
		n=n+1
		f=os.path.join(os.path.abspath(root),i)
		
		if f:
			
			
			x=str(n)+'.png'
			print(f,x)
			os.system('rename %s %s'%(f,x))
			# print('dir %s'%('192.18.1.1'))
			# os.rename(f,d+str(n)+'.png') 

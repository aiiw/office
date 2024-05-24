dic={}#直接赋值,不需要var
#####################################解决人资的周期问题
n=24
for j in range(2021,2100):
	for k in range(1,13): #左开右闭
			n=n+1
			if len(str(k))==1:
				kk='0'+str(k)
			else:
				kk=str(k)
			key=str(j)+str(kk)
			dic[key]=n

key1='202212'
print(dic[key1])
#######################################
for i in range(1,10):
	print(i)
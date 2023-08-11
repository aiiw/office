def abc(n):
	i=0
	if n==0:
		return 1
	vv=abc(n-1)*n
	i=2
	print("-----",i)
	# abc(n-1) 多个循环
	
	return vv

	
	

print("----------------------")
print(abc(2))

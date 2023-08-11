def elclick(level):
	print("aaa")
	if level==1 :
		return 'a'
	else:
		elclick(level-1)


elclick(10)



def elclick1(n):
	print("bbb")
	if n==1:
		return
	else:
		for a in range(1,n):
			elclick1(a)
		return

# elclick1(3)
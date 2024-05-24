import random
def a(fun):
	return fun

# def b(x):
# 	for i in range(1,x):
# 		yield random.randint(1, 5)

# gens = b(10)

# list=[i for i in gens]
# print(list)



def c(x):
	for i in range(0,x):
		yield random.randint(25, 29),random.randint(1, 60),random.randint(33, 45),random.randint(1, 60),random.randint(45, 59),random.randint(1, 60),random.randint(33, 45),random.randint(1,59)
		#它与return的区别,在这里的理解,return每次返回后取最新的数据,但是yield会返回一个列表

gens = c(3)

list=[['07:%s:%s'%(tu[0],tu[1]),'11:%s:%s'%(tu[2],tu[3]),'12:%s:%s'%(tu[4],tu[5]),'17:%s:%s'%(tu[6],tu[7])] for tu in gens]
print(list)

# for i in gens:
# 	print(i)





# def c():
# 	return random.randint(25, 29),random.randint(1, 60),random.randint(33, 45),random.randint(1, 60),random.randint(45, 59),random.randint(1, 60),random.randint(33, 45),random.randint(1,59)
# tu=c()
# t1=[['07:%s:%s'%(tu[0],tu[1]),'11:%s:%s'%(tu[2],tu[3]),'12:%s:%s'%(tu[4],tu[5]),'17:%s:%s'%(tu[6],tu[7])]for i in range(10)]
# print(t1)
# tu=c()
# print(tu[0],tu[1])

# for a in gens:
# 	print(a)

# t2=(x for x in gens)

# for t in t2:
# 	print(t2,"aiiw")


# b=('A','B')
# s='ssddf%sdfdfd%s'%b
# print(s)


# g = (i for i in range(1000000))
# print(g.__next__())
# print(g.__next__())
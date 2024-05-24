# def a1(a='a'):
# 	print(a1,a)
# 	return a1

# def arr(fun):
# 	print("sb")
# 	fun() #参数设置默认值后,可以不写参数
# 	print("bs")

# arr(a1) #这个是将函数当参数传递


# def b1(a='bb'): 
# 	print("aa") #执行
# 	def b2(): #定义
# 		print(a)

# 	return b2 #返回
# 	b2()#这个返回就不执行了
	


# b1() #函数的参数会向下传递的~~
# b2=b1()
# print('1',b2())#这个通过返回值去调用函数中的函数.与19行中一个意思.
# b1()()
print("----------------------f1--------------------------")
#
from functools import wraps
def d1(func):

	print("aaaa")
	# func(*args, **kwargs) #这里就不能执行参数了!
	@wraps(func)#这个位置要放在使用这个函数的外函数
	def d2(*args): #这里还是可以接收参数的
		print("begin",func.__name__)
		func(*args)
		print("end")
	return d2
@d1
def f(a="aaaaa"):
	print("this is  a function")
	print(a)
	pass
# d1(f)()# 在如上d2定义了函数,并且在同级中定义了返回该函数,就相当于使用@d1,即@d1=d1(f)()
f("bbbbbbbbbbbbbbbbbbbbbbb")


print("-----------------------f2--------------------------")
def args(*args):
	print(*args)
	print(args[0])
args('1','2','3')


print("----------------------f3-重点-------------------------")
#装修器的重点思路:使用装饰器下的函数,看为子函数,装饰器定义的函数定义为父函数.子函数会作为参数传送到母函数
#				在母函数中按顺序执行相关语句.子函数的参数可以通过母函数传送.
def ff(vv="aaaaa"):
	def d1(func):
		print("aaaa")
		func(vv)
		def d2():
			print("begin")
			func(vv)
			print("end")
		return d2
	return d1

@ff(vv="bbb") #执行
def fv(xx="ddddddd"):
	print(xx)
fv()

print("----------------------f4--------------------------")
def f4(a="f4"):
	print("begin")
	return f4
a=f4("222") #这个执行是不受表达式影响的,即有括号就执行了

print("----------------------f5--------------------------")
from functools import wraps
def logit(logfile='out.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			func() #这个是增加完善的,不添加这个东西体现不出执行了.
			log_string = func.__name__ + " was called"
			print(log_string)
# 打开logfile，并写⼊内容
			with open(logfile, 'a') as opened_file:
# 现在将⽇志打到指定的logfile
				opened_file.write(log_string + '\n')
		return wrapped_function
	return logging_decorator
@logit()
def myfunc1():
	print("aiiw")
myfunc1()

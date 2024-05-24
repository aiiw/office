# # generator version
# def fibon(n):
# 	a = b = 1
# 	for i in range(n):
# 		yield a
# 		a, b = b, a + b
# #Now we can use it like this:
# for x in fibon(10000000):
# 	print(x)


# def fibon(n):
# 	a = b = 1
# 	result = []
# 	for i in range(n):
# 		result.append(a)
# 		a, b = b, a + b
# 	return result

# fibon(10000000)


# my_string = "Yasoob"
# my_iter = iter(my_string)
# print(next(my_iter))
# print(next(my_iter))

# print(next(my_iter))

# print(next(my_iter))


# def multiply(x):
# 	return (x*x)
# def add(x):
# 	return (x+x)
# funcs = [multiply, add]
# for i in range(5):
# 		value = list(map(lambda x: x(i), funcs))
# 		print(value)


# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for value in some_list:
# 	if some_list.count(value) > 1:
# 		if value not in duplicates:
# 			duplicates.append(value)
# 			print(duplicates)
# ### 输出: ['b', 'n']

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = set([x for x in some_list if some_list.count(x) > 1])
# print(duplicates)
# ### 输出: set(['b', 'n'])

# def hi(name="yasoob"):
# 	return "hi " + name
# print(hi())
# # output: 'hi yasoob'
# # 我们甚⾄可以将⼀个函数赋值给⼀个变量，⽐如
# greet = hi
# # 我们这⾥没有在使⽤⼩括号，因为我们并不是在调⽤hi函数
# # ⽽是在将它放在greet变量⾥头。我们尝试运⾏下这个
# print(greet())
# # output: 'hi yasoob'
# # 如果我们删掉旧的hi函数，看看会发⽣什么！
# del hi
# # print(hi())
# #outputs: NameError
# print(greet())
# #outputs: 'hi yasoob'
# 方式一:没有wraps
######如下为解释器
def a_new_decorator(a_func):#这个相当是模板
	def wrapTheFunction():
		print("I am doing some boring work before executing a_func()")
		a_func()
		print("I am doing some boring work after executing a_func()")
	return wrapTheFunction

def a_function_requiring_decoration():
	print("I am the function which needs some decoration to remov")
a_new_decorator(a_function_requiring_decoration)()
print("*"*50)
@a_new_decorator
def a_function_requiring_decoration():
	print("I am the function which needs some decoration to remove my foul smell")
a_function_requiring_decoration()
print("*"*50)
print("*"*50)
print("*"*50)
print(a_function_requiring_decoration.__name__)##这里有个注意点,加上修饰符后,被修饰的函数的名称,变为wrapTheFunction
# 方式二:有wraps
from functools import wraps
######如下为解释器
def a_new_decorator(a_func):
	@wraps(a_func)
	def wrapTheFunction():
		print("I am doing some boring work before executing a_func()")
		a_func()
		print("I am doing some boring work after executing a_func()")
	return wrapTheFunction

def a_function_requiring_decoration():
	print("I am the function which needs some decoration to remov")

@a_new_decorator
def a_function_requiring_decoration():
	print("I am the function which needs some decoration to remove my foul smell")
a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)##这里有个注意点,加上修饰符后,被修饰的函数的名称,变为wrapTheFunction


print("*"*150)
print("日志例子")
# ⽇志是装饰器运⽤的另⼀个亮点。这是个例⼦：
print("*"*150)
from functools import wraps
def logit(logfile='out.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + " was called--aiiw"
			print(log_string)
# 打开logfile，并写⼊内容
			with open(logfile, 'a') as opened_file:
# 现在将⽇志打到指定的logfile
				opened_file.write(log_string + '\n')
		return wrapped_function
	return logging_decorator
@logit()
def myfunc1():
	pass
myfunc1()

@logit(logfile='out1.log')
def aiiw():
	pass
aiiw()

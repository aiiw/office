from functools import wraps
def super(fn):
	@wraps(fn)
	def w():
		fn()
		print("这个是上级节点")
		def two():
			print("tow")
		two()
		fn()
	return w
@super
def node1():
	print("这个是子节点")

print("node1:",node1.__name__)

node1()

print("=========================封装下=================================================")

from functools import wraps
def super0(a='1'):
	def super1(fn):
		@wraps(fn)
		def w():
			print(a)
			fn()
			print("这个是上级节点")
			def two():
				print("tow")
			two()
			fn()
		w()
	return super1
@super0(a='456')
def node2():
	print("这个是子节点")

print("=========================用类作装饰器=================================================")


class logit(object):
	def __init__(self, logfile='out.log'):
		self.logfile = logfile
	def __call__(self, func):
		log_string = func.__name__ + " was called"
		print(log_string)
		# 打开logfile并写⼊
		with open(self.logfile, 'a') as opened_file:
		# 现在将⽇志打到指定的⽂件
			opened_file.write(log_string + '\n')
		# 现在，发送⼀个通知
		self.notify()
	def notify(self):
	# logit只打⽇志，不做别的
		pass

@logit()
def myfunc1():
	pass

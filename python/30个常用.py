import os
# 1 列出当前目录文件
a=[d+"a" for d in os.listdir('.') ] #列出指定目录
print(a)
print("##################################2#######################################")
#2 递归算法
def abc(n):
	if n<=1:
		return 1
	else:
		return abc(n-1)*n  
		# 假设N为4,第一次:abc(3)*4,第二次abc(2)*3,第三次abc(1)*2 ======1X2X3X4
print(abc(4))
# 3自己测试
print("##################################3#######################################")
def dd(n):
	for i in range(1,n):
		return i
print(dd(3))
# 测试结果,调用一次只返回一个结果
print("##################################4#######################################")
#4 带有yield的生成器
print("4 带有yield的生成器")
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))


def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(3):
    print(n)
print("##################################5#######################################")
# 5 map及lambda函数
print("5 map及lambda函数")
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)
# 5通过过滤器生成列表
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# 6 统计重复的数据
print("##################################6#######################################")
some_list = ['a', 'a', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) == 1])
print(duplicates)
#7返回多个值,其实就是返回一个元组
def profile():
 name = "Danny"
 age = 30
 return name, age
aa=profile()
print(aa)
print("##################################6#######################################")
# 8生成器补充
print("8生成器补充")
def fibon(n):
 a =0
 b = 1
 for i in range(n):
  a=a+b
  yield a

# 其实很简单， a, b = b, a+b 这个表达式的意思就是说，先计算=号的右边b的值，a+b的值，

for x in fibon(10):
 print(x)
print("##################################6#######################################")
 #9这是一种将字典转为列表的方式
list=[]
data = {
    '中国':'北京',
    '韩国':'首尔',
    '日本':'东京',
    '泰国':'曼谷',
    '马来西亚':'吉隆坡',
    '越南':'河内',
    '朝鲜':'平壤',
    '印度':'新德里'
    }

for item in data:
    list.append([item,data.get("%s"%(item)),"aaa"])
print(list)
list1=[]
for key,value in data.items():  
    list1.append([key,value,"aaa"])
print(list1)



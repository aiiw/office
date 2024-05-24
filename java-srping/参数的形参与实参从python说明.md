list=[]
for i in range(1,10):
	a=i
	list.append(i)
print(list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9] //添加不是变量本身,而是字面量

a={}
list1=[]
for i in range(1,10):
	a["aiiw"]=i
	print(a)
	list1.append(a)
print(list1)

# {'aiiw': 1}
# {'aiiw': 2}
# {'aiiw': 3}
# {'aiiw': 4}
# {'aiiw': 5}
# {'aiiw': 6}
# {'aiiw': 7}
# {'aiiw': 8}
# {'aiiw': 9}
# [{'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}, {'aiiw': 9}]添加的是引用地址即是变量本身

list2=[]
for i in range(1,10):
	a={}
	a["aiiw"]=i
	print(a)
	list2.append(a)
print(list2)
# [{'aiiw': 1}, {'aiiw': 2}, {'aiiw': 3}, {'aiiw': 4}, {'aiiw': 5}, {'aiiw': 6}, {'aiiw': 7}, {'aiiw': 8}, {'aiiw': 9}]
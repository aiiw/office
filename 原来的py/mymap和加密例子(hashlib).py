import hashlib
def square(x):
    return x ** 2
 
a=map(square,[1,2,3,4,5])#map返回的是生成器,list会将生成器转换为列表
print(type(a))
print(list(a))

list1=['1236473411', '1618967351', 'alidongxing']

sha1 = hashlib.sha1()

gen=map(sha1.update, list1)
print(type(gen))

print(sha1.hexdigest())

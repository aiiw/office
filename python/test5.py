import numpy as np 
# a = np.array([1,  2,  3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], ndmin =  3) 


# print (a) #创建np对象 numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# print(type(a)) #实质为numpy.ndarray
# print(a.ndim,a.shape,a.size)  
# print("===================")
# b = a.reshape(2,4,3)  # b 现在拥有三个维度
# print (b) #创建np对象 numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# print(type(b)) #实质为numpy.ndarray
# print(b.ndim,b.shape,b.size)  

# b = a.reshape(1,4,6)  # b 现在拥有三个维度
# print (b) #创建np对象 numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# print(type(b)) #实质为numpy.ndarray
# print(b.ndim,b.shape,b.size)  
data=np.random.randint(1,36,6)
import random
list = [20, 16, 10, 5]
data=random.shuffle(list)
print(data)
#[5, 20, 10, 16]
import keyring
password=keyring.get_password('public01','test')
print(password)


a={}
a["a"]=1
a["b"]=2
print(str(a))
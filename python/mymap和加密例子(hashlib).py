import hashlib
def square(x):
    return x ** 2
 
a=map(square,[1,2,3,4,5])#map返回的是生成器,list会将生成器转换为列表
print(type(a))
print(list(a))

list1=['1236473411', '1618967351', 'alidongxing']

sha1 = hashlib.sha1()
sha256 =hashlib.sha256()
gen=map(sha1.update, list1)
print(type(gen))
print(gen)
# 使用十六进表示
print(sha1.hexdigest()) 

#如下三种方式,其实是一样的.

# 除了 SHA-256，hashlib 模块还提供了其他常见的哈希算法，如 MD5、SHA-1、SHA-512 等

data = b'Helloworld!'  # 要计算哈希的数据，必须是字节串
sha1 = hashlib.sha1()
sha1.update(data)
digest = sha1.digest()  # 获取二进制表示的哈希值
hexdigest = sha1.hexdigest()  # 获取十六进制表示的哈希值
print(digest)
print(hexdigest)


data_list = [b'Hello', b'world!']  # 要计算哈希的数据列表，必须是字节串
sha1 = hashlib.sha1()

# 使用 map 函数进行连续的哈希计算
gen = map(sha1.update, data_list)
list(gen)

digest1 = sha1.digest()  # 获取二进制表示的哈希值
hexdigest1 = sha1.hexdigest()  # 获取十六进制表示的哈希值

print(digest1)
print(hexdigest1)


sha1 = hashlib.sha1()

# 分块进行哈希计算
data_chunk1 = b'Hello'
data_chunk2 = b'world!'
sha1.update(data_chunk1)
sha1.update(data_chunk2)

digest2 = sha1.digest()  # 获取二进制表示的哈希值
hexdigest2 = sha1.hexdigest()  # 获取十六进制表示的哈希值

print(digest2)
print(hexdigest2)
import redis
r=redis.Redis(host='192.168.0.7',port='6379')
print(r.get('a'))
str1='aiiw'
# for a in range(1,200):
# 	str1=str1+str(a)
# 	client.set(a, 'a')
# client.set('aa','bb')
print(r.keys())

r.incr('aiiw',amount='100') #具体来说，r.incr 方法用于在 Redis 中对指定键名对应的值进行自增操作。如果指定的键名不存在，则会创建一个新的键，并将其值初始化为 0；
r.hmset("hash2", {"k21": "v2", "k3": "v3"}) #r.hmset 是 Redis 客户端库中的一个方法，用于将多个字段-值对一次性地设置到 Redis 哈希表中。
## 获取哈希表的值
# result = r.hgetall('myhash')
for name in r.keys():
    print(name,':',r.type(name))

#具体来说，r.lpush 方法用于在 Redis 中将一个或多个值插入到指定列表的头部。它接受两个参数：列表的键名和一个或多个要插入的值。
r.lpush("list1", 11, 22, 33)
#具体来说，r.lrange 方法用于从 Redis 列表中获取指定范围内的元素值。它接受两个参数：列表的键名和起始索引与结束索引（包含在内）。
#返回的是一个包含指定范围内元素值的列表。
#方法的第一个参数是列表的键名，第二个参数是起始索引（从 0 开始），
#第三个参数是结束索引（-1 表示获取到最后一个元素）。返回的 result 是一个包含指定范围内元素值的列表。
print(r.lrange('list1', 0, -1))

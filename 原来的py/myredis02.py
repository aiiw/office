import redis
r=redis.Redis(host='192.168.0.7',port='6379')
print(r.get('a'))
str1='aiiw'
# for a in range(1,200):
# 	str1=str1+str(a)
# 	client.set(a, 'a')
# client.set('aa','bb')
print(r.keys())

r.incr('aiiw',amount='100')
r.hmset("hash2", {"k21": "v2", "k3": "v3"})
for name in r.keys():
    print(name,':',r.type(name))


r.lpush("list1", 11, 22, 33)
print(r.lrange('list1', 0, -1))

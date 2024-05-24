import redis

# 创建 Redis 连接，并进行身份验证
r = redis.Redis(host='192.168.0.101', port=6399, password='myoa888')
r.select(1)
#一直是失败
import redis, json
from elasticsearch import Elasticsearch

# Connect to Redis
r = redis.Redis(host='192.168.0.101', port=6399, db=0)

# Connect to Elasticsearch
es = Elasticsearch()

# Iterate over all keys in Redis and index them in Elasticsearch
for key in r.scan_iter():
    value = r.get(key)
    doc = {"key": key.decode(), "value": value.decode()}
    es.index(index="myindex", body=json.dumps(doc))
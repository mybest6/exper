# #encoding:utf-8
import redis
rds = redis.Redis(db=18,password='fs2017',host='192.168.100.209')
print([i for i in rds.keys()])
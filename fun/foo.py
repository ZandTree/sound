import redis

print("starting?")
redis_client = redis.Redis(host="localhost",port=6379,db=0)

# can contain till 16 st, here =0
#print(redis_client) # Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>

redis_client.set(name='tata',value='here',ex=10)

redis_client.set(name='zoo',value='here',ex=60)

print(str(redis_client.get(name='zoo')))

# output in bytes|=> int
print(int(redis_client.ttl('zoo')))

# to close connection |=> .close()
redis_client.close()
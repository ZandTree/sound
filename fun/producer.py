import redis


# set 0 => 0 == string
with redis.Redis() as redis_client:
    redis_client.set('count',0)





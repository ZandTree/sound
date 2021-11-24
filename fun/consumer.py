import redis
import time

with redis.Redis() as redis_client:
    for _ in range(5):
        time.sleep(2)
        redis_client.incr('count',2)
        print(int(redis_client.get('count')))
    redis_client.delete('count')
    print(redis_client.get('count'))


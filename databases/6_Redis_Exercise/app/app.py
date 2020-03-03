import redis


REDIS_HOST = 'redis'

r = redis.Redis(REDIS_HOST)
r.mset({"default": "Hello World from Redis"})
print(r.get("default"))


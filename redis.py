import redis
from dotenv import load_dotenv
config = load_dotenv('.env')

r = redis.Redis(
    host= config["REDIS_HOST"],
    port= config["REDIS_PORT"],
    password= config["REDIS_PASS"],)


def redis_set(key, value):
    res = r.set(key, value)
    return res

def redis_get(key):
    res = r.get(key)
    return res

def redis_del(key):
    res = r.delete(key)
    return res
import redis

_instance: redis.Redis

def connect(host='localhost', port=6379):
    global _instance
    _instance = redis.Redis(host=host, port=port, decode_responses=True)
    _instance.ping()
    return _instance

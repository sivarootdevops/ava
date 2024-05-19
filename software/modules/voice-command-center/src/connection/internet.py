import time
from urllib import request

import operators.notifier as notifier
from enums.redis import StateKeyEnum, StatusEnum
from redis import Redis


def _check_internet_connection(redis: Redis):
    try:
        request.urlopen('https://8.8.8.8', timeout=2.5)
        if (redis.get(StateKeyEnum.INTERNET_STATUS) == StatusEnum.OFFLINE):
            notifier.notify("I'm back")
        redis.set(StateKeyEnum.INTERNET_STATUS, StatusEnum.ONLINE)
        return
    except Exception:
        pass
    if (redis.get(StateKeyEnum.INTERNET_STATUS) == StatusEnum.ONLINE):
        notifier.notify_from_mp3("assets/audio/connection-loss.mp3")
    redis.set(StateKeyEnum.INTERNET_STATUS, StatusEnum.OFFLINE)

def start(redis: Redis):
    def infinite_loop():
        while True:
            _check_internet_connection(redis)
            time.sleep(3)

    return infinite_loop
    
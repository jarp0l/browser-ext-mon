import os

import redis

DRAGONFLY_HOST = os.getenv("DRAGONFLY_HOST", "localhost")
DRAGONFLY_PORT = os.getenv("DRAGONFLY_PORT", 6379)


def init_dragonfly():
    return redis.Redis(host=DRAGONFLY_HOST, port=DRAGONFLY_PORT, decode_responses=True)


dragonfly = init_dragonfly()

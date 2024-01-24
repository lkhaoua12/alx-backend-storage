#!/usr/bin/env python3
"""
create a cach class and insert data with key
"""
from typing import Union
import redis
import uuid


class Cache():
    """ create a cach class and insert data with key """

    def __init__(self):
        """ initiate the new instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data and returns key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

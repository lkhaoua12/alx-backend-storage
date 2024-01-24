#!/usr/bin/env python3
"""
create a cach class and insert data with key
"""
from typing import Callable, Union
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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """ store data and returns key """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """ get string """
        return self.get(key, fn = lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> int:
        """ get int """
        return self.get(key, fn = int)
    


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
            b"foo": None,
            123: int,
            "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

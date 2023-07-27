#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        '''Initializes a Cache instance.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Returns a key string of stored data
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Tracks the number of calls made to a method in a Cache class.
    '''
    @wraps(method)
    def wrapped(self, *args, **kwargs) -> Any:
        # Get the qualified name of the method using __qualname__
        '''Invokes the given method after incrementing its call counter.
        '''

        if isinstance(self._redis, redis.Redis):
            # Increment the count for the method name in Redis
            self._redis.incr(method.__qualname__)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    return wrapped


class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        '''Initializes a Cache instance.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Returns a key string of stored data
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        '''Retrieves an int value from a Redis data storage.
        '''
        return self.get(key, int)

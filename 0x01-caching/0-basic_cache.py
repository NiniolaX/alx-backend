#!/usr/bin/env python3
"""
Contains a BasicCache class.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def __init__(self):
        """ Initializes a BasicCache instance """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if not key:
            return
        return self.cache_data.get(key)

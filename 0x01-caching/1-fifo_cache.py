#!/usr/bin/env python3
"""
Contains a a class FIFOCache that implements the FIFO Cache replacement
policy.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """
    def __init__(self):
        """ Initializes a FIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Inserts a new item into the cache """
        if not key or not item:
            return

        self.cache_data[key] = item

        # If cache is full, free cache by FIFO
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            first_key_inserted = next(iter(self.cache_data))
            self.cache_data.pop(first_key_inserted)
            print(f"DISCARD: {first_key_inserted}")

    def get(self, key):
        """ Retrieves an item from cache """
        if not key:
            return
        return self.cache_data.get(key)

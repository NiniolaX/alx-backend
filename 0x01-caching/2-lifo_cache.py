#!/usr/bin/env python3
"""
Contains a a class LIFOCache that implements the LIFO Cache replacement
policy.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """
    def __init__(self):
        """ Initializes a LIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Inserts a new item into the cache """
        if not key or not item:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        # If cache is full, free cache by LIFO replacement policy
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            last_key_inserted, last_item_inserted = self.cache_data.popitem()
            print(f"DISCARD: {last_key_inserted}")

        # Insert new item after deletion
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from cache """
        if not key:
            return
        return self.cache_data.get(key)

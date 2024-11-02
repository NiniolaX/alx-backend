#!/usr/bin/env python3
"""
Contains a a class LRUCache that implements the LRU Cache replacement policy.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Cache
    """
    def __init__(self):
        """ Initializes the LRUCache instance """
        super().__init__()

    def put(self, key, item):
        """ Inserts a new item into the cache """
        if not key or not item:
            return

        # Update key to most recently used
        if key in self.cache_data:
            del self.cache_data[key]

        # If cache is full, delete Least Recently Used item
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            self.cache_data.pop(lru_key)
            print(f"DISCARD: {lru_key}")

        # Insert new item after deletion
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if not key:
            return

        # Update key to most recently used
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item

        return self.cache_data.get(key)

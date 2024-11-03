#!/usr/bin/env python3
"""
Contains a a class MRUCache that implements the MRU Cache replacement policy.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Cache
    """
    def __init__(self):
        """ Initializes the MRUCache instance """
        super().__init__()

    def put(self, key, item):
        """ Inserts a new item into the cache """
        if not key or not item:
            return

        # Upon cache hit, update key to most recently used
        if key in self.cache_data:
            del self.cache_data[key]

        # If cache is full, delete Most Recently Used item
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            mru_key, mru_item = self.cache_data.popitem()  # Last item
            print(f'DISCARD: {mru_key}')

        # Insert new item into cache
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

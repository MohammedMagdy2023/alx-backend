#!/usr/bin/env python3
"""
    Basic dictionary caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        The caching class
    """
    def __init__(self):
        """The init method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """insert into cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > self.MAX_ITEMS:
            poped, _ = self.cache_data.popitem()
            print(f"DISCARD: {poped}")
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the cached data"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key, None)

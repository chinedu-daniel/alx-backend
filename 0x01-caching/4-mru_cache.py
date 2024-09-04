#!/usr/bin/env python3
"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Basic Dictionary
    """

    def __init__(self):
        """INIT"""
        super().__init__()
        self.current = None

    def put(self, key, items):
        """
        check if the key and item are none or not
        """
        if key is None or items is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = items
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.current)
            print(f"DISCARD: {self.current}")

        self.current = key
        self.cache_data[key] = items

    def get(self, key):
        """
        check if key is none or not and exists in cache_dataa
        """
        if key is None:
            return

        if key is self.cache_data:
            self.current = key
            return self.cache_data[key]

        return None

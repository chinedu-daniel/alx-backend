#!/usr/bin/env python3
"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Basic Dictionary
    """

    def __init__(self):
        """INIT"""
        super().__init__()

    def put(self, key, items):
        """
        check if the key and item are none or not
        """
        if key is None or items is None:
            return

        if key in self.cache:
            self.current.remove.(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            item = self.current.pop()
            self.cache_data.pop(item)
            print(f"DISCARD: {item}")

        self.current.insert(0, key)
        self.cache_data[key] = items

    def get(self, key):
        """
        check if key is none or not and exists in cache_dataa
        """
        if key is None:
            return
        value = self.cache_data.get(key, None)
        if value is None:
            return

        return value

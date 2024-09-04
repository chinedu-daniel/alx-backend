#!/usr/bin/env python3
"""
Basic dictionary
"""

BaseCaching = __import__('fifo_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Basic Dictionary
    """

    def __init__(self):
        """INIT"""
        super().__init__()
        self.order = []

    def put(self, key, items):
        """
        check if the key and item are none or not
        """
        if key is None or items is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)

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

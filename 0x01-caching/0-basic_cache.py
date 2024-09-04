#!/usr/bin/env python3
"""
Basic dictionary
"""


class BasicCache(BaseCaching):
    """
    Basic Dictionary
    """

    def put(self, key, item):
        """
        check if the key and item are none or not
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        check if key is none or not and exists in cache_dataa
        """
        if key is None or key not in self.cache_data:
            return None
        return seelf.cache_data[key]

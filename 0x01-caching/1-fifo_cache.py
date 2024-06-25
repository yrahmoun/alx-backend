#!/usr/bin/python3
""" module for task 1 """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ An implementation of FIFO(First In Fisrt Out) Cach """

    def __init__(self):
        """ initialization """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

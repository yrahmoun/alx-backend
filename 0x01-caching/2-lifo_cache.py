#!/usr/bin/python3
""" module for task 2 """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ implementation of LIFO(Last In Fisrt Out) Cache """

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
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

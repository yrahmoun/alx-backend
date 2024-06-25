#!/usr/bin/python3
""" module for task 3"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ implementation of LRU(Last Recently Used) Cache """

    def __init__(self):
        """ initialization """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None

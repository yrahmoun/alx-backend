#!/usr/bin/python3
""" module for task 0 """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic cache implementaion class"""
    def put(self, key, item):
        """ Adds an item in the cache """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Gets an item by key """
        return self.cache_data.get(key, None)

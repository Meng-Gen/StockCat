#-*- coding: utf-8 -*-

from stockcat.feed_cache.file_storage import FileStorage

class Storage():
    def __init__(self):
        self.impl = FileStorage()

    def set(self, feed_name, url):
        self.impl.set(feed_name, url)


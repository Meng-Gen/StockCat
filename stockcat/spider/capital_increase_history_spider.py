#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class CapitalIncreaseHistorySpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()

    def crawl(self, param):
        url = self.build_url(param)
        key = self.build_key(param)
        self.storage.set(key, url)
        
    def is_crawled(self, param):
        key = self.build_key(param)
        return self.storage.contains(key)

    def get_crawled(self, param):
        key = self.build_key(param)
        return self.storage.get(key)

    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcb/zcb_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''capital_increase_history/%s''' % (param['stock_symbol'])
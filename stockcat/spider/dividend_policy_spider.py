#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class DividendPolicySpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()

    def crawl(self, stock_symbol):
        params = self.__parse_params(stock_symbol)
        url = self.__build_url(params)
        key = self.__build_key(params)
        self.storage.set(key, url)
        
    def is_crawled(self, stock_symbol):
        params = self.__parse_params(stock_symbol)
        key = self.__build_key(params)
        return self.storage.contains(key)

    def get_crawled(self, stock_symbol):
        params = self.__parse_params(stock_symbol)
        key = self.__build_key(params)
        return self.storage.get(key)
        
    def __parse_params(self, stock_symbol):
        return {
            'stock_symbol' : stock_symbol,
        }

    def __build_url(self, params):
        return '''http://jdata.yuanta.com.tw/z/zc/zcc/zcc_%s.djhtm''' % (params['stock_symbol'])

    def __build_key(self, params):
        return '''dividend_policy/%s''' % (params['stock_symbol'])
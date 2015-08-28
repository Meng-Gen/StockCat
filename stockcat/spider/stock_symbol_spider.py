#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage

class StockSymbolSpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.key = {
            'stock_exchange_market' : 'stock_symbol/stock_exchange_market',
            'otc_market' : 'stock_symbol/otc_market',
        }
        self.url = {
            'stock_exchange_market' : 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',
            'otc_market' : 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=4',
        }

    def crawl(self, param):
        key = self.key[param['market_type']]
        url = self.url[param['market_type']]
        self.storage.set(key, url)

    def is_crawled(self, param):
        key = self.key[param['market_type']]
        return self.storage.contains(key)

    def get_crawled(self, param):
        key = self.key[param['market_type']]
        return self.storage.get(key)

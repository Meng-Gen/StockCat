#-*- coding: utf-8 -*-

from stockcat.feed_cache.storage import Storage

class StockSymbolFeedCache():
    def __init__(self):
        self.storage = Storage()
        
    def set_stock_exchange_market(self):
        feed_name = "stock_symbol.stock_exchange_market"
        url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
        self.storage.set(feed_name, url)

    def set_otc_market(self):
        feed_name = "stock_symbol.otc_market"
        url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=4"
        self.storage.set(feed_name, url)

#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class StockSymbolSpider(Spider):
    def build_url(self, param):
        return '''http://isin.twse.com.tw/isin/C_public.jsp?strMode=%s''' \
                % (param['market_mode'])

    def build_key(self, param):
        return '''stock_symbol/%s''' \
                % (param['market_type'])

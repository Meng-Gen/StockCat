#-*- coding: utf-8 -*-

from stockcat.spider.stock_symbol_spider import StockSymbolSpider

import unittest

class StockSymbolSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = StockSymbolSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_stock_exchange_market(self):
        param = { 'market_type' : 'stock_exchange_market' }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

    def test_crawl_otc_market(self):
        param = { 'market_type' :  'otc_market' }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

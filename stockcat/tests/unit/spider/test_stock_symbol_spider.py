#-*- coding: utf-8 -*-

from stockcat.spider.stock_symbol_spider import StockSymbolSpider

import unittest

class StockSymbolSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = StockSymbolSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl(self):
        market_type = 'stock_exchange_market'
        self.spider.crawl(market_type)
        self.assertTrue(self.spider.is_crawled(market_type))

        market_type = 'otc_market'
        self.spider.crawl(market_type)
        self.assertTrue(self.spider.is_crawled(market_type))

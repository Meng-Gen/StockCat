#-*- coding: utf-8 -*-

from stockcat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider

import unittest

class CapitalIncreaseHistorySpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = CapitalIncreaseHistorySpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2498(self):
        param = { 'stock_symbol' : '2498' }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

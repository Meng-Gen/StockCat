#-*- coding: utf-8 -*-

from stockcat.spider.cash_flow_spider import CashFlowSpider

import datetime
import unittest

class CashFlowSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = CashFlowSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2330_in_2010Q3(self):
        param = { 'stock_symbol' : '2330', 'date' : datetime.date(2010, 9, 30) }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

    def test_crawl_2330_in_2014Q3(self):
        param = { 'stock_symbol' : '2330', 'date' : datetime.date(2014, 9, 30) }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

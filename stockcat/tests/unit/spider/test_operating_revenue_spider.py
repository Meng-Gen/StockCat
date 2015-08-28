#-*- coding: utf-8 -*-

from stockcat.spider.operating_revenue_spider import OperatingRevenueSpider

import datetime
import unittest

class OperatingRevenueSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = OperatingRevenueSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2330_in_2010(self):
        param = { 'stock_symbol' : '2330', 'date' : datetime.date(2010, 9, 30) }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

    def test_crawl_2330_in_2014(self):
        param = { 'stock_symbol' : '2330', 'date' : datetime.date(2010, 9, 30) }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

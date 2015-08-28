#-*- coding: utf-8 -*-

from stockcat.spider.operating_revenue_summary_spider import OperatingRevenueSummarySpider

import datetime
import unittest

class OperatingRevenueSummarySpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = OperatingRevenueSummarySpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_stock_exchange_market(self):
        param = { 'market_type' : 'stock_exchange_market', 'date' : datetime.date(2014, 9, 30) }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

    def test_crawl_otc_market(self):
        param = { 'market_type' : 'otc_market', 'date' : datetime.date(2014, 9, 30) }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))

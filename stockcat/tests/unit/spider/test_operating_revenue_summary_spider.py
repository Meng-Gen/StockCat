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
        self.spider.crawl('stock_exchange_market', datetime.date(2014, 9, 30))
        self.assertTrue(self.spider.is_crawled('stock_exchange_market', datetime.date(2014, 9, 30)))

    def test_crawl_otc_market(self):
        self.spider.crawl('otc_market', datetime.date(2014, 9, 30))
        self.assertTrue(self.spider.is_crawled('otc_market', datetime.date(2014, 9, 30)))

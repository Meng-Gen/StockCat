#-*- coding: utf-8 -*-

from stockcat.spider.xbrl_financial_statement_spider import XbrlFinancialStatementSpider

import datetime
import unittest

class XbrlFinancialStatementSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = XbrlFinancialStatementSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl(self):
        self.spider.crawl("2330", datetime.date(2010, 9, 30))
        self.assertFalse(self.spider.is_crawled("2330", datetime.date(2010, 9, 30)))

        self.spider.crawl("2330", datetime.date(2014, 9, 30))
        self.assertTrue(self.spider.is_crawled("2330", datetime.date(2014, 9, 30)))

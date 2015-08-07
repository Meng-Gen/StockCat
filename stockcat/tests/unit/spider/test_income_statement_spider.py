#-*- coding: utf-8 -*-

from stockcat.spider.income_statement_spider import IncomeStatementSpider

import datetime
import unittest

class IncomeStatementSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = IncomeStatementSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2330(self):
        self.spider.crawl("2330", datetime.date(2010, 9, 30))
        self.assertTrue(self.spider.is_crawled("2330", datetime.date(2010, 9, 30)))

        self.spider.crawl("2330", datetime.date(2014, 9, 30))
        self.assertTrue(self.spider.is_crawled("2330", datetime.date(2014, 9, 30)))

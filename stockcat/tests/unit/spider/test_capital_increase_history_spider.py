#-*- coding: utf-8 -*-

from stockcat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider

import unittest

class CapitalIncreaseHistorySpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = CapitalIncreaseHistorySpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2498(self):
        self.spider.crawl('2498')
        self.assertTrue(self.spider.is_crawled('2498'))

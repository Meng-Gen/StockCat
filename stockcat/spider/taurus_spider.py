#-*- coding: utf-8 -*-

import datetime

class TaurusSpider():
    def __init__(self):
        self.ifrs_spider = None
        self.legacy_spider = None

    def crawl(self, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.ifrs_spider.crawl(stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_spider.crawl(stock_symbol, date)

    def is_crawled(self, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.ifrs_spider.is_crawled(stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_spider.is_crawled(stock_symbol, date)

    def get_crawled(self, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.ifrs_spider.get_crawled(stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_spider.get_crawled(stock_symbol, date)

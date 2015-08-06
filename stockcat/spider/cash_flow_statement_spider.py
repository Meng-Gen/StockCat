#-*- coding: utf-8 -*-

from stockcat.spider.ifrs.ifrs_cash_flow_statement_spider import IfrsCashFlowStatementSpider
from stockcat.spider.legacy.legacy_cash_flow_statement_spider import LegacyCashFlowStatementSpider

import datetime

class CashFlowStatementSpider():
    def __init__(self):
        self.ifrs_spider = IfrsCashFlowStatementSpider()
        self.legacy_spider = LegacyCashFlowStatementSpider()

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

#-*- coding: utf-8 -*-

from stockcat.feed.ifrs_financial_statement_feed import IfrsFinancialStatementFeed

import datetime

class FinancialStatementFeed():
    def __init__(self, stock_symbol, date, is_consolidated):
        self.feed_impl = self.__init_feed_impl(stock_symbol, date, is_consolidated)

    def get(self):
        return self.feed_impl.get()

    def __init_feed_impl(self, stock_symbol, date, is_consolidated):
        print date
        if date >= datetime.date(2013, 1, 1):
            return IfrsFinancialStatementFeed(stock_symbol, date, is_consolidated)

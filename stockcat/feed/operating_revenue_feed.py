#-*- coding: utf-8 -*-

from stockcat.feed.ifrs_operating_revenue_feed import IfrsOperatingRevenueFeed
from stockcat.feed.legacy_operating_revenue_feed import LegacyOperatingRevenueFeed

import datetime

class OperatingRevenueFeed():
    def __init__(self, stock_symbol, date):
        self.feed_impl = self.__init_feed_impl(stock_symbol, date)

    def get(self):
        return self.feed_impl.get()

    def __init_feed_impl(self, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return IfrsOperatingRevenueFeed(stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return LegacyOperatingRevenueFeed(stock_symbol, date)

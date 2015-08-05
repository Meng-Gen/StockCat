#-*- coding: utf-8 -*-

import datetime
import sys

def set_stock_symbol_feed_cache():
    from stockcat.feed_cache.stock_symbol_feed_cache import StockSymbolFeedCache
    cache = StockSymbolFeedCache()
    cache.set_stock_exchange_market()
    cache.set_otc_market()

def get_financial_statement():
    from stockcat.feed.financial_statement_feed import FinancialStatementFeed
    feed = FinancialStatementFeed("2330", datetime.date(2014, 9, 30), True)
    feed.get()

def get_operating_revenue():
    from stockcat.feed.operating_revenue_feed import OperatingRevenueFeed
    feed = OperatingRevenueFeed("2330", datetime.date(2010, 9, 30))
    feed.get()

def main():
    set_stock_symbol_feed_cache()
    #get_financial_statement()
    #get_operating_revenue()

if __name__ == '__main__':
    sys.exit(main())
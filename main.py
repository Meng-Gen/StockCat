#-*- coding: utf-8 -*-

from stockcat.feed.financial_statement_feed import FinancialStatementFeed
from stockcat.feed.stock_symbol_feed import StockSymbolFeed

import datetime
import sys

def main():
    feed = FinancialStatementFeed("2330", datetime.date(2014, 9, 30), True)
    feed.get()
    
    #feed = StockSymbolFeed()
    #feed.get()

if __name__ == '__main__':
    sys.exit(main())
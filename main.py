#-*- coding: utf-8 -*-

from financial_statement_feed import FinancialStatementFeed

import datetime
import sys

def main():
    feed = FinancialStatementFeed("2330", datetime.date(2014, 12, 31), True)
    feed.get()

if __name__ == '__main__':
    sys.exit(main())
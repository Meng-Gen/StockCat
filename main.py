#-*- coding: utf-8 -*-

import datetime
import sys

def crawl_stock_symbol():
    from stockcat.spider.stock_symbol_spider import StockSymbolSpider
    spider = StockSymbolSpider()
    spider.crawl("stock_exchange_market")
    spider.crawl("otc_market")

def crawl_operating_revenue():
    from stockcat.spider.operating_revenue_spider import OperatingRevenueSpider
    spider = OperatingRevenueSpider()
    spider.crawl("2330", datetime.date(2010, 9, 30))
    spider.crawl("2330", datetime.date(2014, 9, 30))

def get_financial_statement():
    from stockcat.feed.financial_statement_feed import FinancialStatementFeed
    feed = FinancialStatementFeed("2330", datetime.date(2014, 9, 30), True)
    feed.get()

def get_operating_revenue():
    from stockcat.feed.operating_revenue_feed import OperatingRevenueFeed
    feed = OperatingRevenueFeed("2330", datetime.date(2010, 9, 30))
    feed.get()

def main():
    #crawl_stock_symbol()
    crawl_operating_revenue()
    #get_financial_statement()
    #get_operating_revenue()

if __name__ == '__main__':
    sys.exit(main())
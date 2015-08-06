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

def crawl_cash_flow_statement():
    from stockcat.spider.cash_flow_statement_spider import CashFlowStatementSpider
    spider = CashFlowStatementSpider()
    spider.crawl("2330", datetime.date(2010, 9, 30))
    spider.crawl("2330", datetime.date(2014, 9, 30))

def main():
    #crawl_stock_symbol()
    #crawl_operating_revenue()
    crawl_cash_flow_statement()

if __name__ == '__main__':
    sys.exit(main())
#-*- coding: utf-8 -*-

from stockcat.spider.single_stock_spider import SingleStockSpider

import datetime

class XbrlFinancialStatementSpider(SingleStockSpider):
    def crawl(self, stock_symbol, date):
        if date >= datetime.date(2013, 1, 1):
            return SingleStockSpider.crawl(self, stock_symbol, date)

    def build_url(self, params):
        return '''http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=%s&SYEAR=%s&SSEASON=%s&REPORT_ID=C''' \
                % (params['stock_symbol'], params['roc_era'], params['season_xbrl'])

    def build_key(self, params):
        return '''xbrl_financial_statement/%s/%s/%s''' \
                % (params['stock_symbol'], params['year'], params['season'])

#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class XbrlFinancialStatementSpider(Spider):
    def build_url(self, param):
        return '''http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=%s&SYEAR=%s&SSEASON=%s&REPORT_ID=C''' \
                % (param['stock_symbol'], param['year'], param['quarter_xbrl'])

    def build_key(self, param):
        return '''xbrl_financial_statement/%s/%s/%s''' \
                % (param['stock_symbol'], param['year'], param['quarter'])

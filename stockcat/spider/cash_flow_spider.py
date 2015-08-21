#-*- coding: utf-8 -*-

from stockcat.spider.taurus_spider import TaurusSpider
from stockcat.spider.xbrl_financial_statement_spider import XbrlFinancialStatementSpider
from stockcat.spider.legacy.legacy_cash_flow_spider import LegacyCashFlowSpider

class CashFlowSpider(TaurusSpider):
    def __init__(self):
        TaurusSpider.__init__(self)        
        self.ifrs_spider = XbrlFinancialStatementSpider()
        self.legacy_spider = LegacyCashFlowSpider()

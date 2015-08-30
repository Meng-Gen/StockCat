#-*- coding: utf-8 -*-

from stockcat.spider.composite_spider import CompositeSpider
from stockcat.spider.xbrl_financial_statement_spider import XbrlFinancialStatementSpider
from stockcat.spider.legacy.legacy_cash_flow_spider import LegacyCashFlowSpider

class CashFlowSpider(CompositeSpider):
    def __init__(self):
        CompositeSpider.__init__(self)        
        self.ifrs_spider = XbrlFinancialStatementSpider()
        self.legacy_spider = LegacyCashFlowSpider()

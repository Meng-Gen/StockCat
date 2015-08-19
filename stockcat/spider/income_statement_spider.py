#-*- coding: utf-8 -*-

from stockcat.spider.taurus_spider import TaurusSpider
from stockcat.spider.ifrs.ifrs_income_statement_spider import IfrsIncomeStatementSpider
from stockcat.spider.legacy.legacy_income_statement_spider import LegacyIncomeStatementSpider

class IncomeStatementSpider(TaurusSpider):
    def __init__(self):
        self.ifrs_spider = IfrsIncomeStatementSpider()
        self.legacy_spider = LegacyIncomeStatementSpider()

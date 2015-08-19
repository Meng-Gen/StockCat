#-*- coding: utf-8 -*-

from stockcat.spider.taurus_spider import TaurusSpider
from stockcat.spider.ifrs.ifrs_balance_sheet_spider import IfrsBalanceSheetSpider
from stockcat.spider.legacy.legacy_balance_sheet_spider import LegacyBalanceSheetSpider

class BalanceSheetSpider(TaurusSpider):
    def __init__(self):
        TaurusSpider.__init__(self)
        self.ifrs_spider = IfrsBalanceSheetSpider()
        self.legacy_spider = LegacyBalanceSheetSpider()

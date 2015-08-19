#-*- coding: utf-8 -*-

from stockcat.pipeline.aries_pipeline import AriesPipeline
from stockcat.spider.balance_sheet_spider import BalanceSheetSpider
from stockcat.assembler.balance_sheet_assembler import BalanceSheetAssembler
from stockcat.feed.balance_sheet_feed import BalanceSheetFeedBuilder

class BalanceSheetPipeline(AriesPipeline):
    def __init__(self):
        AriesPipeline.__init__(self)
        self.spider = BalanceSheetSpider()
        self.assembler = BalanceSheetAssembler()
        self.feed_builder = BalanceSheetFeedBuilder()

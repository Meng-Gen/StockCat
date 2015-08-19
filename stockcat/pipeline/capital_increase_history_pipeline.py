#-*- coding: utf-8 -*-

from stockcat.pipeline.taurus_pipeline import TaurusPipeline
from stockcat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider
from stockcat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
from stockcat.feed.capital_increase_history_feed import CapitalIncreaseHistoryFeedBuilder

class CapitalIncreaseHistoryPipeline(TaurusPipeline):
    def __init__(self):
        TaurusPipeline.__init__(self)        
        self.spider = CapitalIncreaseHistorySpider()
        self.assembler = CapitalIncreaseHistoryAssembler()
        self.feed_builder = CapitalIncreaseHistoryFeedBuilder()

#-*- coding: utf-8 -*-

from stockcat.pipeline.aries_pipeline import AriesPipeline
from stockcat.spider.cash_flow_spider import CashFlowSpider
from stockcat.assembler.cash_flow_assembler import CashFlowAssembler
from stockcat.feed.cash_flow_feed import CashFlowFeedBuilder

class CashFlowPipeline(AriesPipeline):
    def __init__(self):
        AriesPipeline.__init__(self)
        self.spider = CashFlowSpider()
        self.assembler = CashFlowAssembler()
        self.feed_builder = CashFlowFeedBuilder()

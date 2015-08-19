#-*- coding: utf-8 -*-

from stockcat.pipeline.taurus_pipeline import TaurusPipeline
from stockcat.spider.dividend_policy_spider import DividendPolicySpider
from stockcat.assembler.dividend_policy_assembler import DividendPolicyAssembler
from stockcat.feed.dividend_policy_feed import DividendPolicyFeedBuilder

class DividendPolicyPipeline(TaurusPipeline):
    def __init__(self):
        TaurusPipeline.__init__(self)        
        self.spider = DividendPolicySpider()
        self.assembler = DividendPolicyAssembler()
        self.feed_builder = DividendPolicyFeedBuilder()

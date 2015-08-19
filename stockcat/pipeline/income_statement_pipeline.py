#-*- coding: utf-8 -*-

from stockcat.pipeline.aries_pipeline import AriesPipeline
from stockcat.spider.income_statement_spider import IncomeStatementSpider
from stockcat.assembler.income_statement_assembler import IncomeStatementAssembler
from stockcat.feed.income_statement_feed import IncomeStatementFeedBuilder

class IncomeStatementPipeline(AriesPipeline):
    def __init__(self):
        AriesPipeline.__init__(self)
        self.spider = IncomeStatementSpider()
        self.assembler = IncomeStatementAssembler()
        self.feed_builder = IncomeStatementFeedBuilder()

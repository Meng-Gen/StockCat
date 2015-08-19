#-*- coding: utf-8 -*-

from stockcat.feed.aries_feed import AriesFeed
from stockcat.feed.tuple_feed_builder import TupleFeedBuilder

class CashFlowFeed(AriesFeed):
    pass

class CashFlowFeedBuilder(TupleFeedBuilder):
    def build(self, dao):
        tuple_feed = TupleFeedBuilder.build(self, dao)
        return CashFlowFeed(tuple_feed)

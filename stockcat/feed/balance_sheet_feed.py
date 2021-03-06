#-*- coding: utf-8 -*-

from stockcat.feed.aries_feed import AriesFeed
from stockcat.feed.tuple_feed_builder import TupleFeedBuilder

class BalanceSheetFeed(AriesFeed):
    pass

class BalanceSheetFeedBuilder(TupleFeedBuilder):
    def build(self, dao):
        tuple_feed = TupleFeedBuilder.build(self, dao)
        return BalanceSheetFeed(tuple_feed)

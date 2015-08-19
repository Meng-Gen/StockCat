#-*- coding: utf-8 -*-

from stockcat.feed.aries_feed import AriesFeed
from stockcat.common.date_utils import DateUtils
from stockcat.synonym.account_synonym import AccountSynonym

class OperatingRevenueFeed(AriesFeed):
    pass

class OperatingRevenueFeedBuilder():
    def __init__(self):
        self.account_synonym = AccountSynonym()
        self.date_utils = DateUtils()

    def build(self, dao):
        tuple_feed = self.__build_tuple(dao)
        return OperatingRevenueFeed(tuple_feed)

    def __build_tuple(self, dao):
        feed = []
        release_date = self.date_utils.get_last_date_of_month(dao.get_date())
        stock_symbol = dao.get_stock_symbol()
        for account, value in dao.get_row_list():
            if self.account_synonym.get(account) == u'當月營收':
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : self.date_utils.get_last_date_of_month(release_date), 
                    'account' : u'當月營收',
                    'account_order' : 1,
                    'value' : value
                }
                feed.append(entry)
        return tuple(feed)

class OperatingRevenueSummaryFeedBuilder():
    def __init__(self):
        self.date_utils = DateUtils()

    def build(self, dao):
        tuple_feed = self.__build_tuple(dao)
        return OperatingRevenueFeed(tuple_feed)

    def __build_tuple(self, dao):
        feed = []
        stmt_date = self.date_utils.get_last_date_of_month(dao.get_stmt_date())
        release_date = dao.get_release_date()
        for row in dao.get_row_list():
            stock_symbol = row[0]
            this_month_value = row[2]
            last_month_value = row[3]
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'當月營收',
                'account_order' : 1,
                'value' : this_month_value
            }
            feed.append(entry)
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : self.date_utils.get_last_date_of_prev_month(stmt_date), 
                'account' : u'上月營收',
                'account_order' : 2,
                'value' : last_month_value
            }
            feed.append(entry)
        return tuple(feed)